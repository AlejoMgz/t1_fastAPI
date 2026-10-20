from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Agregamos la conexión a la base de datos mongo db
MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

db = client.data_ap
collection = db.trainee

# Intentar obtener la información del servidor para verificar la conexión
try:
    client.server_info()
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error de conexión a MongoDB: {e}")