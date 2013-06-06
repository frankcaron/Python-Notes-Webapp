#Imports
import sqlite3 as lite

#Global Vars
_db_name = 'notes.db'

#
# Class: DBHelper
# 
# This helper class manipulates the DB
# 
# 2013, Frank Caron

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
        
class DBReader:
    
    # Private Variables
    _db_name = 'notes.db'
    _db_con = None
    _db_cursor = None
    
    #Do a DB read
    def db_read_all(self):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes')
            print "DBReader Results:\n" 
            print self._db_cursor.fetchall()
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()