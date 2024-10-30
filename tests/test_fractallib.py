import unittest
import numpy as np
import os
import matplotlib.pyplot as plt
from fractallib import (
    fractal,
    fractal_matrix,
    mandelbrot_matrix,
    is_in_julia,
    is_in_mandelbrot,
    julia_matrix,
    get_image,
)

class TestFractalLib(unittest.TestCase):

    def test_fractal(self):
        self.assertEqual(fractal(0, 0), 20,"should be in the fractal")
        self.assertEqual(fractal(0, 0, n=50), 50,"should be in the fractal")
        self.assertNotEqual(fractal(0, 1 + 1j, n=50), 50,"should diverge")

    def test_fractal_matrix(self):
        result = fractal_matrix(0,0)
        self.assertIsInstance(result,np.ndarray,"type should be ndarray")
        self.assertEqual(result.shape,(200,200),"resolution 200*200")

    def test_mandelbrot_matrix(self):
        result = mandelbrot_matrix(0)
        self.assertIsInstance(result,np.ndarray,"type should be ndarray")
        self.assertEqual(result.shape,(200,200),"resolution 200*200")

    def test_julia_matrix(self):
        result = julia_matrix(0)
        self.assertIsInstance(result,np.ndarray,"type should be ndarray")
        self.assertEqual(result.shape,(200,200),"resolution 200*200")

    def test_is_in_julia(self):
        self.assertTrue(is_in_julia(z=0,c=0), "should be inside")
        self.assertFalse(is_in_julia(z=3,c=0), "should be outside")

    def test_is_in_mandelbrot(self):
        self.assertTrue(is_in_mandelbrot(z=0,c=0),"should be inside")
        self.assertFalse(is_in_mandelbrot(z=10,c=0),"shoud be outside")

    def test_get_image(self):
        path = 'test.png'
        get_image(path=path,n=10,resolution=200)
        
        self.assertTrue(os.path.exists(path), "checking for image file creation")
        self.assertEqual(plt.imread(path).shape[:2],(200, 200),"cheching for dimensions, should be 200*200")
        os.remove(path) #clean up
        


if __name__ == "__main__":
    unittest.main()
