# Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo 
# (sea de texto o binario) a otro, de modo que quede exactamente igual.
#copiar contenido de lorem.txt a loremcopy.txt

lorem = open("lorem.txt") #si no se aclara se abre modo lectura
loremcopy=open("loremcopy.txt","w")
linea=lorem.read()
loremcopy.write(linea)
lorem.close()
loremcopy.close()
