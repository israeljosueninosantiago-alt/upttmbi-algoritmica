ventas = [
    ("Teclado", 12, 25.5),
    ("Mouse", 20, 15.0),
    ("Monitor", 5, 210.99),
]
def abc(a):
    b=[a[0][1],a[0][2],a[0][1]*a[0][2],a[1][1],a[1][2],a[1][1]*a[1][2],a[2][1],a[2][2],a[2][1]*a[2][2],a[0][1]*a[0][2]+a[1][1]*a[1][2]+a[2][1]*a[2][2]]
    return f"""=========== REPORTE DE VENTAS ===========
Producto           Unidades   P.Unit    Total
----------------------------------------------
Teclado            {b[0]}         {b[1]}      {b[2]}
Mouse              {b[3]}         {b[4]}      {b[5]}
Monitor            {b[6]}          {b[7]}    {b[8]}
----------------------------------------------
TOTAL GENERAL                           {b[9]}"""
print(abc(ventas))