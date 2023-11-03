import unittest

from tetris.model.implementacion import Tetromino


class TestTetromino(unittest.TestCase):
    def test_igualdad_rotacion_actual(self):
        t1 = Tetromino([
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.']])
        t2 = Tetromino([
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.']])
        self.assertTrue(t1.igual(t2))

    def test_semejanza_en_alguna_rotacion(self):
        t1 = Tetromino([
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.']])
        t2 = Tetromino([
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.']])
        self.assertTrue(t1.semejante(t2))

    def test_rotar(self, t2=None):
        t1 = Tetromino([
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.']])
        t1.rotar()
        # Verificar que la rotación cambió la forma
        self.assertFalse(t1.igual(t2))

if name == 'main':
    unittest.main()