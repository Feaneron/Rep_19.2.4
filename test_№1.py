import pytest
from apps.Calculator import Calculator

class TestCalculator:
    def setup(self):
        self.Calculator = Calculator

    def test_adding_success(self):
        assert self.Calculator.adding(self, 1, 1) == 2

    def test_division_success(self):
        assert self.Calculator.division(self, 6, 2) == 3

    def test_subtraction_success(self):
        assert self.Calculator.subtraction(self, 6, 2) == 4

    def test_multiply_success(self):
        assert self.Calculator.multiply(self, 2, 2) == 4



