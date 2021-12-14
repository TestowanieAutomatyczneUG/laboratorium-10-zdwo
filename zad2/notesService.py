from notesStorage import NotesStorage


class NotesService:
    def __init__(self):
        self.ns = NotesStorage()

    def add(self, note):
        return self.ns.add(note)

    def averageOf(self, name):
        sum = 0
        notes = self.ns.getAllNotesOf(name)
        if len(notes) == 0:
            return sum
        for note in notes:
            sum += note
        avg = sum/len(notes)
        return avg

    def clear(self):
        return self.ns.clear()
