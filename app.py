#!/usr/bin/python3
from typing import List
import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from fastapi.param_functions import Query
from fastapi.responses import RedirectResponse
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": "Departements Methods"},
    {"name": "Towns Methods"},
    {"name": "Districts Methods"},
    {"name": "Neighborhoods Methods"},
]

app = FastAPI(
    title="bj Découpage territorial",
    description="bj Découpage territorial avec fastAPI",
    openapi_tags=tags_metadata
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', include_in_schema=False)
async def docs():
    return RedirectResponse("/docs")


@app.get("/departments", tags=["Departements Methods"], response_model=List[schemas.Department])
async def get_departments(db: Session = Depends(get_db)):
    departments = crud.get_departments(db)
    if departments:
        return departments
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/departments/{name}/towns", tags=["Departements Methods"], response_model=schemas.DepartmentTowns)
async def get_departement_towns(name: str, db: Session = Depends(get_db)):
    department_towns = crud.get_departement_towns(db, name)
    if department_towns:
        return department_towns
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/departments/{name}/districts", tags=["Departements Methods"], response_model=schemas.DepartmentDistrict)
async def get_department_district(name: str, db: Session = Depends(get_db)):
    department_districts = crud.get_department_district(db, name)
    if department_districts:
        return department_districts
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/departments/{name}/neighborhoods", tags=["Departements Methods"], response_model=schemas.DepartmentNeighborhoods)
async def get_department_neighborhoods(name: str, db: Session = Depends(get_db)):
    department_neighborhoods = crud.get_department_neighborhoods(db, name)
    if department_neighborhoods:
        return department_neighborhoods
    else: 
        raise HTTPException(status_code=404, detail="No record")


@app.get("/towns", tags=["Towns Methods"], response_model=List[schemas.Town])
async def get_towns(db: Session = Depends(get_db)):
    towns = crud.get_towns(db)
    if towns:
        return towns
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/towns/{town_name}/districts", tags=["Towns Methods"], response_model=schemas.TownDistricts)
async def get_town_districts(town_name: str, db: Session = Depends(get_db)):
    town_districts = crud.get_town_districts(db, town_name)
    if town_districts:
        return town_districts
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/towns/{town_name}/neighborhoods", tags=["Towns Methods"], response_model=schemas.TownNeighborhoods)
async def get_town_neighborhoods(town_name: str, db: Session = Depends(get_db)):
    town_neighborhoods = crud.get_town_neighborhoods(db, town_name)
    if town_neighborhoods:
        return town_neighborhoods
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/districts", tags=["Districts Methods"], response_model=List[schemas.District])
async def get_districts(db: Session = Depends(get_db)):
    districts = crud.get_districts(db)
    if crud.get_districts(db):
        return districts
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/districts/{district_name}/neighborhoods", tags=["Districts Methods"], response_model=schemas.DistrictNeighborhoods)
async def get_district_neighborhoods(district_name: str, db: Session = Depends(get_db)):
    district_neighborhoods = crud.get_district_neighborhoods(db, district_name)
    if district_neighborhoods:
        return district_neighborhoods
    else:
        raise HTTPException(status_code=404, detail="No record")


@app.get("/neighborhoods", tags=["Neighborhoods Methods"], response_model=schemas.NeighborhoodPage)
async def get_neighborhoods(page: int = Query(1, description="Number of page"), page_size: int = Query(20, description="Number of element per page"), db: Session = Depends(get_db)):
    neighborhoods = crud.get_neighborhoods(db, page, page_size)
    if neighborhoods:
        return neighborhoods
    else:
        raise HTTPException(status_code=404, detail="No record")

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=5000,
                reload=True, debug=True, workers=3)
