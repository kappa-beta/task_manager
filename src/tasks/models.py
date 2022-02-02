from sqlalchemy import Column, Integer, String, Date, ForeignKey

from ..database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False)
    description = Column(String)
    plan_start = Column(Date)
    plan_end = Column(Date)
    executors = Column(String)


class TimeLog(Base):
    __tablename__ = 'time_log'

    id = Column(Integer, primary_key=True)
    time_log_id = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    start = Column(Date)
    end = Column(Date)
