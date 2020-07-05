import os
import speech_recognition as s


class Model:

    def __init__(self):
        self.key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.offset = 5

    def encrypt(self, plaintext):
        result = ''
        for ch in plaintext:
            try:
                i = (self.key.index(ch) + self.offset) % 62
                result = result + self.key[i]
            except ValueError:
                result = result + ch
        return result

    def decrypt(self, ciphertext):
        result = ''
        for ch in ciphertext:
            try:
                i = (self.key.index(ch) - self.offset) % 62
                result = result + self.key[i]
            except ValueError:
                result = result + ch
        return result

    def save_file(self, msg, url):
        if type(url) is not str:
            file = url.name
        else:
            file = url

        filename, file_extension = os.path.splitext(file)
        if file_extension in '.ntxt':
            content = msg
            encrypted = self.encrypt(content)
            with open(file, 'w', encoding='utf-8') as fw:
                fw.write(encrypted)

        else:
            content = msg
            with open(file, 'w', encoding='utf-8') as fw:
                fw.write(content)
        #shorter version in mobile gallery

    def save_as(self, msg, url):
        if type(url) is not str:
            file = url.name
        else:
            file = url

        with open(file, 'w', encoding='utf-8') as fw:
            content = msg
            encrypted = self.encrypt(content)
            fw.write(encrypted)
    # shorter version in mobile gallery

    def read_file(self, url):
        base = os.path.basename(url)
        filename, file_extension = os.path.splitext(url)
        print(filename, file_extension)
        if file_extension in '.ntxt':
            f1 = open(url, 'r')
            msg1 = f1.read()
            decrypted = self.decrypt(msg1)
            f1.close()
            return decrypted, base
        else:
            f1 = open(url, 'r')
            msg1 = f1.read()
            f1.close()
            return msg1, base
        #shorter version in moble gallery

    def take_querry(self):
        sr = s.Recognizer()
        sr.pause_threshold = 1
        with s.Microphone() as m:
            #sr.adjust_for_ambient_noise(m)
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            return query

