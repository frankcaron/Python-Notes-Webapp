#
# Script: test
#
# Basic test playbed for testing the note app
#
#Import Classes
import Notes

#
print '\ntest 2: '

#Make a New List
temp2 = Notes.Notepad()

#Add some notes
temp2.add_note('note1')
temp2.add_note('note2')
temp2.add_note('note3')

#Print the deets
#print 'There are ' + str(len(temp2._notes)) + ' notes'
#print 'The second note has the following content: ' + temp2._notes[1]._note_content

#Remove the second note
temp2.remove_note(1)

#Print the deets
#print 'There are ' + str(len(temp2._notes)) + ' notes'
#print 'The second note has the following content: ' + temp2._notes[1]._note_content


