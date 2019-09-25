#leer texto e imprimirlo separado por coma
try:
	nombre='lorem.txt'
	archivo=open(nombre)
	for linea in archivo:
		lista=linea.split()
		print(lista)
	archivo.close()
except FileNotFoundError:
	print("archivo no existe")


#SACAR COMA DE TEXTO
# try:
# 	nombre='lorem.txt'
# 	archivo=open(nombre)
# 	contenido=archivo.read()
# 	lista=contenido.split("")
# 	print(lista)
# 	archivo.close()
# except FileNotFoundError:
# 	print("archivo no existe")