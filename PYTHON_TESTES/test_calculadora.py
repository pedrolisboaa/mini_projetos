import unittest
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retonar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_10_e_10_deve_retornar_20(self):
        self.assertEqual(soma(10, 10), 20)
    def test_soma_varias_entradas(self):
        x_y_saida = (
            (10, 10, 20),
            (100, 100, 200),
            (15, 10, 25),
            (15, 100, 115),
        )

        for x_y_saida in x_y_saida:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)
    def test_soma_x_nao_e_int_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 1)
    def test_soma_y_nao_e_int_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(11, 'p')


unittest.main(verbosity=2)
