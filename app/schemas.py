from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        description="Employee Name"
    )

    department: str = Field(
        min_length=2,
        max_length=50,
        description="Department Name"
    )


class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True