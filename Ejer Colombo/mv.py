# Mover contenido de archivo a otro archivo 

import os
lorem=open("loremborrar.txt")
lorem2=open("lorem2.txt","w")
lineas=lorem.read()
lorem2.write(lineas)
lorem.close()
os.remove("loremborrar.txt")
