#
# Class: Note
# 
# The base "Note" object which will contain and persist the content.
# 
# 2013, Frank Caron

class Note:
    
    # Private Variables
    _note_id = ''
    _note_creator = ''
    _note_content = ''
    _note_title = ''
    
    #Constructor method
    def __init__(self):
        #This will eventually sync with the ID in the DB
        self._note_id = 0
            
    #Function to set Note
    def create_note(self, content_to_add):
        self._note_creator = 'system_default'
        self._note_content = content_to_add
        self._note_title = self.determine_title(content_to_add + '\n')  #include a '\n' in case it's a one-liner
    
    #Updates the note with the specified content
    def update_note(self, content_to_update):
        self._note_content = content_to_update
        self._note_title = self.determine_title(content_to_update)
    
    #Determines the title from the content
    #by finding the first new line character.
    def determine_title(self, title_to_cut):
        return title_to_cut.split('\n', 1)[1]

#
# Class: NoteList
# 
# The List Collection for the notes resources
# 
# 2013, Frank Caron

class Notepad:
    
    #Private Variables
    _id = 0
    _notes = []
    
    #Constructor method
    def __init__(self):
    #This will eventually sync with the ID in the DB
        self._id = 0

    #Add note to the list
    def add_note(self, content):
        new_note = Note()
        new_note.create_note(content)
        self._notes.append(new_note)
        
    #Remove note at id
    def remove_note(self, note_id):
        del self._notes[note_id]