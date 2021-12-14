class Note:
    def __init__(self, name, note):
        if type(name) is not str:
            raise TypeError('wrong name type')
        elif type(note) is not float:
            raise TypeError('wrong note type')
        elif name in [None, '']:
            raise Exception('name cant be null')
        elif not 2 <= note <= 6:
            raise Exception('note must be <= 6 and >=2')
        else:
            self.name = name
            self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note


