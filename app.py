# coding=utf-8

import time
import os
import html

docHtml=html.Html()
# Dibuja las torres.
def dibujarTorres():
    global docHtml
    for x in range(len(torres)):
        if x == 0:
            espaciox=0
            espacioy=0
            espacioz=0
            for k in range(len(torres)):
                for j in range(len(torres[k])):
                    if j==0:
                        if torres[k][j]!=0:
                            espaciox=espaciox+1
                    elif j==1:
                        if torres[k][j]!=0:
                            espacioy=espacioy+1
                    elif j==2:
                        if torres[k][j]!=0:
                            espacioz=espacioz+1
            espacio = (7 * 20) - (len(torres[x]) * 20)
            docHtml.colx += """<div id="nube"></div>\n\t<div id="torres">\n\t<div id="t1" class="contenidoTorre">\n\t<div style='height:""" + str((7 * 20) - (espaciox * 20)) + """px'></div>\n"""
            docHtml.coly += """\n\t<div id="t2" class="contenidoTorre">\n\t<div style='height:""" + str((7 * 20) - (espacioy * 20)) + """px'></div>\n"""
            docHtml.colz += """\n\t<div id="t3" class="contenidoTorre">\n\t<div style='height:""" + str((7 * 20) - (espacioz * 20)) + """px'></div>\n"""
        for y in range(len(torres[x])):

            if y==0:
                if torres[x][y]!=0:
                    ancho=(torres[x][y]*20)+10
                    docHtml.colx+="""\t<div id='"""+str(x)+str(y)+"""' class='ficha' style='width:"""+str(ancho)+"""px'></div>\n"""
            elif y==1:
                if torres[x][y]!=0:
                    ancho=(torres[x][y]*20)+10
                    docHtml.coly+="""\t<div id='"""+str(x)+str(y)+"""' class='ficha' style='width:"""+str(ancho)+"""px'></div>\n"""
            elif y==2:
                if torres[x][y]!=0:
                    ancho=(torres[x][y]*20)+10
                    docHtml.colz+="""\t<div id='"""+str(x)+str(y)+"""' class='ficha' style='width:"""+str(ancho)+"""px'></div>\n"""
            if x==(len(torres)-1) and y==2:
                docHtml.colx+="""\t</div>"""
                docHtml.coly+="""\t</div>"""
                docHtml.colz+="""\t</div>\n\t</div><br><br>"""
                docHtml.contenido+=docHtml.colx+docHtml.coly+docHtml.colz
                docHtml.colx=""
                docHtml.coly=""
                docHtml.colz=""




# Nos devuelve el disco de arriba de la columna col, sino devuelve 0.


def buscarDiscoArriba(col):
    fila = 0
    while fila <= discos and torres[fila][col] == 0:
        fila += 1
    if fila <= discos:
        return torres[fila][col]
    else:
        return 0

# Nos devuelve el espacio vacio de arriba de la columna col.


def buscarEspacioArriba(col):
    fila = 0
    while fila <= discos and torres[fila][col] == 0:
        fila += 1
    return fila - 1

# Elimina el disco de arriba de la columna col.


def eliminarDiscoArriba(col):
    fila = 0
    while fila <= discos and torres[fila][col] == 0:
        fila += 1
    torres[fila][col] = 0

# Representación gráfica.


def hanoiGrafico(n,origen=1, auxiliar=2, destino=3):
    if n > 0:
        # n-1 discos de la torre origen a la torre auxiliar.
        hanoiGrafico(n-1,origen, destino, auxiliar)
        disco = buscarDiscoArriba(origen-1)
        eliminarDiscoArriba(origen-1)
        torres[buscarEspacioArriba(destino-1)][destino-1] = disco
        # print("*"*77)
        # print("\n"*5)
        # print("Se mueve el disco %d de torre %d a la torre %d" %(n, origen, destino))
        paso="Se mueve el disco "+str(n)+" de torre "+str(origen)+" a la torre "+str(destino)
        docHtml.contenido+="""\n\t<center><h3>"""+paso+"""</h3></center>"""
        dibujarTorres()
        # n-1 discos de la torre auxiliar a la torre final.
        hanoiGrafico(n-1,auxiliar, origen, destino)


os.system('cls')
print("     TORRES DE HANOI     ")
print("CURSO: Matematica para computación")
print("SECCION: N\n")
print("Nombre: Eddy Gerardo Paz Quex")
print("Carne: 201404346")
print("*"*25)

discos = int(input("\nIngrese entre 1 y 7 discos: "))
# Defino la matriz para el gráfico
if discos > 0 and discos < 8:
    if discos == 1:
        torres = [[0, 0, 0], [1, 0, 0]]
    elif discos == 2:
        torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0]]
    elif discos == 3:
        torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]]
    elif discos == 4:
        torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0]]
    elif discos == 5:
        torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0],[3, 0, 0], [4, 0, 0], [5, 0, 0]]
    elif discos == 6:
        torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0]]
    elif discos == 7:
        torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0],[4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0]]
    dibujarTorres()
    hanoiGrafico(discos)
    docHtml.generarHeader()
    docHtml.generarSolucion()
else:
    print("\nERROR! Solo se permiten de 1 a 7 discos para el modo grafico.")
