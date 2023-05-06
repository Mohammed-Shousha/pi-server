from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException
from models import MedicineModel, PrescriptionMedicineModel


async def update_medicines(db, medicines: list[PrescriptionMedicineModel]):
    for medicine in medicines:
        medicine_id = medicine["medicineId"]
        quantity = medicine["quantity"]
        update_result = await db["medicines"].update_one(
            {"_id": ObjectId(medicine_id)}, {"$inc": {"availableQuantity": -quantity}}
        )

        if update_result.modified_count != 1:
            raise HTTPException(
                status_code=500,
                detail="Error updating medicines",
            )

    return True


async def update_prescription(db, prescription_id: str):
    update_result = await db["prescriptions"].update_one(
        {"_id": ObjectId(prescription_id)}, {"$set": {"isRecived": True}}
    )

    if update_result.modified_count != 1:
        raise HTTPException(
            status_code=500,
            detail="Error updating prescription",
        )

    return True


def separate_medicines(
    prescription_medicines: list[PrescriptionMedicineModel],
    medicines: list[MedicineModel],
):
    available_medicines = []
    unavailable_medicines = []

    for medicine in prescription_medicines:
        for db_medicine in medicines:
            if medicine["medicineId"] == str(db_medicine["_id"]):
                if medicine["quantity"] > db_medicine["availableQuantity"]:
                    unavailable_medicines.append(medicine)
                else:
                    medicine["position"] = db_medicine["position"]
                    available_medicines.append(medicine)

    return (available_medicines, unavailable_medicines)


async def create_prescription_with_unavailable_medicines(
    db,
    prescription_id: str,
    unavailable_medicines: list[PrescriptionMedicineModel],
):
    prescription = await db["prescriptions"].find_one(
        {"_id": ObjectId(prescription_id)}
    )

    prescription["_id"] = ObjectId()
    prescription["date"] = datetime.now()
    prescription["isRecived"] = False
    prescription["medicines"] = unavailable_medicines

    new_prescription = await db["prescriptions"].insert_one(prescription)

    created_prescription = await db["prescriptions"].find_one(
        {"_id": new_prescription.inserted_id}
    )

    if (created_prescription) is None:
        raise HTTPException(
            status_code=500,
            detail="Error creating prescription",
        )

    return True
