# database/models.py

# lib
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime, timezone, timedelta
# module

# attribute
BASE = declarative_base()

class Trend(BASE):
    __tablename__="trend"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(45))
    created_at = Column(TIMESTAMP, default=lambda:datetime.now(timezone.utc), nullable=False)
    rank_1 = Column(String(45))
    rank_2 = Column(String(45))
    rank_3 = Column(String(45))
    rank_4 = Column(String(45))
    rank_5 = Column(String(45))
    rank_6 = Column(String(45))
    rank_7 = Column(String(45))
    rank_8 = Column(String(45))
    rank_9 = Column(String(45))
    rank_10 = Column(String(45))
    rank_11 = Column(String(45))
    rank_12 = Column(String(45))
    rank_13 = Column(String(45))
    rank_14 = Column(String(45))
    rank_15 = Column(String(45))
    rank_16 = Column(String(45))
    rank_17 = Column(String(45))
    rank_18 = Column(String(45))
    rank_19 = Column(String(45))
    rank_20 = Column(String(45))


class Test(BASE):
    __tablename__="test"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))
