import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Metal(Base):
    __tablename__ = 'metal'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))

    prices = relationship('Price', back_populates='metal')
    coins = relationship('Coin', back_populates='metal')


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True, autoincrement=True)
    metal_id = Column(Integer, ForeignKey('metal.id'))
    time = Column(DateTime, default=datetime.datetime.now)

    metal = relationship('Metal', back_populates='prices')


class Coin(Base):
    __tablename__ = 'coin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    metal_id = Column(Integer, ForeignKey('metal.id'))

    metal = relationship('Metal', back_populates='coins')
