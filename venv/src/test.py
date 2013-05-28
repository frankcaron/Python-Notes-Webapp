#
# Script: test
#
# Basic test playbed for testing the note app
#

#Import Note Class
from Notes import Note
from Notes import Notepad

#
# ===========
# Tier 1 Test: No Lists
# ===========
#

print 'test 1: '

#Make a new note
temp = Note()
temp.create_note('test')

#Set content
temp.update_note('tester\nloles')

#Print the note contents
print 'my content is ' + temp._note_content
print 'my title is ' + temp._note_title

#
# ===========
# Tier 2 Test: Lists
# ===========
#

print '\ntest 2: '

#Make a New List
temp2 = Notepad()

#Add some notes
temp2.add_note('note1')
temp2.add_note('note2')
temp2.add_note('note3')

#Print the deets
print 'There are ' + str(len(temp2._notes)) + ' notes'
print 'The second note has the following content: ' + temp2._notes[1]._note_content

#Remove the second note
temp2.remove_note(1)

#Print the deets
print 'There are ' + str(len(temp2._notes)) + ' notes'
print 'The second note has the following content: ' + temp2._notes[1]._note_content
