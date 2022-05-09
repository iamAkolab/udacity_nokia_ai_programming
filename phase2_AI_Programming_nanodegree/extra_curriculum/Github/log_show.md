## Git Log Recap

The git log command is used to display all of the commits of a repository.

$ git log
By default, this command displays:

the SHA
the author
the date
and the message
...of every commit in the repository. I stress the "By default" part of what Git displays because the git log command can display a lot more information than just this.

Git uses the command line pager, Less, to page through all of the information. The important keys for Less are:

to scroll down by a line, use j or ↓
to scroll up by a line, use k or ↑
to scroll down by a page, use the spacebar or the Page Down button
to scroll up by a page, use b or the Page Up button
to quit, use q
