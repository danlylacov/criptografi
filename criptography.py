from functools import reduce


class Cryptografi_algoritms:
    def XOR(message, key):
        # алгоритм XOR - шифрования
        # расшиврование происходит повторным использованием алгоритма с тем же ключом
        i_message, len_message = 0, len(message)
        i_key, len_key = 0, len(key)
        result = ''
        while i_message < len_message:
            if i_key == len_key:
                i_key = 0
            result += chr(ord(message[i_message]) ^ ord(key[i_key])) # ord - str -> числовой код символа
            # chr() - числовой код символа -> str
            i_key += 1
            i_message += 1
        return result



class Mathematics:


    def ge2(x, y, p):
        # аддативная цепочка(метод двоичных квадратов и умножений)
        # x^y mod p -> result
        res = 1

        while (y > 0):

            if ((int(y) & 1) != 0): # & - побитовое "и"
                res = res * x

            y = y >> 1 # y cдвигаем влево на 1 бит(берем целую часть от корня)
            x = x * x  # возведение Х в квадрат

        return res % p

    def gcd(x, y, parametr='div'):
        # вычисление НОД(x, y)
        # алгортм Эвклида

        # проверка на ошибки входных данных
        if x < 0:
            x  = -x
        if y < 0:
            y = -y
        if x + y == 0:
            raise ValueError('Incorrect input data (x + y = 0)')

    # реализация через деление
        if parametr == 'div':
            while x != 0 and y != 0:
                if x >= y:
                    x = x % y
                else:
                    y = y % x
            return x or y

    # реализация через вычитание
        if parametr == 'sub':
            while x != 0 and y != 0:
                if x >= y:
                    x -= y
                else:
                    y -= x
            return x or y

    def gcd_extended(num1, num2):
        # расширенный алгорртим Eвклида
        # ax + by = gcd(a,b), где gcd – это функция по нахождения НОД.
        # a, b -> делитель, X, y
        if num1 == 0:
            return (num2, 0, 1)
        else:
            div, x, y = Mathematics.gcd_extended(num2 % num1, num1)
        return (div, y - (num2 // num1) * x, x)

    def totient(n):
        # функция эйлера
        # n -> k (количество чисел)
        if n <= 0:
            raise ValueError('Incorrect data! (n < 0)')

        k = 0
        i = 1
        while i != n:
            if Mathematics.gcd(i, n, 'div') == 1 or Mathematics.gcd(i, n, 'div') == -1:
                k += 1
            i+=1
        return k

    def chinese_remainder(pairs):
        "" "Китайская теорема об остатках" ""

        mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
        mod_product = reduce(lambda x, y: x * y, mod_list)
        mi_list = [mod_product // x for x in mod_list]
        mi_inverse = [Mathematics.gcd_extended(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
        x = 0
        for i in range(len(remainder_list)):
            x += mi_list[i] * mi_inverse[i] * remainder_list[i]
            x %= mod_product
        return x






























