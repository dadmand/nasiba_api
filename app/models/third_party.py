from sqlalchemy import Integer, String, Date, Float
from sqlalchemy.orm import mapped_column, Mapped, validates
from datetime import date
from app.core.database import Base
from typing import Optional

class ThirdParty(Base):
    
    __tablename__ = "T_THIRD_PARTY"
    __table_args__ = {'comment': 'Table storing third party information'}

    # Primary key and identification
    c_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, comment="Auto-incrementing primary key")
    c_third_party_id: Mapped[str] = mapped_column(String(50), unique=True, index=True, comment="Unique business identifier")
    
    # Personal information
    c_first_name: Mapped[str] = mapped_column(String(100), comment="First name of the third party")
    c_last_name: Mapped[str] = mapped_column(String(100), comment="Last name of the third party")
    c_national_id: Mapped[str] = mapped_column(String(20), comment="National identification number")
    c_phone_number: Mapped[str] = mapped_column(String(20), comment="Contact phone number")
    c_birth_date: Mapped[date] = mapped_column(Date, comment="Date of birth")
    
    # Financial information
    c_amount: Mapped[float] = mapped_column(Float, comment="Financial amount associated")
    c_number_of_repayments: Mapped[int] = mapped_column(Integer, comment="Number of repayment installments")

    @validates('c_phone_number')
    def validate_phone(self, key: str, phone_number: str) -> str:
        """Validate phone number format"""
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits")
        if not (8 <= len(phone_number) <= 15):
            raise ValueError("Phone number must be between 8 and 15 digits")
        return phone_number

    @validates('c_national_id')
    def validate_national_id(self, key: str, national_id: str) -> str:
        """Validate national ID format"""
        if not national_id.strip():
            raise ValueError("National ID cannot be empty")
        return national_id.strip()

    def __repr__(self) -> str:
        """String representation of the ThirdParty instance"""
        return f"<ThirdParty(id={self.c_third_party_id}, name={self.c_first_name} {self.c_last_name})>"

    @property
    def full_name(self) -> str:
        """Return the full name of the third party"""
        return f"{self.c_first_name} {self.c_last_name}"