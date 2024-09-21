from collections import default, deque

class GrafoDAG:
     def __init__(self, vertices):
         self.grafo = defaultdict(list)
         self.vertices = vertices
         self.costos = {}
 
     # Medtodo para añadir una arista
     def añadir_arista(self, u ,v ,costo
         self.grafo[u].append(v)
         self.costos[(u,v)] = costo
    
     #funcion para encontrar el vertice con mas caminos alcanzables
     def vertice_mas_alcanzable(self, fuente):
         caminos = defaultdict(list)

         def dfs(v, camino, costo, visitados):
             if v in visitados
                 return
             visitados.add(v)
             camino.append(v)
             caminos[v].append((list(camino), costo))
             for vecino in self.grafo[v]:
                 dfs(vecino, camino, costo + self.costos[(v, vecino)], visitados)
             camino.pop()
             visitados.remove(v)
          # llamamos a la funcion dfs desde el vertice fuente
          dfs(fuente, camino[], costo:0, set())
          #Encontrar al vertice mas alcanzable basado en el numero de caminos
          mas_alcanzable = max(caminos, key=lambda k: len(caminos[k]))
          print(f"vertice mas alcanzable: {mas_alcanzable}")
         
           Ordenamos los caminos hacia el vértice alcanzable por costo en orden descendente
        caminos_ordenados = sorted(caminos[mas_alcanzable], key=lambda x: x[1], reverse=True)
        print(f"Caminos hacia el vértice {mas_alcanzable} ordenados por costo descendente:")
        for camino, costo in caminos_ordenados:
            print(f"Camino: {camino} con costo: {costo}")

        return mas_alcanzable, caminos_ordenados

    # Insertar un nuevo vértice V' cumpliendo las condiciones
    def insertar_vertice(self, fuente, mas_alcanzable):
        nuevo_vertice = self.vertices
        self.vertices += 1

        # Añadimos una nueva arista desde la fuente hacia el nuevo vértice
        self.añadir_arista(fuente, nuevo_vertice, 1)  # Definimos un costo arbitrario para esta nueva arista

        # Conectamos el nuevo vértice con los vecinos de la fuente excepto el más alcanzable
        for vecino in self.grafo[fuente]:
            if vecino != mas_alcanzable:
                self.añadir_arista(nuevo_vertice, vecino, self.costos[(fuente, vecino)])

        # Revisamos si algún vecino del nuevo vértice comparte aristas con el vértice más alcanzable
        vecinos = set(self.grafo[mas_alcanzable])
        for vecino in self.grafo[nuevo_vertice]:
            if vecino in vecinos:
                print(
                    f"Error: No se puede insertar el nuevo vértice {nuevo_vertice} porque comparte un vecino ({vecino}) con el vértice {mas_alcanzable}.")
                return None

        print(f"Nuevo vértice {nuevo_vertice} insertado exitosamente.")
        return nuevo_vertice


# Función principal de ejecución
def main():
    # Definimos las aristas del grafo con sus respectivos costos
    aristas = [
        (0, 1, 2), (0, 2, 4), (0, 4, -2), (0, 5, 1), (0, 6, 5),
        (2, 3, 3), (2, 4, 2), (3, 8, -4), (4, 3, 5), (4, 8, 1),
        (4, 7, 2), (5, 7, -1), (5, 8, -3), (6, 7, 6), (7, 8, 2)
    ]

    # Creamos un grafo con 9 vértices (de 0 a 8)
    g = GrafoDAG(9)

    # Añadimos las aristas al grafo
    for u, v, costo in aristas:
        g.añadir_arista(u, v, costo)

    # Paso 1: Encontrar el vértice más alcanzable desde el vértice 0
    mas_alcanzable, caminos_ordenados = g.vertice_mas_alcanzable(0)

    # Paso 2: Insertar un nuevo vértice cumpliendo las condiciones
    nuevo_vertice = g.insertar_vertice(0, mas_alcanzable)

    # Paso 3: Si se ha insertado el nuevo vértice, mostrarlo en el formato de entrada
    if nuevo_vertice is not None:
        print(f"Nuevo vértice insertado: {nuevo_vertice}")
        for (u, v), costo in g.costos.items():
            print(f"{{{u}, {v}, {costo}}}")


if _name_ == "_main_":
    main()
input("Presiona Enter para salir...")
