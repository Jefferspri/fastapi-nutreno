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
    "sexo":"M", 
    "edad":25, 
    "altura":1.68, 
    "peso":65,
    "obesidad_visual":"baja",
    "objetivo":"mantener", 
    "experiencia_gimnasio":"menos de 1 año",
    "tipo_trabajo":"no activo",
    "nivel_actividad": "2. Ejercicios suaves",
    "ejercicio_semanal":2,
    "ejercicio_diario":40
    }
    """
    # 'sexo':['M','F'], 'obesidad_visual':['baja','alta'], 'objetivo':['bajar','mantener','subir'], 'experiencia_gimnasio':['menos de 1 año', 'más de 1 año'], 'work_type':['no activo', 'activo'] , 'Nivel de actividad': according to MB table.
    user = todo

    #BMI = user['weight']/(user['height'])**2
    BMI = user.peso/(user.altura)**2

    print('BMI: ', BMI)

    #  Calculo de IMC
    if BMI >= 30 and user.obesidad_visual=='alta':
        if user.sex == 'M':
            Ideal_weight = user.altura*100 - 100 - (user.altura*100-150)/4
        else:
            Ideal_weight = user.altura*100 - 100 - (user.altura*100-150)/2
            
        user.peso = (user.peso-Ideal_weight)*0.25 + Ideal_weight

    print('Weight: ', user.peso)

    # Calculo de tasa metabolica basal
    if user.sexo == 'M':
        TMB = 10*user.peso + 6.25*user.altura*100 - 5*user.edad + 5
    else:
        TMB = 10*user.peso + 6.25*user.altura*100 - 5*user.edad - 161

    print('TMB: ', TMB)

    # Efecto termico de los alimentoos
    ETA = 1.1 # usually is 10%

    # Termogenesis de la actividad física que no es ejercicio
    if user.tipo_trabajo == 'no activo':
        NEAT = 1.15
    else:
        NEAT = 1.3 

    print('NEAT: ', NEAT)

    # Factor de actividad fisica
    if user.nivel_actividad == "1. Sedentario":
        FA = 1.2
    elif user.nivel_actividad == "2. Ejercicios suaves":
        FA = 1.375
    elif user.nivel_actividad == "3. Moderadamente activo":
        FA = 1.55
    elif user.nivel_actividad == "4. Muy activo":
        FA = 1.725
    elif user.nivel_actividad == "5. Hiperactivo":
        FA = 1.9

    # METS
    MET = 5  # fijarse en tabla METs
    METS = 0.0175*MET*user.peso*user.ejercicio_diario/2  # entre 2 porque se hace la mitad

    print('METS: ', METS)

    # Calculo de gasto calorico total
    if user.experiencia_gimnasio == 'más de 1 año' or (user.experiencia_gimnasio == 'menos de 1 año' and user.sexo == 'M'):
        GET = TMB*ETA*NEAT*FA
    else:
        GET = TMB*ETA*NEAT+METS

    print('GET: ', GET)   

    # Gasto calorico por factor objetivo
    if user.objetivo == 'bajar':
        GET = GET*1.2  # 1.2
    elif user.objetivo =='subir':
        GET = GET*0.8

    print('GET: ', GET) 
    return {"message": GET}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}