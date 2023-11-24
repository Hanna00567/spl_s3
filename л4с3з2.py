from string import ascii_uppercase


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f"Alphabet ({self.lang}) :{self.letters}")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = len(ascii_uppercase)

    def __init__(self, lang='En'):
        super().__init__(lang, ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "Hello, world"


alphabet_obj = Alphabet("Custom", "ABC")
alphabet_obj.print()
print("Number of letters in custom alphabet:", alphabet_obj.letters_num())

eng_alphabet_obj = EngAlphabet()
eng_alphabet_obj.print()
print("Number of letters in English alphabet:", eng_alphabet_obj.letters_num())
print("Is 'A' an English letter?", eng_alphabet_obj.is_en_letter('A'))
print("Is 'Я' an English letter?", eng_alphabet_obj.is_en_letter('Я'))
print("Example text in English:", EngAlphabet.example())
