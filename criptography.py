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

print(Mathematics.ge2(2, 3, 5))
