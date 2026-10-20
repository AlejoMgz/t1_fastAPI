from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# agragamos la conexion a la base de datos mogo db
MONGO_URI = "mongodb+srv://alejitomg7519_db_user:ipEEJtyFhgjj3aiU@cluster0.s9yhxbm.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)


db = client.data_ap
collection = db.trainee

#intentar obtener la informacion del servidor para verificar la conexión 
try:
    client.server_info()
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error de conexión a MongoDB: {e}")

finally:
    # cerrar la conexión al cliente de MongoDB
    client.close()