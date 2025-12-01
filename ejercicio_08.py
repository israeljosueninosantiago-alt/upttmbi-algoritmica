mensaje = "Hola Mundo 2025!"
desplazamiento = 3

def cifrar(a,b,c,d):
    a=d.split(" ")
    for i in a:
        for ii in i:
            e=ord(ii)+c
            e=chr(e)
            b+=e
        b+=" "
    return b

def descifrar(a,b,c,d):
    a=d.split(" ")
    for i in a:
        for ii in i:
            e=ord(ii)-c
            e=chr(e)
            b+=e
        b+=" "
    return b

def abc(a,b):
    c=""
    d=[]
    c=cifrar(d,c,b,a)
    e=""
    f=[]
    e=descifrar(f,e,b,c)

    print(e)

    return f"""=== CIFRADO CÉSAR ===
Mensaje original: {a}
Desplazamiento: {b}

Mensaje cifrado: {c}
Mensaje descifrado: {e}"""
print(abc(mensaje,desplazamiento))