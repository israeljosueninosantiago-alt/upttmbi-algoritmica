password = "Py3!2025"
def abc(a):
    v=["","","","","",""]

    if len(a)>=8:v[0]="✅"
    else: v[0]="❌"

    if any(char.isupper() for char in a)==True:v[1]="✅"
    else: v[1]="❌"

    if any(char.islower() for char in a)==True:v[2]="✅"
    else: v[2]="❌"

    if any(char.isdigit() for char in a)==True:v[3]="✅"
    else: v[3]="❌"

    if any(a.count(char) for char in "!@#$%^&*")==True:v[4]="✅"
    else: v[4]="❌"

    if v[0]=="✅" and v[1]=="✅" and v[2]=="✅" and v[3]=="✅" and v[4]=="✅":v[5]="CONTRASEÑA SEGURA"
    else:v[5]="CONTRASEÑA INSEGURA"

    return f"""=== VALIDADOR DE CONTRASEÑAS ===
Contraseña analizada: {a}

- Longitud mínima (8): {v[0]}
- Contiene mayúscula: {v[1]}
- Contiene minúscula: {v[2]}
- Contiene dígito: {v[3]}
- Contiene símbolo (!@#$%^&*): {v[4]}

Resultado final: {v[5]}"""

print(abc(password))