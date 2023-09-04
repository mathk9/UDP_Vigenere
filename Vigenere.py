class Vigenere():  

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_length = len(key)

        for i in range(len(plain_text)):
            char = plain_text[i]
            if char.isalpha():
                # Calcula o deslocamento para o caractere atual na chave
                key_char = key[i % key_length]
                key_offset = ord(key_char.lower()) - ord('a')

                # Realiza a criptografia para letras maiúsculas e minúsculas
                if char.islower():
                    encrypted_char = chr(((ord(char) - ord('a') + key_offset) % 26) + ord('a'))
                else:
                    encrypted_char = chr(((ord(char) - ord('A') + key_offset) % 26) + ord('A'))

                encrypted_text += encrypted_char
            else:
                # Mantém caracteres não alfabéticos como estão
                encrypted_text += char

        return encrypted_text


    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_length = len(key)

        for i in range(len(encrypted_text)):
            char = encrypted_text[i]
            if char.isalpha():
                # Calcula o deslocamento para o caractere atual na chave
                key_char = key[i % key_length]
                key_offset = ord(key_char.lower()) - ord('a')

                # Realiza a descriptografia para letras maiúsculas e minúsculas
                if char.islower():
                    decrypted_char = chr(((ord(char) - ord('a') - key_offset) % 26) + ord('a'))
                else:
                    decrypted_char = chr(((ord(char) - ord('A') - key_offset) % 26) + ord('A'))

                decrypted_text += decrypted_char
            else:
                # Mantém caracteres não alfabéticos como estão
                decrypted_text += char

        return decrypted_text