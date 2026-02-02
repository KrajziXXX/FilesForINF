class Notatka:
    def __init__(self,topic,des):
        self.topic = topic
        self.des = des
    
class Notes:
    def __init__(self):
        self.notatki = []
    def add_note(self,topic,des):
        note = Notatka(topic,des)
        self.notatki.append(note)
    def remove_note(self,topic):
        note_exists = False
        for note in self.notatki:
            if note.topic == topic:
                self.notatki.remove(note)
                note_exists = True
                break
        if not note_exists:
            print("Nie można znaleźć notatki")
    def display(self):
        if not self.notatki:
            print("Brak notatek")
        else:
            print("Notatki: ")
            for note in self.notatki:
                print(f"Topic: {note.topic} | description: {note.des}")

notes = Notes()
notes.add_note("Coś", "coś coś coś")
notes.add_note("Coś2", "coś coś coś")
notes.add_note("Coś3", "coś coś coś")
notes.display()

notes.remove_note("Coś")
notes.display()