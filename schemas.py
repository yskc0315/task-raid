from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    title: str
    difficulty: int

class TaskUpdate(BaseModel):
    completed: bool

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    title: str
    difficulty: int
    completed: bool
    exp: int