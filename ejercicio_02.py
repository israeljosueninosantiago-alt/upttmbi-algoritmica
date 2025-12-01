a = "URGENTE: Reunión URGENTE mañana. Llevar informe urgente. spam publicidad virus"
b = ["spam", "publicidad", "virus"]
def abc(a,b):
    q=a
    q=q.lower()
    l=q.split()
    k=0
    j=0
    t=""
    for u in b:
        k+=q.count(u)
    j=q.count("urgente")
    if k>0:
        k="Si"
    else:
        k="No"
    if j>0:
        t="Si"
    else:
        t="No"
    return f"""=== ANALIZADOR ===
Mensaje original: {a}
Palabras prohibidas detectadas: {k}
Conteo 'urgente': {j}
Requiere atención inmediata: {t}"""
print(abc(a,b))