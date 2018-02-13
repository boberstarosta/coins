import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Sequence, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Metal(Base):
    __tablename__ = 'metal'

    id = Column(Integer, Sequence('metal_id_seq'), primary_key=True)
    name = Column(String(length=50))

    prices = relationship('Price', back_populates='metal')
    coins = relationship('Coin', back_populates='metal')


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, Sequence('price_id_seq'), primary_key=True)
    metal_id = Column(Integer, ForeignKey('metal.id'))
    time = Column(DateTime, default=datetime.datetime.now)
    value = Column(Float)

    metal = relationship('Metal', back_populates='prices')


class Coin(Base):
    __tablename__ = 'coin'

    id = Column(Integer, Sequence('coin_id_seq'), primary_key=True)
    metal_id = Column(Integer, ForeignKey('metal.id'))

    metal = relationship('Metal', back_populates='coins')
