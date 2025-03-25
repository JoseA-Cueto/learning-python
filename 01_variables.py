#variables
#Las Variables en python no se escriben en camelCase sino en snap_case
#Python es un lenguaje interpretado a diferencia de c# que es compilado

my_string_variable ="My String Variable"
print(my_string_variable)

my_int_variable=12
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)


#Concatenacion de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)

#Funciones del sistema para las variables
print(len(my_string_variable))# numero de caracteres

#variables en una sola linea ,(esto no es buena practica , solo es una curiosidad)
name,fullname,age,alias="Jose", "Cueto", 26,"VPK"
print("Mi nombre es:", name ,fullname,",mi edad es:",age,",mi alias es:",alias)


#Introducir datos
name_input= input("Cual es tu nombre: ")
age_input = input("Cual es tu edad: ")

print(name_input)
print(age_input)

"""
IMPORTANTE
 Existen varios tipos de tipados python es de tipado dinamico y fuerte (
 El tipo de una variable se determina en tiempo de ejecución y puede cambiar y
 No permite conversiones implícitas entre tipos incompatibles)"
 """
"type es una funcion que nos permite saber el tipo de dato de una variable ejemplo:"
print(type(5))
