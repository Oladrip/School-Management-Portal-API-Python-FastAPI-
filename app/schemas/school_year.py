from datetime import date, datetime
from pydantic import BaseModel, field_validator


class Base(BaseModel):
    title: str
    start_date: date
    end_date: date

    @field_validator("title")
    def validate_title(cls, value):
        if not value:
            raise ValueError('Title must not be empty.')
        return value

    @field_validator("start_date", mode="before")
    def parse_start_date(cls, value):
        if isinstance(value, date):
            return value
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    @field_validator("end_date", mode="before")
    def parse_end_date(cls, value):
        if isinstance(value, date):
            return value
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    @field_validator("end_date")
    def validate_start_and_end_date(cls, v, values):
        if values.data.get('start_date') and values.data.get('start_date') >= v:
             raise ValueError('End date is bigger than or equal to start date.')
        return v


class SchoolYearCreate(Base):
    pass


class SchoolYearUpdate(Base):
    pass


class SchoolYearInDB(Base):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
