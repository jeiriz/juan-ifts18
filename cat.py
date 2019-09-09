try:
	nombre='lorem.txt'
	archivo=open(nombre,'r')
	contenido=archivo.read()
	print(contenido)
	archivo.close()
except:
	print("archivo no existe")
