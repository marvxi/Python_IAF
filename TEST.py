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

print(encryption('halloy'))