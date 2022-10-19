import unittest
'''
Разработайте юнит-тесты проверяющие корректность работы функции. 
Удалось ли найти какие-либо дефекты в этой функции, 
полагаясь на ее назначение исходя из описания? 
Учтите, что вопрос не на знание фреймворков тестирования и их 
применение, можете взять любой, 
или даже разработать ряд самостоятельных функций.

'''
'''
Написать функцию, которая запрашивает 
у пользователя цифры и проверяет, является ли данная пользователем цифра 
четной или нет, 
если четное - возвращать True
если нет - то возвращать False
'''
class Numbers(unittest.TestCase):
    def __init__(self, number):
        self.number = number

        def is_even(number):
            number = int(input('enter your num: '))
            if number % 2 == 0:
                print('Even')
            else:
                print('Odd')    
        is_even()    


class TestIsEvenNumbersOrNot(unittest.TestCase):

    def test_values(self):
        self.assertRaises(ValueError, is_even, -3)
        self.assertRaises(ValueError, is_even, -2)
        self.assertRaises(ValueError, is_even, -1)

    def test_equals(self):
        self.assertEqual(type(is_even), int)


if __name__ == '__main__':
    unittest.main()


