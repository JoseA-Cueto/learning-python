### Strings ###

#Formateo
my_string_var = "Un String"

name, surname, age = "Jose", "Cueto", 26
print("Mi nombre es %s %s y mi edad es %s".format(name,surname,age)) #ERROR:Forma incorrecta

print("Mi nombre es %s %s y mi edad es %s"%(name,surname,age)) #INFO: Forma correcta
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age)) #INFO: Forma correcta


# Formas de hacer comentarios bien estructurados extension better Comments

# TODO: Implementar la validación de entrada
# WARNING: Posible error si input es nulo
# ERROR: No usar en producción
# INFO: Devuelve un objeto con los datos del usuario


#Inferencia de datos 
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #INFO: Forma correcta


#Desempaquetado de caracteres 