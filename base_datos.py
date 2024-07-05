import json

# Base de datos de ejemplo con puntajes de países
dicc = {
    "España": 1,
    "Italia": 0
}

# Convertir el diccionario a una cadena JSON
data = json.dumps(dicc)
print( data)

# Guardar los datos en un archivo JSON
with open("base_de_datos.json", "w") as archivo:
    archivo.write(data)  # Escribimos la cadena JSON en el archivo

# Solicitar datos de inicio de sesión
user_ = "admin"
pwd_ = "123"
print("Ingrese sus datos")
print("Usuario: ")
user = input()
print("Contraseña: ")
pwd = input()

# Validar las credenciales del usuario
if user == user_ and pwd == pwd_:
    print("Bienvenido a la base de datos")

    # Leer los datos del archivo JSON
    with open("base_de_datos.json", "r") as archivo:
        data = json.load(archivo) 
        # Leemos la cadena JSON del archivo y la convertimos a un diccionario
        print("Datos leídos del archivo:\n", data)
else:
    print("Usuario o contraseña inválido")