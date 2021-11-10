## Calling the read Method with an Integer
"""
In the code you saw earlier, the call to f.read() had no arguments passed to it. This defaults to reading all the remainder of the file from its current position - the whole file. If you pass the read method an integer argument, it will read up to that number of characters, output all of them, and keep the 'window' at that position ready to read on.

Let's see this in an example that uses the following file, camelot.txt:

We're the knights of the round table
We dance whenever we're able

Here's a script that reads in the file a little at a time by passing an integer argument to .read().

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
Outputs:

We
're the 
knights of the round table
We dance whenever we're able
You can try out this example by creating your own camelot.txt and example.py files with the text above.

Each time we called read on the file with an integer argument, it read up to that number of characters, outputted them, and kept the 'window' at that position for the next call to read. This makes moving around in the open file a little tricky, as there aren't many landmarks to navigate by.

Reading Line by Line
\ns in blocks of text are newline characters. The newline character marks the end of a line, and tells a program (such as a text editor) to go down to the next line. However, looking at the stream of characters in the file, \n is just another character.

Fortunately, Python knows that these are special characters and you can ask it to read one line at a time. Let's try it!
"""
# Read the next line
# Use the relevant part of the Python documentation to find a method that reads the next line of a file. Put the name of the method in the box.

## readline()


"""
Conveniently, Python will loop over the lines of a file using the syntax for line in file. I can use this to create a list of lines in the file. Because each line still has its newline character attached, I remove this using .strip().

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

Outputs:

["We're the knights of the round table", "We dance whenever we're able"]
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Quiz: Flying Circus Cast List
You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. 
It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com). 
Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. 
You'll need to extract only the name and add it to a list. You might use the .split() method to process each line.
"""
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open(filename) as f:
        
         #use the for loop syntax to process each line
         for line in f:
             
            #and add the actor name to cast_list
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
    
#output
"""
Graham Chapman
Eric Idle
Terry Jones
Michael Palin
Terry Gilliam
John Cleese
Carol Cleveland
Ian Davidson
John Hughman
The Fred Tomlinson Singers
Connie Booth
Bob Raymond
Lyn Ashley
Rita Davies
Stanley Mason
David Ballantyne
Donna Reading
Peter Brett
Maureen Flanagan
Katya Wyeth
Frank Lester
Neil Innes
Dick Vosburgh
Sandra Richards
Julia Breck
Nicki Howorth
Jimmy Hill
Barry Cryer
Jeannette Wild
Marjorie Wilde
Marie Anderson
Caron Gardner
Nosher Powell
Carolae Donoghue
Vincent Wong
Helena Clayton
Nigel Jones
Roy Gunson
Daphne Davey
Stenson Falke
Alexander Curry
Frank Williams
Ralph Wood
Rosalind Bailey
Marion Mould
Sheila Sands
Richard Baker
Douglas Adams
Ewa Aulin
Reginald Bosanquet
Barbara Lindley
Roy Brent
Jonas Card
Tony Christopher
Beulah Hughes
Peter Kodak
Lulu
Jay Neill
Graham Skidmore
Ringo Starr
Fred Tomlinson
David Hamilton
Suzy Mandel
Peter Woods
"""

""""
flying_circus_cast.txt
Graham Chapman,  Various / ... (46 episodes, 1969-1974)
Eric Idle,  Various / ... (46 episodes, 1969-1974)
Terry Jones,  Various / ... (46 episodes, 1969-1974)
Michael Palin,  It's Man / ... (46 episodes, 1969-1974)
Terry Gilliam,  Various / ... (46 episodes, 1969-1974)
John Cleese,  Announcer / ... (40 episodes, 1969-1973)
Carol Cleveland,  Various / ... (34 episodes, 1969-1974)
Ian Davidson,  Algy Braithwaite / ... (8 episodes, 1969-1970)
John Hughman,  Alfred Lord Tennyson / ... (8 episodes, 1970-1974)
The Fred Tomlinson Singers,  Amantillado Chorus / ... (7 episodes, 1969-1973)
Connie Booth,  Animated Mother / ... (6 episodes, 1969-1974)
Bob Raymond,  'Dad' / ... (5 episodes, 1974)
Lyn Ashley,  Algon Girl / ... (5 episodes, 1970-1972)
Rita Davies,  Argument Secretary / ... (4 episodes, 1969-1972)
Stanley Mason,  Clapper Man / ... (4 episodes, 1970-1971)
David Ballantyne,  Ivan the Terrible / ... (3 episodes, 1970-1971)
Donna Reading,  Girl in Bikini with Its Man / ... (3 episodes, 1969)
Peter Brett,  Door-to-Door Martial Arts Salesman (2 episodes, 1974)
Maureen Flanagan,  Anona Winn / ... (2 episodes, 1969-1970)
Katya Wyeth,  Elsie / ... (2 episodes, 1969)
Frank Lester,  The Late Professor Thynne (2 episodes, 1972-1974)
Neil Innes,  Hesitant guitarist / ... (2 episodes, 1974)
Dick Vosburgh,  Van der Berg (1 episode, 1969)
Sandra Richards,  'Semprini' Girl / ... (1 episode, 1970)
Julia Breck,  Puss In Boots / ... (1 episode, 1972)
Nicki Howorth,  Miss Bladder (1 episode, 1972)
Jimmy Hill,  Himself (1 episode, 1974)
Barry Cryer,  Herman Rodrigues (1 episode, 1969)
Jeannette Wild,  Second Secretary (1 episode, 1970)
Marjorie Wilde,  Dear Old Lady (1 episode, 1970)
Marie Anderson,  Girl interviewing the announcer (1 episode, 1972)
Caron Gardner,  Mary (1 episode, 1973)
Nosher Powell,  Jack Bodell (1 episode, 1973)
Carolae Donoghue,  Vera's Husband's Mistress (1 episode, 1969)
Vincent Wong,  Mr. Kamikaze (1 episode, 1970)
Helena Clayton,  Various Roles (1 episode, 1971)
Nigel Jones,  Various (1 episode, 1972)
Roy Gunson, (1 episode, 1970)
Daphne Davey,  Various Roles (1 episode, 1971)
Stenson Falke, (1 episode, 1974)
Alexander Curry,  Various (1 episode, 1970)
Frank Williams,  Clerk of the Court (1 episode, 1972)
Ralph Wood, (1 episode, 1970)
Rosalind Bailey,  Elizabethan Girl (1 episode, 1972)
Marion Mould, (1 episode, 1974)
Sheila Sands,  Stripper / ... (uncredited) (2 episodes, 1969)
Richard Baker,  Himself - BBC News Anchor (uncredited) (3 episodes, 1972-1973)
Douglas Adams,  Dr. Emile Koning - Surgeon / ... (uncredited) (2 episodes, 1974)
Ewa Aulin,  Harrassed Woman (uncredited) (1 episode, 1969)
Reginald Bosanquet,  Himself (uncredited) (1 episode, 1970)
Barbara Lindley,  Bride (uncredited) (1 episode, 1970)
Roy Brent,  Armoured Knight (uncredited) (1 episode, 1972)
Jonas Card,  Armoured Knight (uncredited) (1 episode, 1972)
Tony Christopher,  Armoured Knight (uncredited) (1 episode, 1972)
Beulah Hughes, (uncredited) (1 episode, 1972)
Peter Kodak,  Armoured Knight (uncredited) (1 episode, 1972)
Lulu,  Herself (uncredited) (1 episode, 1972)
Jay Neill,  Armoured Knight (uncredited) (1 episode, 1972)
Graham Skidmore,  Armoured Knight (uncredited) (1 episode, 1972)
Ringo Starr,  Himself (uncredited) (1 episode, 1972)
Fred Tomlinson,  Superintendent McGough (uncredited) (1 episode, 1972)
David Hamilton,  Himself - Thames TV Announcer (uncredited) (1 episode, 1973)
Suzy Mandel,  German Girl (uncredited) (1 episode, 1974)
Peter Woods,  BBC Presenter (uncredited) (1 episode, 1974)
"""
