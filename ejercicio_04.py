titulo_raw = "  ¡Lanzamiento: Python 3.12 y más allá!  "
def abc(a):
    b=a.lower()
    b=b.strip()
    b=b.replace(" ","-")
    b=b.replace(".","-")
    b=b.replace("¡","")
    b=b.replace("!","")
    b=b.replace(":","-")
    b=b.replace("á","a")
    b=b.replace("é","e")
    b=b.replace("í","i")
    b=b.replace("ó","o")
    b=b.replace("ú","u")
    b=b.replace("--","-")
    print(f"""=== GENERADOR DE SLUG ===
Título original: {a}
Slug: {b}""")
abc(titulo_raw)