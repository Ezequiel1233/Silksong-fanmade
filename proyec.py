import random
caracteres="=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789090 "  
numero = int(input("introduzca la longitud de la contraseña"))
contraseña = ""
for i in range(numero):
    contraseña+= random.choice(caracteres)
print(contraseña)
