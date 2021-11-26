from os import SEEK_CUR
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
import paginate_sqlalchemy

from . import models


def get_departments(db: Session):
    return db.query(models.Department.name).all()

def get_departement_towns(db: Session, department_name: str):
    towns = db.query(models.Town.name).join(
        models.Department, models.Department.id == models.Town.department_id
    ).filter(
        models.Department.name == department_name
    ).all()

    datas = {
        "department": department_name,
        "towns": towns
    }

    return datas

def get_department_district(db: Session, department_name: str):
    districts = db.query(
        models.District.name
    ).join(
        models.Town, models.Town.id == models.District.town_id
    ).join(
        models.Department, models.Department.id == models.Town.department_id
    ).filter(
        models.Department.name == department_name
    ).all()

    datas = {
        "department": department_name,
        "districts": districts
    }
    return datas


def get_department_neighborhoods(db: Session, department_name: str):
    neighborhoods = db.query(
        models.Neighborhood.name
    ).join(
        models.District, models.District.id == models.Neighborhood.district_id
    ).join(
        models.Town, models.Town.id == models.District.town_id
    ).join(
        models.Department, models.Department.id == models.Town.department_id
    ).filter(models.Department.name == department_name).all()

    datas = {
        "department": department_name,
        "neighborhoods": neighborhoods
    }

    return datas


def get_towns(db: Session):
    return db.query(models.Town.name).all()

def get_town_districts(db: Session, town_name: str):
    districts = db.query(models.District.name).join(
        models.Town, models.Town.id == models.District.town_id
    ).filter(
        models.Town.name == town_name
    ).all()
    
    datas = {
        "town": town_name,
        "districts": districts
    }
    return datas


def get_town_neighborhoods(db: Session, town_name: str):
    neighborhoods = db.query(models.Neighborhood.name).join(
        models.District, models.District.id == models.Neighborhood.district_id
    ).join(
        models.Town, models.Town.id == models.District.town_id
    ).filter(
        models.Town.name == town_name
    ).all()

    datas = {
        "town": town_name,
        "neighborhoods": neighborhoods
    }

    return datas

def get_districts(db: Session):
    return db.query(models.District.name).all()


def get_district_neighborhoods(db: Session, district_name: str):
    districts = db.query(models.Neighborhood.name).join(
        models.District, models.District.id == models.Neighborhood.district_id
    ).filter(
        models.District.name == district_name
    ).all()
    datas = {
        "district": district_name,
        "neighborhoods": districts
    }
    return datas


def get_neighborhoods(db: Session, page: int = 1, page_size: int = 20):
    neighborhoods_query = db.query(models.Neighborhood.name)
    neighborhoods = paginate_sqlalchemy.SqlalchemyOrmPage(
        neighborhoods_query, 
        page=page, 
        items_per_page=page_size
    )
    datas = {
        "total": neighborhoods.item_count,
        "per_page": neighborhoods.items_per_page,
        "page": neighborhoods.page,
        "last_page": neighborhoods.last_page,
        "data": neighborhoods.items
    }
    return datas
