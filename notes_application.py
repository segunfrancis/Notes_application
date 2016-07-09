class NotesApplication(object):
	def __init__(self, author, notes = []):
		self.author = author
		self.notes = notes

	def create(self, note_content):
		if type(note_content) == str:
			self.notes.append(note_content)
			return "note created successfully"
		elif len(note_content) == 0:
			return "enter a note"
		else:
			return "only alphabets are allowed"

			
a = NotesApplication("grey")
a.create("first note")
a.create("second note")