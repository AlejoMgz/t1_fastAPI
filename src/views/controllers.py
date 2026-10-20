from bson import ObjectId
from src.models.database import collection
from src.models.model import TraineeModel, TraineeUpdateModel

def helper_trainee(trainee) -> dict:
    return{
        "id": str(trainee["_id"]),
        "document": trainee["document"],
        "first_name": trainee["first_name"],
        "last_name": trainee["last_name"],
        "email": trainee["email"],
        "age": trainee["age"],
        "program": trainee["program"],
        "record_number": trainee["record_number"]
    }

def create_trainee(trainee: TraineeModel) -> dict:
    trainee_dict = trainee.model_dump()
    result = collection.insert_one(trainee_dict)
    new_trainee = collection.find_one({"_id": result.inserted_id})
    return helper_trainee(new_trainee)