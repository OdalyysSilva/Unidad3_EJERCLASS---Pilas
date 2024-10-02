class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        """Agrega un elemento a la pila."""
        self.elementos.append(elemento) #meter datos a la pila
        print(f"Elemento apilado: {elemento}")

    def desapilar(self):
        """Elimina y devuelve el elemento en la parte superior de la pila."""
        if self.esta_vacia():
            print("Error: La pila está vacía.")
            return None
        elemento = self.elementos.pop() # sacar datos de la pila
        print(f"Elemento desapilado: {elemento}")
        return elemento

    def peek(self):
        """Devuelve el elemento en la parte superior de la pila sin quitarlo."""
        if self.esta_vacia():
            print("Error: La pila está vacía.")
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        """Devuelve True si la pila está vacía, False en caso contrario."""
        return len(self.elementos) == 0

    def tamaño(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.elementos)

# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila()

    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    print(f"Elemento en la parte superior: {pila.peek()}")
    print(f"Tamaño de la pila: {pila.tamaño()}")

    pila.desapilar()
    print(f"Elemento en la parte superior: {pila.peek()}")
    print(f"Tamaño de la pila: {pila.tamaño()}")

    pila.desapilar()
    pila.desapilar()
    pila.desapilar()  # Intentar desapilar de una pila vacía
