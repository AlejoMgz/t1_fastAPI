from src.templates.controllers import create_trainee, get_all_trainees,get_trainee_by_id, update_trainee,delete_trainee

from src.models.model import TraineeModel, TraineeUpdateModel
from fastapi import FastAPI, HTTPException, status
#uvicorn src.main:app --reload 
app = FastAPI(
    title="gestion de datos de los apendices",
    description="API simple de fastAPI para consumir los datos de los aprendices",
    version="1.0.0"
)
#mesaje de bienvenida
@app.get("/")
async def root():
    return{"message": "API simple de fastAPI y desplegada en RENDER "}

# registrar aprendices
@app.post(
    "/trainee/", response_description="Registrar un nuevo aprendiz", status_code=status.HTTP_201_CREATED,
)

def create_trainee_api(trainee: TraineeModel):
    #Validar si ya existe el documento
    return create_trainee(trainee)

#Obtener la lista de aprendices

@app.get(
    "/trainees/", response_description="Listar todos los aprendices")

def get_all_trainee_api():
    return get_all_trainees()


#Obtener un aprendiz por id
@app.get(
    "/trainee/{id}", response_description="lista para obtener un aprendiz por su ID"
)
def get_trainee_api(id: str):
    trainee = get_trainee_by_id(id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Aprendiz con ID no encontrado")
    return trainee

#editar un aprendiz por su ID
@app.put(
    "/trainee/{id}", response_description="lista para editar un aprendiz por su ID"
)
def update_trainee_api(id: str, trainee: TraineeUpdateModel):
    updated_trainee = update_trainee(id, trainee)
    if not updated_trainee:
        raise HTTPException(status_code=404, detail="Aprendiz con ID no encontrado")
    return updated_trainee

#eliminar un aprendiz por su ID
@app.delete(
    "/trainee/{id}", response_description="lista para eliminar un aprendiz por su ID"
)
def delete_trainee_api(id: str):
    deleted_trainee = delete_trainee(id)
    if not deleted_trainee:
        raise HTTPException(status_code=404, detail="Aprendiz con ID no encontrado")
    return {"message": "Aprendiz eliminado exitosamente"}