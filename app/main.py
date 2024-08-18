from database import Base, engine, get_db
from models import Task
from schemas import TaskCreate, Task

Base.metadata.create_all(bind=engine)
