import re
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, field_validator
from app.schemas.nationality import NationalityInDB


class Base(BaseModel):
    first_name: str
    father_name: str
    gfather_name: str
    last_name: str
    gender: bool
    date_of_birth: date
    guardian_phone_no: str

    @field_validator("first_name")
    def validate_first_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError('First name must not be empty.')
        return value

    @field_validator("father_name")
    def validate_father_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError('Father name must not be empty.')
        return value

    @field_validator("gfather_name")
    def validate_gfather_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError('Grand Father name must not be empty.')
        return value

    @field_validator("last_name")
    def validate_last_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError('Last name must not be empty.')
        return value

    @field_validator("date_of_birth", mode="before")
    def parse_date_of_birth(cls, value):
        if isinstance(value, date):
            return value
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    @field_validator("guardian_phone_no")
    def validate_guardian_phone_no(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError('Guardian phone number must not be empty.')
        if not re.match(r'^\d{9}$', value):
            raise ValueError('Please Enter a valid phone number.')

        return value


class StudentCreate(Base):
    nationality_id: int


class StudentUpdate(StudentCreate):
    pass


class StudentInDB(Base):
    id: int
    nationality: NationalityInDB

    class Config:
        from_attributes = True
