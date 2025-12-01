fila = '  "Carlos Bravo", 27, "Guadalajara, MX", Desarrollador '
columnas = ["nombre", "edad", "ciudad", "ocupacion"]
def abc(a,b):

    c=a
    c=c.strip()
    c=c.replace(",","")
    c=c.split('"')
    for i in c:
        if i == "":
            c.remove(i)
    
    d={}
    for i in range((len(c)-1)):
        d[b[i]]=c[i]

    return f"""=== PARSER CSV ===
Fila original:   "Carlos Bravo", 27, "Guadalajara, MX", Desarrollador 

Resultado:{d}
"""
print(abc(fila,columnas))