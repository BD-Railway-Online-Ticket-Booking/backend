from typing import List
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Time, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship


class Seat(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    train_id = Column(Integer, ForeignKey("trains.id"))
    train = relationship("Train", foreign_keys=[train_id], back_populates="seats")


class Train(Base):
    __tablename__ = "trains"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    seats = relationship("Seat", back_populates="train", cascade="all, delete")


class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)


class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("places.id"))
    source = relationship("Place", foreign_keys=[source_id])
    destination_id = Column(Integer, ForeignKey("places.id"))
    destination = relationship("Place", foreign_keys=[destination_id])
    distance = Column(Integer, nullable=False)
    leavetime = Column(Time, nullable=False)
    reachtime = Column(Time, nullable=False)
    train_id = Column(Integer, ForeignKey("trains.id"))
    train = relationship("Train", foreign_keys=[train_id])
    
class BookingLog(Base):
    __tablename__ = "booking_logs"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id"))
    seat = relationship("Seat", foreign_keys=[seat_id])
    available = Column(Integer, nullable=False)
    booked= Column(Integer, nullable=False)