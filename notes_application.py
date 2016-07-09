# creation of the Notesapplication class
class NotesApplication(object):
	def __init__(self, author, notes = []):
		self.author = author
		self.notes = notes

# function for creating notes	
	def create(self, note_content):
		if type(note_content) == str:
			self.notes.append(note_content)
			return "note created successfully"
		elif len(note_content) == 0:
			return "enter a note"
		else:
			return "only alphabets are allowed"

# function for listing all the notes created
	def listNotes(self):
		for index,item in enumerate(self.notes):
			print "Note ID: ", index+1
			print item
			print "By ", self.author
	
# function for getting note contents by its id
	def get(self, note_id):
		if type(note_id) == int:
			return self.notes[note_id-1]

# search function
	def search(self, search_text):
		if type(search_text) == int:
			return "wrong input"
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
			return "error"

# delete function
	def delete(self, note_id):
		if note_id > len(self.notes):
			return "Not applicable"
		if type(note_id) == int:
			self.notes.pop(note_id-1)
			return "delete successful"
		else:
			return "error"

# edit function
	def edit(self, note_id, new_content):
		if type(note_id) != int:
			return "error"
		if type(new_content) != str:
			return "error"
		else:
			self.notes.pop(note_id-1)
			self.notes.insert(note_id-1, new_content)
			return "edit successful"


# instantiation of the class	
a = NotesApplication("grey")
a.create("first note")
a.create("second note")
a.listNotes()
a.get(1)
a.search('this')
a.delete(1)
a.edit(2, "real second note")
a.listNotes()