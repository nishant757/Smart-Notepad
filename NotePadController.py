import NotePadModel


class Controller:
    def __init__(self):
        self.notepadmodel = NotePadModel.Model()

    def save_file(self, msg, url):
        self.notepadmodel.save_file(msg, url)

    def save_as(self, msg, url):
        self.notepadmodel.save_as(msg, url)

    def read_file(self, url):
        self.msg, self.base = self.notepadmodel.read_file(url)
        return self.msg, self.base

    def take_querry(self):
        self.takeaudio = self.notepadmodel.take_querry()
        return self.takeaudio


