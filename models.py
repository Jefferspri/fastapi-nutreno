from fastapi import FastAPI
from pydantic import BaseModel


class Todo(BaseModel):
    sex: str
    age: float 
    height: float
    weight: float
    visual_fat: str
    goal: str 
    gym_experience: str
    work_type: str
    activity_level: float
    excercise_ina_week: float
    excercise_ina_day: float
    
