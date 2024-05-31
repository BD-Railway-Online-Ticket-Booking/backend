from typing import List
from pydantic import BaseModel
from datetime import date, datetime, time


class SeatSchemaOut(BaseModel):
    id: int
    type: str
    price: int
    capacity: int

    class Config:
        orm_mode = True


class TrainSchemaOut(BaseModel):
    id: int
    name: str
    seats: List[SeatSchemaOut]

    class Config:
        orm_mode = True



class SeatSchemaIn(BaseModel):
    type: str
    price: int
    capacity: int

    class Config:
        orm_mode = True


class TrainSchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PlaceSchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class RouteSchemaIn(BaseModel):
    source_id: int
    destination_id: int
    distance: int
    leavetime: time
    reachtime: time
    train_id: int


class RouteSchemaOut(BaseModel):
    id: int
    source_name: str
    destination_name: str
    distance: int
    leavetime: time
    reachtime: time
    train_name: str

    class Config:
        orm_mode = True


class pathsh1(BaseModel):
    source_name: str
    destination_name: str
    distance: int
    leavetime: time
    duration: int

    class Config:
        orm_mode = True

class pathsh2(BaseModel):
    source_name:str
    destination_name:str
    distance:int

    class Config:
        orm_mode=True

class TrainRouteSchema1(BaseModel):
    train_id: int
    train_name: str
    path: List[pathsh1]

    class Config:
        orm_mode = True

class TrainRouteSchema2(BaseModel):
    train_id: int
    train_name: str
    path: List[pathsh2]

    class Config:
        orm_mode = True


class AvailSeat(BaseModel):
    id: int
    type: str
    price: int
    available: int

    class Config:
        orm_mode = True