a = "  aNa carLos  bravo  "
b = "  ab-1234-cd  "
def abc(a,b):
    print(f"""=== NORMALIZADOR DE IDENTIDAD ===
Nombre original: '{a}'
Documento original: '{b}' 
""")
    a=a.lower()
    e=a
    a=""
    ii=0
    for i in e:
        if ii==0:a+=i.upper()
        elif e[ii-1]==" ":a+=i.upper()
        else:a+=i
        ii+=1
    b=b.upper()
    a=a.replace("-","")
    b=b.replace("-","")
    l=a.split()
    a=" ".join(l)
    print(f"""Nombre limpio: {a}
Documento limpio: {b}""")
    a=a.upper()
    a=a.strip()
    b=b.strip()
    return f"{a} - DOC: {b}"
print(abc(a,b))