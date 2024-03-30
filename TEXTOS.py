with open('my_notes.txt', 'w') as file:
    file.write('Primera nota personal\n')
    file.write('Segunda nota personal\n')
    file.write('Tercera nota personal\n')

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# El archivo se cierra automáticamente cuando sales del bloque 'with'