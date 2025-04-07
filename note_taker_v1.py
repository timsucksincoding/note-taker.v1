class NoteTakingApp:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print("Note added!")

    def delete_note(self, note_index):
        if 0 <= note_index < len(self.notes):
            deleted_note = self.notes.pop(note_index)
            print(f"Deleted note: {deleted_note}")
        else:
            print("Invalid note index!")

    def display_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            print("Your Notes:")
            for index, note in enumerate(self.notes):
                print(f"{index}: {note}")

    def homepage(self):
        while True:
            print("\n--- Note Taking App ---")
            print("1. Add Note")
            print("2. Delete Note")
            print("3. View Notes")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                note = input("Enter your note: ")
                self.add_note(note)
            elif choice == '2':
                self.display_notes()
                note_index = int(input("Enter the index of the note to delete: "))
                self.delete_note(note_index)
            elif choice == '3':
                self.display_notes()
            elif choice == '4':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    app = NoteTakingApp()
    app.homepage()
