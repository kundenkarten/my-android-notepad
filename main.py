
import os

from kivy.app import App
from kivy.uix.textinput import TextInput


class MyNotepad(App):

    def build(self):

        # Permanent storage location
        self.filename = os.path.join(
            self.user_data_dir, "my_note.txt"
        )

        # Load previous note
        text = ""

        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                text = f.read()

        # Main writing area
        self.editor = TextInput(
            text=text,
            multiline=True,
            font_size=22,
            padding=15,
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(0.9, 0.9, 0.9, 1),
            cursor_color=(1, 1, 1, 1)
        )

        # Autosave whenever text changes
        self.editor.bind(text=self.save_note)

        return self.editor

    def save_note(self, *args):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(self.editor.text)

    def on_stop(self):
        self.save_note()


MyNotepad().run()
