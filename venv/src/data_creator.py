#
# Script: Database Creator
# 
# The one-time use script will create and test the database
# 
# 2013, Frank Caron

# ==========
# Manifold
# ==========

#Imports
import sqlite3 as lite
import sys

#"Global" Vars
con = None

#Method to create the new columns
def create_table_columns():
    #Create column
    sql_1 = 'ALTER TABLE notes ADD COLUMN notes_id_key INTEGER PRIMARY KEY AUTOINCREMENT;'
    sql_1 += 'ALTER TABLE notes ADD COLUMN notepad_id_key INTEGER;'
    sql_1 += 'ALTER TABLE notes ADD COLUMN note_creator TEXT;'
    sql_1 += 'ALTER TABLE notes ADD COLUMN note_date_updated TEXT;'
    sql_1 += 'ALTER TABLE notes ADD COLUMN note_title TEXT;'
    sql_1 += 'ALTER TABLE notes ADD COLUMN note_content BLOB;'
    
    cur.execute(sql_1)

# ==========
# Test
# ==========

try:
    #Connect to db
    con = lite.connect('notes.db')
    
    #Select junk
    cur = con.cursor()    
    cur.execute('SELECT * FROM notes')
    data = cur.fetchone()
    
    #Print
    print "Data returned: " + str(data)   
    
    #Try alters
    create_table_columns()           
    
except lite.Error, e:
    
    #Catch and print errors
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    #Clean up
    if con:
        con.close()