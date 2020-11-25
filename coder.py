class Coder:
    def encode_symbol(self, symbol, operation_type, indent=3):
        if operation_type == 'encode': 
            symbol_number = ord(symbol) +indent
        elif operation_type == 'decode': 
            symbol_number = ord(symbol) -indent
        new_symbol = chr(symbol_number)
        return new_symbol

    def translation(self, text, operation_type):
        translated = ''
        for symb in text:
            translated += self.encode_symbol(symb, operation_type)
        return translated

       

s = Coder()

while True:

    print(s.translation(input('Введи текст\n'), input('Что делаем? encode/decode\n')))
