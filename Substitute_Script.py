# mono-alphabetic substitution cipher

alphabet_large = ['A', 'B', 'C', 'D', 'E', 'F',
                  'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R',
                  'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z']

alphabet_small = ['a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z']

symbols = ['.', ',', '?', '!', '#']


def generate_the_key():
    dictionary_key_small = {}
    dictionary_key_large = {}
    dictionary_symbols = {}

    file = 'passwd.txt'
    with open(file, 'r', encoding='utf-8') as f:
        text = f.readlines()

    value_small = 0
    value_large = 0
    value = 0

    for x in text:
        for y in x:
            if y in alphabet_small and value_small < len(alphabet_small):
                letter = alphabet_small[value_small]
                dictionary_key_small[letter] = y
                value_small += 1
            elif y in alphabet_large and value_large < len(alphabet_large):
                letter = alphabet_large[value_large]
                dictionary_key_large[letter] = y
                value_large += 1
            elif y in symbols and value < len(symbols):
                symbol = symbols[value]
                dictionary_symbols[symbol] = y
                value += 1
    return dictionary_key_small, dictionary_key_large, dictionary_symbols


def encrypt_the_text(text):
    encrypted_text = []
    dictionary_small, dictionary_large, dictionary_symbols = generate_the_key()
    for letter in text:
        if letter in dictionary_small:
            value = dictionary_small[letter]
            encrypted_text.append(value)
        elif letter in dictionary_large:
            value = dictionary_large[letter]
            encrypted_text.append(value)
        elif letter in dictionary_symbols:
            value = dictionary_symbols[letter]
            encrypted_text.append(value)
        else:
            encrypted_text.append(letter)

    final_encrypted_text = ''.join(encrypted_text)
    return final_encrypted_text


def upload_the_file():
    file = 'plain.txt'
    new_file = 'substitute_proprietary.txt'

# utf-8 used to use Polish diacritical marks
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    encrypted_text = encrypt_the_text(text)

    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

    return text


if __name__ == '__main__':
    upload_the_file()
