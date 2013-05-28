#
# Script: test
#
# Basic test playbed for testing the note app
#

#Import Note Class
from Note import Note

#Make a new note
temp = Note()

#Set content
temp.update_note('tester\nloles')

#Print the note contents
print 'my content is ' + temp._note_content
print 'my title is ' + temp._note_title