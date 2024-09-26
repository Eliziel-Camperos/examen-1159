class Comics:
    def __init__(self):
        # Usamos un diccionario para almacenar los datos del cómic
        self.datos = {
            "ID": "",
            "Serie": "",
            "Género": "",
            "Cómics Vendidos": 0,
            "Autor": "",
            "Color": "",
            "Precio": 0.0
        }

    def mostrar_datos(self):
        for key, value in self.datos.items():  #diccionario
            print(f"{key}: {value}")

    def set_datos(self, id_comic, serie, genero, cven, autor, color, precio):
        self.datos["ID"] = id_comic
        self.datos["Serie"] = serie
        self.datos["Género"] = genero
        self.datos["Cómics Vendidos"] = cven
        self.datos["Autor"] = autor
        self.datos["Color"] = color
        self.datos["Precio"] = precio

    def lista_ID(self):
        return ["454", "742", "735", "777", "222", "9999", "043"]

    def lista_series(self):
        return ["Spiderman", "Iron Man", "X-Men", "Chaos + Order", "Jujutsu Kaizen", "One Piece", "Deadpool"]

    def lista_generos(self):
        return [
            "Acción, superheroes, Ciencia Ficción, Fantasía",
            "Acción, superheroes, Ciencia Ficción, Fantasía, Drama",
            "Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama",
            "Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama, horror",
            "Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama, aventura",
            "Acción, Superhéroes, Ciencia ficción, Comedia"
        ]
    
    def lista_cven(self):
        return [1000, 900, 800, 750, 650, 1200, 1100]
    
    def lista_autores(self):
        return ["Stan Lee, Steve Ditko", "Stan Lee, Jack Kirby, Larry Lieber, Don Heck", "Stan lee", "Elicrafting","GeGe Akutami", "Eiichiro Oda", "Rob Liefeld, Fabian Nicieza"]
    
    def lista_colores(self):
        return ["Color", "Color", "Color", "Color", "Blanco y negro", "Blanco y negro", "Color"]
    
    def lista_precios(self):
        return [4.99, 8.99, 36.99, 4.99, 7.99, 7.99, 10.99]


# Crear un objeto
comic_obj = Comics()
comic_obj.set_datos("454", "Spiderman", "Acción", 1000, "Stan Lee", "Color", 10.99)

# Mostrar los datos del cómic
comic_obj.mostrar_datos()
print("Lista de IDs:           ", comic_obj.lista_ID())
print("Lista de series:        ", comic_obj.lista_series())
print("Lista de géneros:       ", comic_obj.lista_generos())
print("Lista de cómics vendidos:", comic_obj.lista_cven())
print("Lista de autores:       ", comic_obj.lista_autores())
print("Lista de colores:       ", comic_obj.lista_colores())
print("Lista de precios:       ", comic_obj.lista_precios())
