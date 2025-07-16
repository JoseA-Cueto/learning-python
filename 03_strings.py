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
lenguaje ="python"
a,b,c,d,e,f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division
#Info:Esto funciona = que un array , al final un string es un array d caracteres , asi q comienza en la posicion 0
lenaguaje_slice =lenguaje[1:3]
print(lenaguaje_slice)

#WARNING: al no existir el -0 , el final empezaria en -1
reversed_lenguaje = lenguaje[::-1]
print(reversed_lenguaje)

#ERROR: Funciones del sistema con string
print(lenguaje.capitalize() ) # warning: Pone Mayusculas  al inicio

print(lenguaje.upper() )  # warning:Pone todo en mayus

print(lenguaje.count("p") )  # warning: Cuentas las P

print(lenguaje.lower() ) # warning: Todo a minuscula

print(lenguaje.startswith("py") ) # warning: booleano para ver con que empieza
