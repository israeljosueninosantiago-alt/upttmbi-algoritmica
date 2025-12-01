texto = "banana bandana"
clave = "ana"
def abc(a,b):
    l=[]
    i=0
    while a.find(b,i) != -1:
        l.append(a.find(b,i+1))
        i+=a.find(b,i+1)
    return f"""=== BUSCADOR DE COINCIDENCIAS ===
Texto: {a}
Clave: {b}

Coincidencias encontradas: {len(l)}
Índices: {l}"""

print(abc(texto,clave))