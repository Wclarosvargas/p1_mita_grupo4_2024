archivo=open("cursos.txt","r",encoding="UTF-8")
for linea in archivo:
    print(linea)
archivo.close()