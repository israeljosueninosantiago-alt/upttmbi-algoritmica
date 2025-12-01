frase = "Anita lava la tina"

def abc(a):

    b=a
    b=b.lower()
    b=b.replace(" ","")

    w=""
    for i in range(len(b)):
        if b[i]==b[-(i+1)]:
            w="Si"
        else:
            w="No"
        if w=="No":
            break
    return f"""=== DETECTOR DE PALÍNDROMOS ===
Frase original: {a}
Frase limpia: {b}
¿Es palíndromo?: {w}"""

print(abc(frase))