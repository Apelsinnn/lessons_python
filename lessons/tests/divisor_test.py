# В названии модуля всегда надо добавлять либо в начале, либо в конце _test, название_test
# Надо убедиться, что тест падает!! то есть специально сделать неправильный тест 2 == 3
# Сначала роняем тестом, потом пишем правильно(это называется redgreenrefactoring)

import doctest
from unittest import TestCase, main

from lessons import divisor


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(divisor))
    return tests


class DivisorTest(TestCase):
    def test_zero_devider(self):
        with self.assertRaises(ValueError) as e:
            divisor.divide(10, 0)
        self.assertEqual('На 0 делить нельзя', e.exception.args[0])


if __name__ == '__main__':
    main()
