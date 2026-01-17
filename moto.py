class Moto:
    def __init__(self, marca, referencia, cilindrada, precio, color):
        # Atributos (Lo que la moto ES)
        self.marca = marca
        self.referencia = referencia
        self.cilindrada = cilindrada
        self.precio = precio
        self.color = color
        self.encendida = False

    # Métodos (Lo que la moto HACE)
    def encender(self):
        if not self.encendida:
            self.encendida = True
            print(f"La {self.marca} {self.referencia} ha rugido. ¡Lista para rodar!")
        else:
            print("La moto ya está encendida.")

    def mostrar_info(self):
        return f"Moto: {self.marca} {self.referencia} | {self.cilindrada}cc | Precio: ${self.precio}"
          
