from os import name
from typing import List

from pydantic import BaseModel

from .database import Base

class Department(BaseModel):
    name: str


class Town(BaseModel):
    name: str


class District(BaseModel):
    name: str


class Neighborhood(BaseModel):
    name: str

class DepartmentTowns(BaseModel):
    department: str
    towns: List[Town]


class DepartmentDistrict(BaseModel):
    department: str
    districts: List[District]


class DepartmentNeighborhoods(BaseModel):
    department: str
    neighborhoods: List[Neighborhood]


class TownDistricts(BaseModel):
    town: str
    districts: List[District]


class TownNeighborhoods(BaseModel):
    town: str
    neighborhoods: List[Neighborhood]


class DistrictNeighborhoods(BaseModel):
    district: str
    neighborhoods: List[Neighborhood]


class NeighborhoodPage(BaseModel):
    total: int
    per_page: int
    page: int
    last_page: int
    data: List[Neighborhood]
    
