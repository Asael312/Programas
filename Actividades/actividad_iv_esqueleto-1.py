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
    """Devuelve un texto normalizado para evitar duplicados (sin espacios extremos y en minúsculas)."""
    # TODO: implementar
    return texto


# ===== Funciones principales =====
def registrar_libro():
    """Captura datos del libro y lo agrega a la lista 'biblioteca'."""
    # TODO: implementar registro con validaciones e inserción en la lista
    pass


def consultar_libros():
    """Muestra todos los libros registrados en forma de tabla simple."""
    # TODO: implementar
    pass


def buscar_libro():
    """Busca un libro por título y muestra sus datos si existe; si no, lanza LibroNoEncontradoError."""
    # TODO: implementar
    pass


def eliminar_libro():
    """Elimina un libro por título; si no existe, lanza LibroNoEncontradoError."""
    # TODO: implementar
    pass


def estadisticas():
    """Muestra total de libros, autor con más publicaciones y género más frecuente."""
    # TODO: implementar
    pass


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
                registrar_libro()
            elif opcion == "2":
                consultar_libros()
            elif opcion == "3":
                buscar_libro()
            elif opcion == "4":
                eliminar_libro()
            elif opcion == "5":
                estadisticas()
            elif opcion == "6":
                print("Saliendo... ¡Gracias por usar el sistema!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except LibroNoEncontradoError as e:
            print("Error:", e)
        except ValueError as e:
            print("Entrada inválida:", e)
        except Exception as e:
            print("Ha ocurrido un error no esperado:", e)


if __name__ == "__main__":
    main()
