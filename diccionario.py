alumno_p =  {
    "nombre": "Dennis",
    "edad": 25,
    "ciudad": "Tiquisate",
    "educación": "Nivel medio",
    "estado civil": "Soltero",
    "email": "dennis.tiquisate@example.com",
    "idiomas": "español",
    "nacionalidad": "guatemalteco"
}

alumno_p["Universidad"] = "Universidad San Pablo"
alumno_p["edad"] = 26

for clave, valor in alumno_p.items():
    print(clave, "=>", valor)

if "email" in alumno_p:
    print("La clave 'email' existe.")
else:
    print("La clave 'email' no existe.")

telefono = alumno_p.get("teléfono")
print(telefono)








