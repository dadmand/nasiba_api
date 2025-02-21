from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ThirdPartyBase(BaseModel):
    """Base schema with shared attributes for Third Party entities."""
    c_third_party_id: str = Field(alias="third_party_id")
    c_first_name: str = Field(alias="first_name")
    c_last_name: str = Field(alias="last_name")
    c_national_id: str = Field(alias="national_id")
    c_phone_number: str = Field(alias="phone_number")
    c_birth_date: date = Field(alias="birth_date")
    c_amount: float = Field(alias="amount")
    c_number_of_repayments: int = Field(alias="number_of_repayments")


class ThirdPartyCreate(BaseModel):
    """Schema for creating a new Third Party."""
    third_party_id: str
    first_name: str
    last_name: str
    national_id: str
    phone_number: str
    birth_date: date
    amount: float
    number_of_repayments: int


class ThirdPartyResponse(BaseModel):
    """Schema for Third Party responses, including database ID."""
    id: int = Field(alias="c_id")
    third_party_id: str = Field(alias="c_third_party_id")
    first_name: str = Field(alias="c_first_name")
    last_name: str = Field(alias="c_last_name")
    national_id: str = Field(alias="c_national_id")
    phone_number: str = Field(alias="c_phone_number")
    birth_date: date = Field(alias="c_birth_date")
    amount: float = Field(alias="c_amount")
    number_of_repayments: int = Field(alias="c_number_of_repayments")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )


class ThirdPartyUpdate(BaseModel):
    """Schema for updating an existing Third Party."""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    amount: Optional[float] = None
    number_of_repayments: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)