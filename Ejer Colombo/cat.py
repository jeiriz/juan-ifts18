try:
	nombre='lorem.txt'
	archivo=open(nombre,'r')
	contenido=archivo.read()
	print(contenido)
	archivo.close()
except FileNotFoundError:
	print("archivo no existe")