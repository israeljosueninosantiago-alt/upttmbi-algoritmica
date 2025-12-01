poema = "Aún canta el ave y el viento sopla suave"
def abc(a):
    b=a.lower()
    return f"""Texto: {a}
    
Vocales sin tilde:
- a: {b.count("a")}
- e: {b.count("e")}
- i: {b.count("i")}
- o: {b.count("o")}
- u: {b.count("u")}

Vocales con tilde: {sum(b.count(v) for v in "áéíóú")}
Total de vocales: {sum(b.count(v) for v in "aeiouáéíóú")}"""

print(abc(poema))