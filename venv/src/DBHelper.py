#
# Module: DBHelper
# 
# This helper class manipulates the DB
# 
# 2013, Frank Caron

#Imports
import sqlite3 as lite

#Global Vars
_db_name = 'notes.db'

#
# Module: DBWriter
# 
# Writes to the DB

class DBWriter:
    
    # Private Variables
    _db_con = None
    _db_cursor = None
    
    #Do a DB update
    def db_update(self, query):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute(query)
            self._db_con.commit()
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        
    #Check if Notepad ID exists
    def db_check_notepad_id(self, notepad_id):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT COUNT(*) FROM notes WHERE notepad_id_key =' + str(notepad_id) + ';')
            number_occur = self._db_cursor.fetchone()[0]
            print number_occur
            return number_occur
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        
#
# Module: DBWriter
# 
# Reads from the DB

class DBReader:
    
    # Private Variables
    _db_con = None
    _db_cursor = None
    
    #Do a DB read
    def db_read_all(self):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes')
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        
    def db_get_last_row_id(self):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute("SELECT max(note_id) FROM notes")
            return str(self._db_cursor.fetchone()[0])
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()    
        
#
# Module: DBDeleter
# 
# Deletes from the DB  

class DBDeleter:
    
    # Private Variables
    _db_con = None
    _db_cursor = None 

    #Do a DB read
    def db_delete(self, note_id):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute("DELETE FROM notes WHERE note_id =" + str(note_id) + ";")
            self._db_con.commit()
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        