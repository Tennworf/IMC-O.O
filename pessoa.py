class Pessoa:
    def __init__(self, sexo, peso, altura):
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def condicao_imc(self):
        imc = self.calcular_imc()

        if self.sexo == 'feminino':
            if imc < 19.1:
                return "Abaixo do peso"
            elif 19.1 <= imc < 25.8:
                return "Peso normal"
            elif 25.8 <= imc < 27.3:
                return "Um pouco acima do peso"
            elif 27.3 <= imc < 32.3:
                return "Acima do peso ideal"
            else:
                return "Obeso"
        elif self.sexo == 'masculino':
            if imc < 20.7:
                return "Abaixo do peso"
            elif 20.7 <= imc < 26.4:
                return "Peso normal"
            elif 26.4 <= imc < 27.8:
                return "Um pouco acima do peso"
            elif 27.8 <= imc < 31.1:
                return "Acima do peso ideal"
            else:
                return "Obeso"
        return "Sexo inválido"
