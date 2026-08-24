from sqlalchemy import Column, Integer, String

from app.database import Base


class Instance(Base):
    __tablename__ = "instances"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpu = Column(Integer, nullable=False)
    memory = Column(Integer, nullable=False)
    region = Column(String, nullable=False)
    status = Column(String, nullable=False)