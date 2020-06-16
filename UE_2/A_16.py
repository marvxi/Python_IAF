text = open(r'C:\Users\Marvi\Documents\Pycharm_Projects\Python_IAF\UE_2\Text.txt')
text = str(text.readlines())


def encryption(text):
    text = text.upper() #Macht alle Buchstaben groß!
    encrypted_message = ''
    for character in text:
        num = ord(character) # Unicode, jedes Zeichen hat eine bestimmte Zahl int wert
        new_num = num + 3    # verändere den Unicode also + 3
        if new_num > ord('Z'):  # Wenn new_num größer als 90 ist:
            new_num = new_num - 26  # new_num wird um 26 verringert
            new_character = chr(new_num)
            encrypted_message = encrypted_message + new_character
    # Ausgabe
    return encrypted_message

encrp = encryption(text)

def decryption(text):
    decrpted_message = ''
    for character in text:
        num = ord(character)
        new_num = num + 26
        if new_num > ord('Z'):
            new_num = new_num - 3
            new_character = chr(new_num)

            decrpted_message = decrpted_message + new_character

    return decrpted_message

print(decryption(encrp))


