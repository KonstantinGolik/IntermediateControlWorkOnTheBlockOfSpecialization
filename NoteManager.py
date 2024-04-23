import json
import os
import datetime
from Note import Note

NOTES_FILE = "notes.json"

class NoteManager:
    NOTES_FILE = "notes.json"

    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.NOTES_FILE):
            with open(self.NOTES_FILE, "r") as file:
                notes_data = json.load(file)
                self.notes = [Note(**note) for note in notes_data]

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.NOTES_FILE, "w") as file:
            json.dump(notes_data, file, indent=4)

    def create_note(self, title, body):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body, timestamp)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        if not self.notes:
            print("Заметок нет.")
        else:
            for note in self.notes:
                print(note)
                print()

    def edit_note(self, note_id, new_title=None, new_body=None):
        for note in self.notes:
            if note.id == note_id:
                if new_title:
                    note.title = new_title
                if new_body:
                    note.body = new_body
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return True
    
        print("Заметка с указанным ID не найдена.")
        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                for i, remaining_note in enumerate(self.notes):
                    if remaining_note.id > note_id:
                        remaining_note.id -= 1
                self.save_notes()
                return True
        return False