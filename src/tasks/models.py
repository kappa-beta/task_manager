from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False)
    description = Column(String)
    plan_start = Column(Date)
    plan_end = Column(Date)
    executors = Column(String)

    time_log = relationship('TimeLog', back_populates='task')


class TimeLog(Base):
    __tablename__ = 'time_log'

    id = Column(Integer, primary_key=True)
    time_log_id = Column(Integer, ForeignKey('task.id', ondelete='CASCADE'), nullable=False)
    start = Column(Date, nullable=False)
    end = Column(Date)

    task = relationship('Task', back_populates='time_log')
