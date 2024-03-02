from fastapi import FastAPI
from pydantic import BaseModel


class Todo(BaseModel):
    sexo: str
    edad: float 
    altura: float
    peso: float
    obesidad_visual: str
    objetivo: str 
    experiencia_gimnasio: str
    tipo_trabajo: str
    nivel_actividad: str
    ejercicio_semanal: float
    ejercicio_diario: float
    
