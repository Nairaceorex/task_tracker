from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str = "in progress"

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config:
        orm_mode = True
