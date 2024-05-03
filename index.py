import os
import re

class Usuario:
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre},{self.apellido},{self.correo},{self.telefono}"

class GestorUsuarios:
    def __init__(self, archivo='usuarios.txt'):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            print(f"El archivo {self.archivo} no existe. Creando uno nuevo.")
            open(self.archivo, 'w').close()

    def agregar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        telefono = input("Ingrese su número de teléfono: ") 

        if not self.validar_correo(correo):
            print("El correo ya está en uso. Por favor, intente con otro.")
            return

        if not self.validar_telefono(telefono):
            print("El número de teléfono no es válido.")
            return

        usuario = Usuario(nombre, apellido, correo, telefono)
        with open(self.archivo, 'a') as f:
            f.write(str(usuario) + '\n')
        print("Usuario agregado exitosamente.")

    def listar_usuarios(self):
        try:
            with open(self.archivo, 'r') as f:
                usuarios = f.readlines()
            for usuario in usuarios:
                print(usuario.strip())
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no se encontró.")

    def buscar_usuario(self, correo):
        try:
            with open(self.archivo, 'r') as f:
                usuarios = f.readlines()
            for usuario in usuarios:
                if correo in usuario:
                    print(usuario.strip())
                    return
            print("Usuario no encontrado.")
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no se encontró.")

    def eliminar_usuario(self, correo):
        try:
            with open(self.archivo, 'r') as f:
                usuarios = f.readlines()
            with open(self.archivo, 'w') as f:
                for usuario in usuarios:
                    if correo not in usuario:
                        f.write(usuario)
            print("Usuario eliminado si existía.")
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no se encontró.")

    def validar_correo(self, correo):
        patron_correo = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(patron_correo, correo):
            try:
                with open(self.archivo, 'r') as f:
                    if correo in f.read():
                        return False
                return True
            except FileNotFoundError:
                print(f"El archivo {self.archivo} no se encontró.")
                return False
        return False

    def validar_telefono(self, telefono):
        patron_telefono = r'^\+\d{11,16}$'
        return re.match(patron_telefono, telefono)

def menu():
    gestor = GestorUsuarios()
    while True:
        print("1. Agregar usuario")
        print("2. Listar todos los usuarios")
        print("3. Buscar un usuario por correo")
        print("4. Eliminar un usuario por correo")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestor.agregar_usuario()
        elif opcion == '2':
            gestor.listar_usuarios()
        elif opcion == '3':
            correo = input("Ingrese el correo del usuario a buscar: ")
            gestor.buscar_usuario(correo)
        elif opcion == '4':
            correo = input("Ingrese el correo del usuario a eliminar: ")
            gestor.eliminar_usuario(correo)
        elif opcion == '5':
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()


