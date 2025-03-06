import unittest  # Importa o módulo unittest para criar e executar testes

def soma(a, b):
    return a + b  # Função que retorna a soma de dois números

class TestMathOperations(unittest.TestCase):
    # Classe de teste que herda de unittest.TestCase

    def test_soma_positivos(self):
        # Testa se a soma de 1 e 1 é igual a 2
        self.assertEqual(soma(1, 1), 2)
    
    def test_soma_negativos(self):
        # Testa se a soma de -1 e -1 é igual a -2
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_positivo_negativo(self):
        # Testa se a soma de 1 e -1 é igual a 0
        self.assertEqual(soma(1, -1), 0)

if __name__ == '__main__':
    unittest.main()  # Executa os testes quando o script é executado diretamente