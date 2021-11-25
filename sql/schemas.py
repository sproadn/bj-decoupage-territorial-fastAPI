from os import name
from typing import List

from pydantic import BaseModel

from sql.database import Base


class NeighborhoodOut(BaseModel):
    name: str

class Neighborhood(BaseModel):
    id: int
    name: str
    district_id: int

    class Config:
        orm_mode = True

class District(BaseModel):
    id: int
    name: str
    town_id: int
    neighborhoods: List[Neighborhood] = []

    class Config:
        orm_mode = True


class Town(BaseModel):
    id: int
    name: str
    department_id: str
    districts: List[District] = []

    class Config:
        orm_mode = True


class Department(BaseModel):
    id: int
    name: str
    towns: List[Town] = []

    class Config:
        orm_mode = True
