# В названии модуля всегда надо добавлять либо в начале, либо в конце _test, название_test
# Надо убедиться, что тест падает!! то есть специально сделать неправильный тест 2 == 3
# Сначала роняем тестом, потом пишем правильно(это называется redgreenrefactoring)

from unittest import TestCase, main

from lessons.tests.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('4-2'), 2)

    def test_multi(self):
        self.assertEqual(calculator('2*3'), 6)

    def test_divide(self):
        self.assertEqual(calculator('6/2'), 3.0)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и лишь один знак (+-/*)', e.exception.args[0])

    def test_float(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.3+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и лишь один знак (+-/*)', e.exception.args[0])

    def test_strint(self):
        with self.assertRaises(ValueError) as e:
            calculator('hello+world')
        self.assertEqual('Выражение должно содержать 2 целых числа и лишь один знак (+-/*)', e.exception.args[0])


if __name__ == '__main__':
    main()
