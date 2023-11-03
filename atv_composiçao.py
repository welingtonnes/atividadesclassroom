class Cabeca:
    def __init__(self):
        self.estado = "Intacta"

    def destruir(self):
        self.estado = "Destruída"
        print("A cabeça foi destruída!")

class Boneco:
    def __init__(self):
        self.cabeca = Cabeca()

    def destruir(self):
        self.cabeca.destruir()
        print("O boneco foi destruído!")

if __name__ == "__main__":
    boneco = Boneco()
    boneco.destruir()