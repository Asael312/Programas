biblioteca = [
{"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio":967, "genero": "Novela", "fecha_registro": (1, 3, 2023)},
{"titulo": "1984", "autor": "George Orwell", "anio": 1949, "genero":"Distopía", "fecha_registro": (12, 5, 2023)},
{"titulo": "1984", "autor": "George Orwell", "anio": 1949, "genero":"Distopía", "fecha_registro": (12, 5, 2023)},
{"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio":1605, "genero": "Novela", "fecha_registro": (20, 8, 2023)},
{"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943,"genero": "Fábula", "fecha_registro": (7, 6, 2023)},
{"titulo": "Crimen y castigo", "autor": "Fiódor Dostoievski", "anio": 1866,"genero": "Novela", "fecha_registro": (15, 4, 2023)},
{"titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963, "genero":"Novela", "fecha_registro": (22, 7, 2023)},
{"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "anio": 1953, "genero":"Ciencia ficción", "fecha_registro": (30, 9, 2023)},
{"titulo": "La Odisea", "autor": "Homero", "anio": -800, "genero": "Épica","fecha_registro": (11, 10, 2023)},
{"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "anio": 1955, "genero":"Novela", "fecha_registro": (3, 11, 2023)},
{"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "anio": 1813,"genero": "Romántica", "fecha_registro": (25, 12, 2023)},
{"titulo": "Drácula", "autor": "Bram Stoker", "anio": 1897, "genero": "Terror","fecha_registro": (5, 1, 2024)},
{"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "anio": 2001,"genero": "Novela", "fecha_registro": (14, 2, 2024)}
]
def normalizar(texto):
    """Devuelve un texto normalizado (minúsculas y sin espacios extremos)."""
    return texto.strip().lower()
def eliminar_libro(biblioteca):
    """Elimina un libro por título; si no existe, lanza LibroNoEncontradoError."""
    if not biblioteca:
        print('La biblioteca esta')
        return    
    nombre = normalizar(input('¿Qué libro buscas?: '))
    for i in range(len(biblioteca)):
        for libro in biblioteca:
            if nombre == normalizar(libro['titulo']):
                del biblioteca[i]
                print('Libro eliminado con exito')
                return
    print('No se encontro el libro')

if __name__=="__main__":
    eliminar_libro(biblioteca)