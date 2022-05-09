# Git Log Recap


## git log
The git log command is used to display all of the commits of a repository.

$ git log
By default, this command displays:

the SHA
the author
the date
and the message
...of every commit in the repository. I stress the "By default" part of what Git displays because 
the git log command can display a lot more information than just this.

Git uses the command line pager, Less, to page through all of the information. The important keys for Less are:

to scroll down by a line, use j or ↓
to scroll up by a line, use k or ↑
to scroll down by a page, use the spacebar or the Page Down button
to scroll up by a page, use b or the Page Up button
to quit, use q

## git log --oneline
The git log command has a flag that can be used to alter how it displays the repository's information. 

$ git log --oneline
This command:

* lists one commit per line
* shows the first 7 characters of the commit's SHA
* shows the commit's message


## git log --stat
The git log command has a flag that can be used to display the files that have been changed in the commit, 
as well as the number of lines that have been added or deleted.


Remember, the q key gets out of the git log view. We're still using git log but are just passing a flag to 
change how the information is displayed. So the q key still works and returns the terminal to the command prompt.


## git log -p
The git log command has a flag that can be used to display the actual changes made to a file. The flag is --patch which can be shortened to just -p:

$ git log -p
