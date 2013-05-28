#
# Class: Note
# 
# This is the base note class for a Note object which will contain the content.
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
        self.id = 0
    
    #Function to set Note
    def create_note(self, content_to_add):
        self._note_creator = 'system_default'
        self._note_content = content_to_add
        self._note_title = self.determine_title(content_to_add)
    
    #Updates the note with the specified content
    def update_note(self, content_to_update):
        self._note_content = content_to_update
        self._note_title = self.determine_title(content_to_update)
    
    #Determines the title from the content
    #by finding the first new line character.
    def determine_title(self, title_to_cut):
        return title_to_cut.split('\n', 1)[1]
