DICT = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцшщъыьэюяQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789 .,;?:!()-|\"«»'"

class Encrypt:
    def __init__(self, key, string):

        out = ""
        for char in string:
            out += self.encrypt(char, key)
        self.encrypted = out

        s = ""
        for char in out:
            s += self.decrypt(char, key)
        self.decrypted = s

    def encrypt(self, char, k):
        s = DICT
        index = s.find(char)

        if k > len(s):
            k = k - len(s)

        if index + k >= len(s):
            return s[index + k - len(s)]
        else:
            return s[index + k]

    def decrypt(self, char, k):
        s = DICT
        index = s.find(char)

        if k > len(s):
            k = k - len(s)

        if index - k >= len(s):
            return s[index - k + len(s)]
        else:
            return s[index - k]


def main():
    try:
        k = int(input("Введите сдвиг K -> "))
        s = str(input("Введите строку -> "))
    except:
        print("Ошибка (Возможно присутствуют символы, которых нет в словаре)")
        return

    obj = Encrypt(k, s)
    print("Зашифрованный ключ: " + obj.encrypted)
    print("Расшифрованный ключ: " + obj.decrypted)

if __name__ == "__main__":
    main()