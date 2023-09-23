# -*- coding: utf-8 -*-
"""
Updated March 15, 2023
The primary goal of this file is to test the classifyTriangle() function in Triangle.py

"""

import unittest
from Triangle import classifyTheTriangle

class TestTriangles(unittest.TestCase):

    def test_equilateral_triangle(self): 
        self.assertEqual(classifyTheTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')
        
    def test_isosceles_triangle(self):
        self.assertEqual(classifyTheTriangle(5,5,3),'Isosceles','5,5,3 should be isosceles')
        self.assertEqual(classifyTheTriangle(7,3,7),'Isosceles','7,3,7 should be isosceles')
        self.assertEqual(classifyTheTriangle(3,7,7),'Isosceles','3,7,7 should be isosceles')
        
    def test_scalene_triangle(self):
        self.assertEqual(classifyTheTriangle(6,7,8),'Scalene','6,7,8 should be scalene')
        self.assertEqual(classifyTheTriangle(8,6,7),'Scalene','8,6,7 should be scalene')
        self.assertEqual(classifyTheTriangle(7,8,6),'Scalene','7,8,6 should be scalene')
        
    def test_right_triangle(self):
        self.assertEqual(classifyTheTriangle(3,4,5),'Right','3,4,5 should be right')
        self.assertEqual(classifyTheTriangle(5,3,4),'Right','5,3,4 should be right')
        self.assertEqual(classifyTheTriangle(6,8,10),'Right','6,8,10 should be right')
        
    def test_not_a_triangle(self):
        self.assertEqual(classifyTheTriangle(3,4,7),'NotATriangle','3,4,7 should not be a triangle')
        self.assertEqual(classifyTheTriangle(2,2,5),'NotATriangle','2,2,5 should not be a triangle')
        self.assertEqual(classifyTheTriangle(8,2,1),'NotATriangle','8,2,1 should not be a triangle')
        
    def test_invalid_input(self):
        self.assertEqual(classifyTheTriangle(201,3,4),'InvalidInput','201,3,4 is invalid input')
        self.assertEqual(classifyTheTriangle(0,3,4),'InvalidInput','0,3,4 is invalid input')
        self.assertEqual(classifyTheTriangle(-3,-4,-5),'InvalidInput','-3,-4,-5 is invalid input')
        self.assertEqual(classifyTheTriangle(2.5,3.5,4.5),'InvalidInput','2.5,3.5,4.5 is invalid input')
        self.assertEqual(classifyTheTriangle("a", "b", "c"),'InvalidInput','"a","b","c" are invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
