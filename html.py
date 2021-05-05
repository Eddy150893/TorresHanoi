import webbrowser
import os


class Html:

    def __init__(self):
        self.html=""
        self.head=""
        self.contenido=""
        self.colx=""
        self.coly=""
        self.colz=""

    def generarHeader(self):
        self.head="""<head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <LINK href="estilosHanoi.css" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Quicksand:700" rel="stylesheet"> 
        <title>Torres de Hanoi</title>
        </head>"""


    def generarSolucion(self):
        self.generarHeader()
        self.html="""<!DOCTYPE html>
        <html lang="en">"""
        self.html+=self.head
        self.html+="""<body>
        <h1>Torres de Hanoi</h1>
        <div class="contenido">"""
        self.html+=self.contenido
        self.html+="""
        </div>   
        </body>
        </html>"""
        f = open(os.getcwd()+'\\solucion.html', 'w', encoding='utf8')
        f.write(self.html)
        f.close()
        webbrowser.open_new_tab(os.getcwd()+'\\solucion.html')