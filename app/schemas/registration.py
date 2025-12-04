from pydantic import BaseModel, field_validator
from .student import StudentInDB
from .grade import GradeInDB
from .school_year import SchoolYearInDB


class Base(BaseModel):
    regi_no: str
    student_id: int
    grade_id: int
    school_year_id: int

    @field_validator("regi_no")
    def validate_regi_no(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError('Registration number must not be empty.')
        return value


class RegistrationCreate(Base):
    pass


class RegistrationUpdate(Base):
    pass


class RegistrationIn(BaseModel):
    student_id: int
    grade_id: int


class RegistrationOut(BaseModel):
    id: int
    regi_no: str
    student: StudentInDB
    grade: GradeInDB
    school_year: SchoolYearInDB

    class Config:
        from_attributes = True
