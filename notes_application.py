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

	def listNotes(self):
		for index,item in enumerate(self.notes):
			print "Note ID: ", index+1
			print item
			print "By ", self.author
	
	def get(self, note_id):
		if type(note_id) == int:
			print self.notes[note_id-1]

	def search(self, search_text):
		if type(search_text) == int:
			print "wrong input"
		if type(search_text) == str:
			for index,item in enumerate(self.notes):
				if search_text in item:
					print "Showing results for search", "'"+search_text+"'"
					print "Note ID: ", index+1
					print item
					print "By ", self.author
				elif search_text not in item:
					print "Not found!"
		else:
			print "error"

	def delete(self, note_id):
		if note_id > len(self.notes):
			print "Not applicable"
		if type(note_id) == int:
			self.notes.pop(note_id-1)
			return "delete successful"
		else:
			return "error"

	
a = NotesApplication("grey")
a.create("first note")
a.create("second note")
a.listNotes()
a.get(1)
a.search('this')
a.delete(1)
a.listNotes()