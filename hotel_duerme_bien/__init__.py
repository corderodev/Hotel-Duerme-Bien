#pip install firebase-admin (Instalar el admin de firebase)
#placeholder en init, para crear funciones CRUD
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Iniciar Firebase con las credenciales descargadas desde el proyecto.
cred = credentials.Certificate("SDK/hotel-duerme-bien--desapps.json")#Poner direccion el SDK
#asegurarse que el SDK esta siempre junto la app
firebase_admin.initialize_app(cred)

# referencia a la base de datos de Firestore
db = firestore.client()

#tambien puede sobreescribir documentos, solo si no se le da un nuevo ID
def crear_documento(coleccion, id_documento, datos):
    try:
        # esto crea un nuevo documento
        doc_ref = db.collection(coleccion).document(id_documento)
        
        # requiere datos del documento
        doc_ref.set(datos)
        
        print("Documento creado con ID:", doc_ref.id)
    except Exception as e:
        print("Error al crear el documento:", e)

def recuperar_documento_id(coleccion, id_documento):
    try:
        #referencia al documento 
        doc_ref = db.collection(coleccion).document(id_documento)
        
        #aqui se recupera el documento
        doc = doc_ref.get()

        #se retorna el documento como un diccionario
        return doc.to_dict()
    except Exception as err:
        print(err)

#se hace pasar un documento por update
#se actualiza el documento cuyo id se entregue
def actualizar_documento_id(coleccion, id_documento, update):
    try:
        #ref doc
        doc_ref = db.collection(coleccion).document(id_documento)

        #se hace pasar el documento a update()
        doc_ref.update(update)

        print("Actualizacion exitosa.")
    except Exception as err:
        print(err)


def borrar_documento_id(coleccion, id_documento):
    try:
        db.collection(coleccion).document(id_documento).delete()

        print("Documento eliminado.")
    except Exception as err:
        print(err)
# Ejemplo de uso
datos_documento = {
    "nombre": "Pedro",
    "Apellido": "Arayan",
    "RUT": "12345678-9876",
    "Tipo de pasajero": "Comúne"
}

#para actualizar tira error con tipo de pasajero
#es porque tiene espacios en blanco
#se evita escribiendo las keys sin espacios en blanco
update = {
    "nombre": "PETTER",
    "Apellido": "PARKER",
    "RUT": "RUN",
}

#En colección el nombre de la colección y en el ID el id que quieran asignarle a la colección
#crear_documento("Colección", "ID", datos_documento)
actualizar_documento_id("Colección", "ID", update) 
print(recuperar_documento_id("Colección", "ID"))
borrar_documento_id("Colección", "ID2")