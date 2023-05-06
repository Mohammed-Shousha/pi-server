import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio
from bson import ObjectId
from models import MedicineModel, PrescriptionModel, PrescriptionMedicineModel
from utils import (
    separate_medicines,
    update_medicines,
    update_prescription,
    create_prescription_with_unavailable_medicines,
)

app = FastAPI()

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI"])

db = client.SAP


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/medicines", response_model=list[MedicineModel])
async def list_medicines():
    medicines = await db["medicines"].find().to_list(length=1000)

    return medicines


@app.get("/otc-medicines", response_model=list[MedicineModel])
async def list_otc_medicines():
    medicines = await db["medicines"].find({"otc": True}).to_list(length=1000)

    return medicines


@app.get("/medicines/{id}", response_model=MedicineModel)
async def show_medicine(id: str):
    if (medicine := await db["medicines"].find_one({"_id": ObjectId(id)})) is not None:
        return medicine

    raise HTTPException(
        status_code=404,
        detail=f"Medicine with id: {id} not found",
    )


@app.get("/prescriptions", response_model=list[PrescriptionModel])
async def list_prescriptions():
    prescriptions = await db["prescriptions"].find().to_list(length=1000)

    return prescriptions


@app.get("/prescriptions/{id}", response_model=PrescriptionModel)
async def show_prescription(id: str):
    if (
        prescription := await db["prescriptions"].find_one({"_id": ObjectId(id)})
    ) is not None:
        return prescription

    raise HTTPException(status_code=404, detail=f"Prescription with id: {id} not found")


@app.post(
    "/verify-prescription-medicines-availability/{prescription_id}",
)
async def verify_prescription_medicines_availability(prescription_id: str):
    if (
        prescription := await db["prescriptions"].find_one(
            {"_id": ObjectId(prescription_id)}
        )
    ) is None:
        raise HTTPException(
            status_code=404,
            detail=f"Prescription with id: {prescription_id} not found",
        )

    if prescription["isPaid"] == False:
        raise HTTPException(
            status_code=402,
            detail="Prescription is not paid",
        )

    if prescription["isRecived"] == True:
        raise HTTPException(
            status_code=400,
            detail="Prescription is already recived",
        )

    prescription_medicines = prescription["medicines"]

    medicines = await db["medicines"].find().to_list(length=1000)

    available_medicines, unavailable_medicines = separate_medicines(
        prescription_medicines, medicines
    )

    return {
        "available_medicines": available_medicines,
        "unavailable_medicines": unavailable_medicines,
    }


@app.post("/process-prescription/{prescription_id}")
async def process_prescription(
    prescription_id: str,
    available_medicines: list[PrescriptionMedicineModel],
    unavailable_medicines: list[PrescriptionMedicineModel],
):
    received = False
    created = False

    available_medicines = jsonable_encoder(available_medicines)

    unavailable_medicines = jsonable_encoder(unavailable_medicines)

    if len(unavailable_medicines) > 0:
        created = await create_prescription_with_unavailable_medicines(
            db, prescription_id, unavailable_medicines
        )

    # TODO: get availableMedicines using GPIO

    await update_medicines(db, available_medicines)

    await update_prescription(db, prescription_id)

    received = True  # TODO: get received using GPIO

    return {
        "received": received,
        "created": created,
    }


@app.post("/order-medicines")
async def order_medicines(medicines: list[PrescriptionMedicineModel]):
    medicines = jsonable_encoder(medicines)

    db_medicines = await db["medicines"].find().to_list(length=1000)

    available_medicines, unavailable_medicines = separate_medicines(
        medicines, db_medicines
    )

    if len(unavailable_medicines) > 0:
        raise HTTPException(
            status_code=400,
            detail="Medicines are not available",
        )

    await update_medicines(db, available_medicines)

    return {"message": "Medicines ordered successfully"}
