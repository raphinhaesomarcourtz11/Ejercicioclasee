


USUARIO_BBDD="ADMIN"
PASSWORD_BBDD=1234
print("escribe un nombre para tu usuario")
usuario=(input())
print("es necesario que te inventes una contrasena")
contrasena=int(input())

if(usuario == USUARIO_BBDD) and (contrasena == PASSWORD_BBDD):
    print("acceso concedido")
else:
    print("acceso denegado")    