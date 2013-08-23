#
# Module: DBHelper
# 
# This helper class manipulates the DB
# 
# 2013, Frank Caron

#Imports
import os
import psycopg2
import urlparse
import datetime

#Connection
urlparse.uses_netloc.append("postgres")

#Remote
url = urlparse.urlparse(os.environ["HEROKU_POSTGRESQL_RED_URL"])

#Local
#url = urlparse.urlparse("postgres://frankcaron:@127.0.0.1:5432/postgres")

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
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)

        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute(query)
            self._db_con.commit()
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
        self._db_cursor.close()
        self._db_con.close()
        
    #Create a new note
    def db_create_note(self, note_content, note_creator, note_id):
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
            
        #Prep DB Query
        _note_create_query = "INSERT INTO notes (note_content, note_title, note_creator, note_date_updated, notepad_id_key)"
        _note_create_query += "VALUES ('" + note_content + "','" + "Test" + "','" + note_creator + "','"
        _note_create_query += str(datetime.datetime.now()) + "'," + str(note_id) + ");"

        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute(_note_create_query)
            self._db_con.commit()
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
        self._db_cursor.close()
        self._db_con.close()
        
    #Check if Notepad ID exists
    def db_check_notepad_id(self, notepad_id):
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT COUNT(*) FROM notes WHERE notepad_id_key =' + str(notepad_id) + ';')
            return self._db_cursor.fetchone()[0]
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
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
    
    #Do a DB read for all notes
    def db_read_all(self):
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes')
            r = [dict((self._db_cursor.description[idx][0], value)
               for idx, value in enumerate(row)) for row in self._db_cursor.fetchall()]
            return r 
            
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
        self._db_cursor.close()
        self._db_con.close()
    
    #Do a DB read for a specific note
    def db_read_specific(self, note_id):
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes where note_id =' + str(note_id))
            r = [dict((self._db_cursor.description[idx][0], value)
               for idx, value in enumerate(row)) for row in self._db_cursor.fetchall()]
            return r 
            
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
        self._db_cursor.close()
        self._db_con.close()

    #Do a DB read for a specific notepad
    def db_read_specific_notepad(self, notepad_id):
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes where notepad_id_key =' + str(notepad_id))
            r = [dict((self._db_cursor.description[idx][0], value)
               for idx, value in enumerate(row)) for row in self._db_cursor.fetchall()]
            return r 
            
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
        self._db_cursor.close()
        self._db_con.close()
     
    #Do a DB read for the last row ID   
    def db_get_last_row_id(self):
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute("SELECT max(note_id) FROM notes")
            return str(self._db_cursor.fetchone()[0])
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
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
        self._db_con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute("DELETE FROM notes WHERE note_id =" + str(note_id) + ";")
            self._db_con.commit()
        except Exception, e:
            print "DBHelper Error: " + e.pgerror
        self._db_cursor.close()
        self._db_con.close()
        