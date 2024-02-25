from typing import Optional

from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    variable = "Hello dear user, welcome to the future"
    return {"message": variable}


@app.post("/kcal")
async def create_todos(todo: Todo):
    # Jefferson
    """
    {
    "sex":"M", 
    "age":25, 
    "height":1.68, 
    "weight":65,
    "visual_fat":"low",
    "goal":"flow", 
    "gym_experience":"-1",
    "work_type":"no active",
    "activity_level": 2,
    "excercise_ina_week":2,
    "excercise_ina_day":40
    }
    """
    user = todo

    #BMI = user['weight']/(user['height'])**2
    BMI = user.weight/(user.height)**2

    print('BMI: ', BMI)

    #  Calculo de IMC
    if BMI >= 30 and user.visual_fat=='high':
        if user.sex == 'M':
            Ideal_weight = user.height*100 - 100 - (user.height*100-150)/4
        else:
            Ideal_weight = user.height*100 - 100 - (user.height*100-150)/2
            
        user.weight = (user.weight-Ideal_weight)*0.25 + Ideal_weight

    print('Weight: ', user.weight)

    # Calculo de tasa metabolica basal
    if user.sex == 'M':
        TMB = 10*user.weight + 6.25*user.height*100 - 5*user.age + 5
    else:
        TMB = 10*user.weight + 6.25*user.height*100 - 5*user.age - 161

    print('TMB: ', TMB)

    # Efecto termico de los alimentoos
    ETA = 1.1 # usually is 10%

    # Termogenesis de la actividad física que no es ejercicio
    if user.work_type == 'no active':
        NEAT = 1.15
    else:
        NEAT = 1.3 

    print('NEAT: ', NEAT)

    # Factor de actividad fisica
    if user.activity_level == 1:
        FA = 1.2
    elif user.activity_level == 2:
        FA = 1.375
    elif user.activity_level == 3:
        FA = 1.55
    elif user.activity_level == 4:
        FA = 1.725
    elif user.activity_level == 5:
        FA = 1.9

    # METS
    MET = 5  # fijarse en tabla METs
    METS = 0.0175*MET*user.weight*user.excercise_ina_day/2  # entre 2 porque se hace la mitad

    print('METS: ', METS)

    # Calculo de gasto calorico total
    if user.gym_experience == '+1' or (user.gym_experience == '-1' and user.sex == 'M'):
        GET = TMB*ETA*NEAT*FA
    else:
        GET = TMB*ETA*NEAT+METS

    print('GET: ', GET)   

    # Gasto calorico por factor objetivo
    if user.goal == 'up':
        GET = GET*1.2  # 1.2
    elif user.goal=='low':
        GET = GET*0.8

    print('GET: ', GET) 
    return {"message": GET}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}