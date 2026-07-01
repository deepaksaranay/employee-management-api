from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models import Base
from app import crud, schemas

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    version="2.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Employee Management API with SQLite Database"
    }


@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(db, employee)


@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def read_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee(db, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@app.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    db_employee = crud.update_employee(db, employee_id, employee)

    if db_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return db_employee


@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.delete_employee(db, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }