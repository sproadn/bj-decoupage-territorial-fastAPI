from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    towns = relationship("Town", back_populates="department")


class Town(Base):
    __tablename__ = "towns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("Department", back_populates="towns")
    districts = relationship("District", back_populates="town")


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    town_id = Column(Integer, ForeignKey('towns.id'))

    town = relationship("Town", back_populates="districts")
    neighborhoods = relationship("Neighborhood", back_populates="district")


class Neighborhood(Base):
    __tablename__ = "neighborhoods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    district_id = Column(Integer, ForeignKey('districts.id'))

    district = relationship("District", back_populates="neighborhoods")

