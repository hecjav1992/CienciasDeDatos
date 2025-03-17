Estudiantes = [{"Nombre":"Anthony", "Nota":3.5},
               {"Nombre":"Moises", "Nota":2.5},
               {"Nombre":"Pepe", "Nota":4.5}]

for x in Estudiantes:
    if x["Nota"]< 3.0:
        
        print("se quedo",x["Nombre"])
        Estudiantes.remove(x)

print(f"estudiantes que aprobaron {Estudiantes}")

vocales = ["a","e","i","o","U"]




