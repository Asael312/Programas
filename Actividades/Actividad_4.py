# Actividad IV – Gestor de Biblioteca Digital (ESQUELETO)
# Instrucciones resumidas:
# - Usa listas, diccionarios y tuplas.
# - Implementa funciones para registrar, consultar, buscar, eliminar y estadísticas.
# - Maneja excepciones.
# - Menú con opciones 1-6.
#
# NOTA: Este archivo es un esqueleto para que el alumno complete.
# Sólo se usan temas hasta el Tema 16 (entradas/salidas, condicionales, ciclos,
# funciones, strings, listas, tuplas, diccionarios y excepciones).


# ===== Datos =====
# Lista que contendrá diccionarios de libros
biblioteca = []  # cada libro: {"titulo": str, "autor": str, "anio": int, "genero": str, "fecha_registro": (d, m, a)}


# ===== Utilidades =====
def normalizar(texto):
    """Devuelve un texto normalizado (minúsculas y sin espacios extremos)."""
    return texto.strip().lower()


# ===== Funciones principales =====        
def registrar_libro(biblioteca):
    """Captura datos del libro y lo agrega a la lista 'biblioteca'."""
    try:
        titulo = normalizar(input('Ingrese el nombre del libro: '))
        autor = normalizar(input('Ingrese el autor del libro: '))
        anio = int(input('Año de publicación: '))
        genero = normalizar(input('Género del libro: '))
        d = int(input('Día de registro: '))
        m = int(input('Mes de registro: '))
        a = int(input('Año de registro: '))
        if not titulo or not autor or not genero:
            print("Título, autor y género no pueden estar vacíos.")
            return
        for libro in biblioteca:
            if normalizar(libro["titulo"]) == titulo and normalizar(libro["autor"]) == autor:
                print("El libro ya existe en la biblioteca.")
                return
        libro = {"titulo": titulo,"autor": autor,"anio": anio,"genero": genero,"fecha_registro": (d, m, a)}
        biblioteca.append(libro)
        print("Libro agregado exitosamente.")
    except ValueError:
        print("Entrada inválida: asegúrate de ingresar números donde corresponde.")

def consultar_libros(biblioteca):
    """Muestra todos los libros registrados en forma de tabla simple."""
    if not biblioteca:
        print('La biblioteca esta vacía')
        return    
    print("{:<30} {:<25} {:<6} {:<20} {:<15}".format('Titulo','Autor','Año', 'Genero', 'Fecha de registro'))
    for libros in biblioteca:
        d, m, a = libros['fecha_registro']
        fecha = f"{d:02d}/{m:02d}/{a}"
        print("{:<30} {:<25} {:<6} {:<20} {:<15}".format(libros['titulo'],libros['autor'],libros['anio'],libros['genero'],fecha))

def buscar_libro(biblioteca):
    """Busca un libro por título y muestra sus datos si existe."""
    if not biblioteca:
        print('La biblioteca esta vacía')
        return    
    nombre = normalizar(input('¿Qué título de libro buscas?: '))
    for libro in biblioteca:
        if nombre == normalizar(libro['titulo']):
            d, m, a = libro['fecha_registro']
            fecha = f"{d:02d}/{m:02d}/{a}"
            print(f"Titulo: {libro['titulo']:<25}\nAutor: {libro['autor']:<24}\nAño: {libro['anio']:<4}\nGenero: {libro['genero']:<10}\nFecha de registro: {fecha:>10}")
            return
    print('No se encontro ningun libro con ese titulo')

def eliminar_libro(biblioteca):
    """Elimina un libro por título; si no existe, muestra mensaje."""
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    nombre = normalizar(input("¿Qué libro deseas eliminar?: "))
    for libro in biblioteca:
        if nombre == normalizar(libro["titulo"]):
            biblioteca.remove(libro)
            print("Libro eliminado con éxito.")
            return
    print("No se encontró el libro.")

def estadisticas(biblioteca):
    """Muestra total de libros, autor con más publicaciones y género más frecuente"""
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    print(f"El número total de libros en la biblioteca es de {len(biblioteca)}")
    autores = [libro['autor'] for libro in biblioteca]
    generos = [libro['genero'] for libro in biblioteca]
    autor_max = max(autores, key=autores.count)
    cantidad_autor = autores.count(autor_max)
    genero_max = max(generos, key=generos.count)
    cantidad_genero = generos.count(genero_max)
    print(f"Autor con más publicaciones: {autor_max} ({cantidad_autor} libros)")
    print(f"Género más frecuente: {genero_max} ({cantidad_genero} libros)")
    



# ===== Menú principal =====
def mostrar_menu():
    print("\n=== GESTOR DE BIBLIOTECA DIGITAL ===")
    print("1. Registrar libro")
    print("2. Consultar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Ver estadísticas")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        try:
            if opcion == "1":
                registrar_libro(biblioteca)
            elif opcion == "2":
                consultar_libros(biblioteca)
            elif opcion == "3":
                buscar_libro(biblioteca)
            elif opcion == "4":
                eliminar_libro(biblioteca)
            elif opcion == "5":
                estadisticas(biblioteca)
            elif opcion == "6":
                print("Saliendo... ¡Gracias por usar el sistema!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida:") # Esto Tambien
        except Exception:
            print("Ha ocurrido un error no esperado:") # cambialo Asa


if __name__ == "__main__":
    main()
