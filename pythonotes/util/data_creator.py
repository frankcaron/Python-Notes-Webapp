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
    
except lite.Error, e:
    #Catch and print errors
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    #Clean up
    if con:
        con.close()