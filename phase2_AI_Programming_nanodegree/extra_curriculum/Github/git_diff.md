# Git Diff
To recap, the git diff command is used to see changes that have been made but haven't been committed, yet:

$ git diff

This command displays:

* the files that have been modified
* the location of the lines that have been added/removed
* the actual changes that have been made

# Git Ignore
If you want to keep a file in your project's directory structure but make sure it isn't accidentally committed to the project, you can use the specially named file, .gitignore (note the dot at the front, it's important!). Add this file to your project in the same directory that the hidden .git directory is located. All you have to do is list the names of files that you want Git to ignore (not track) and it will ignore them.

Let's try it with the "project.docx" file. Add the following line inside the .gitignore file:

$ touch .gitignore

project.docx
Now run git status and check its output:


# Globbing
Globbing lets you use special characters to match patterns/characters. In the .gitignore file, you can use the following:

* blank lines can be used for spacing
* # - marks line as a comment
* * - matches 0 or more characters
* ? - matches 1 character
* [abc] - matches a, b, _or_ c
* ** - matches nested directories - a/**/z matches
  * a/z
  * a/b/z
  * a/b/c/z

## Further Research
* Ignoring files from the Git Book (https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Ignoring-Files)
* gitignore from the Git Docs (https://git-scm.com/docs/gitignore#_pattern_format)
* Ignoring files from the GitHub Docs (https://help.github.com/articles/ignoring-files/)
* gitignore.io
