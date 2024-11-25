import unittest
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    def test_imc_mulher_abaixo_do_peso(self):
        pessoa = Pessoa('feminino', 50, 1.70)  
        self.assertEqual(pessoa.condicao_imc(), "Abaixo do peso")
    
    def test_imc_mulher_peso_normal(self):
        pessoa = Pessoa('feminino', 60, 1.70)  
        self.assertEqual(pessoa.condicao_imc(), "Peso normal")
    
    def test_imc_mulher_um_pouco_acima_do_peso(self):
        pessoa = Pessoa('feminino', 75, 1.70)  
        self.assertEqual(pessoa.condicao_imc(), "Um pouco acima do peso")
    
    def test_imc_mulher_acima_do_peso_ideal(self):
        pessoa = Pessoa('feminino', 80, 1.70)  
        self.assertEqual(pessoa.condicao_imc(), "Acima do peso ideal")
    
    def test_imc_mulher_obeso(self):
        pessoa = Pessoa('feminino', 95, 1.70)  
        self.assertEqual(pessoa.condicao_imc(), "Obeso")

    def test_imc_homem_abaixo_do_peso(self):
        pessoa = Pessoa('masculino', 60, 1.80)  
        self.assertEqual(pessoa.condicao_imc(), "Abaixo do peso")
    
    def test_imc_homem_peso_normal(self):
        pessoa = Pessoa('masculino', 75, 1.80)  
        self.assertEqual(pessoa.condicao_imc(), "Peso normal")

    def test_imc_homem_um_pouco_acima(self):
        pessoa = Pessoa('masculino', 87, 1.80)  
        self.assertEqual(pessoa.condicao_imc(), "Um pouco acima do peso")

    def test_imc_homem_acima_do_peso_ideal(self):
        pessoa = Pessoa('masculino', 95, 1.80)  
        self.assertEqual(pessoa.condicao_imc(), "Acima do peso ideal")
    
    def test_imc_homem_obeso(self):
        pessoa = Pessoa('masculino', 105, 1.80)  
        self.assertEqual(pessoa.condicao_imc(), "Obeso")

if __name__ == '__main__':
    unittest.main()
