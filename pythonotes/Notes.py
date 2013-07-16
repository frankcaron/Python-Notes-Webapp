#
# Module: Notes
# 
# Classes related to the note objects.
# 
# 2013, Frank Caron

#Imports
import datetime
import DBHelper

#
# Class: Note
# 
# The base "Note" object which will contain and persist the content.

class Note:
    
    # Private Variables
    _note_id = ''
    _notepad_id = ''
    _note_creator = ''
    _note_content = ''
    _note_title = ''
    _note_db_query = ''
    _note_db_writer = DBHelper.DBWriter()
    _note_db_reader = DBHelper.DBReader()
    
    #Constructor method
    def __init__(self):
        #This will eventually sync with the ID in the DB
        self._note_id = 0
            
    #Function to set Note
    def create_note(self, content_to_add):
        self._note_creator = 'system_default'
        self._note_content = content_to_add
        self._note_title = self._determine_title(content_to_add + '\n')  #include a '\n' in case it's a one-liner
        
        #Prep DB Query
        self._note_db_query = "INSERT INTO notes (note_content, note_title, note_creator, note_date_updated, notepad_id_key)"
        self._note_db_query += "VALUES ('" + self._note_content + "','" + self._note_title + "','" + self._note_creator + "','"
        self._note_db_query += str(datetime.datetime.now()) + "'," + str(self._notepad_id) + ");"
        
        #Write to DB
        self._note_db_writer.db_update(self._note_db_query)
        
        #Read back new ID
        self._note_id = self._note_db_reader.db_get_last_row_id()
        
    #Updates the note with the specified content
    def update_note(self, content_to_update):
        self._note_content = str(content_to_update)
        self._note_title = self._determine_title(content_to_update + '\n')
        
        #, note_title, note_date_updated)"
        #Prep DB Query
        self._note_db_query = "UPDATE notes SET note_content='" + self._note_content + "',"
        self._note_db_query += "note_title='" + self._note_title + "',"
        self._note_db_query += "note_date_updated='" + str(datetime.datetime.now()) + "' "
        self._note_db_query += "WHERE note_id = " + self._note_id + ";" 
        
        #Write to DB
        self._note_db_writer.db_update(self._note_db_query)
     
    #Function to set the notepad ID for the note
    def assign_notepad(self, notepad_id):
        self._notepad_id = notepad_id
    
    #Determines the title from the content
    #by finding the first new line character.
    def _determine_title(self, title_to_cut):
        return title_to_cut.split('\n', 1)[0]

#
# Class: Notepad
# 
# The List Collection for the notes resources

class Notepad:
    
    #Private Variables
    _id = 0
    _notes = []
    _note_db_deleter = DBHelper.DBDeleter()
    
    #Constructor method
    def __init__(self, id_to_specify):
        
        _note_db_writer = DBHelper.DBWriter()
        if _note_db_writer.db_check_notepad_id(id_to_specify) == 0:
            self._id = id_to_specify
        else:
            print "Error: This ID already exists."

    #Add note to the list
    def add_note(self, content):
        new_note = Note()
        new_note.assign_notepad(self._id)
        new_note.create_note(content)
        self._notes.append(new_note)
        
    #Remove note at id
    def remove_note(self, note_id):
        self._note_db_deleter.db_delete(note_id)
        del self._notes[note_id]