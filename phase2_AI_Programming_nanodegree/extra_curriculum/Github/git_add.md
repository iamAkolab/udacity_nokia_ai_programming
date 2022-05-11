Big Picture Review
That's really cool, isn't it! We haven't done anything specific with Git just yet, but it's watching this directory (since it's a Git project), and 
it knows that we've created a couple of new files. What's also pretty neat about the output of the git status command is that it's telling us that 
the files are untracked by Git.

Let's do a quick review of what's going on and what we're about to do:

* we have some new files that we want Git to start tracking
* for Git to track a file, it needs to be committed to the repository
* for a file to be committed, it needs to be in the Staging Index
* the git add command is used to move files from the Working Directory to the Staging Index


TIP: 

Did you also notice the helpful text that's located just beneath "Changes to be committed"? It says (use "git rm --cached <file>..." to unstage) 
This is a hint of what you should do if you accidentally ran git add and gave it the wrong file.

As a side note, git rm --cached is not like the shell's rm command. git rm --cached will not destroy any of your work; 
it just removes it from the Staging Index.

Also, this used the word "unstage". The act of moving a file from the Working Directory to the Staging Index is called "staging". 
If a file has been moved, then it has been "staged". Moving a file from the Staging Index back to the Working Directory will unstage the file. 
If you read documentation that says "stage the following files" that means you should use the git add command.
  

Stage Remaining Files
The index.html file has been staged. Let's stage the other two files. Now we could run the following:

$ git add css/app.css js/app.js
...but that's a lot of extra typing. We could use a special command line character to help:

The Period .
The period refers to the current directory and can be used as a shortcut to refer to all files and directories (including all nested files and directories!).

$ git add css/app.css js/app.js
# would become
$ git add .
  
  
The only thing to be careful of is that you might accidentally include more files than you meant to
