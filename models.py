from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime
from typing import Optional


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MedicineModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    price: float = Field(...)
    otc: bool = Field(...)
    availableQuantity: int = Field(...)
    position: dict[str, int] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class PrescriptionMedicineModel(BaseModel):
    medicineId: str = Field(...)
    medicineName: str = Field(...)
    quantity: int = Field(...)
    price: float = Field(...)
    position: Optional[dict[str, int]]
    doctorInstructions: Optional[str]


class PrescriptionModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    patientId: PyObjectId = Field(default_factory=PyObjectId)
    doctorId: PyObjectId = Field(default_factory=PyObjectId)
    date: datetime = Field(...)
    isPaid: bool = Field(...)
    isReceived: bool = Field(...)
    medicines: list[PrescriptionMedicineModel] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
