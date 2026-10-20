from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# agragamos la conexion a la base de datos mogo db
MONGO_URI = "mongodb+srv://alejitomg7519_db_user:ipEEJtyFhgjj3aiU@cluster0.s9yhxbm.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

#crear la base de datos y la coleccion
db = client.amb703
collection = db.mesa

#crear el modelo de datos para la coleccion
nueva_mesa = {
    "name": "Alejo Mesa",
    "status": "Alive",
    "species": "Human",
    "gender": "Male"
}
#insertar el documento en la coleccion
collection.insert_one(nueva_mesa)
print("Documento insertado en la colección 'mesa' de la base de datos 'amb703'")


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