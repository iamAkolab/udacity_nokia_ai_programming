# The git branch command
The git branch command is used to interact with Git's branches:

$ git branch
It can be used to:

* list all branch names in the repository
* create new branches
* delete branches

## Create A Branch
To create a branch, all you have to do is use git branch and provide it the name of the branch you want 
it to create. So if you want a branch called "sidebar", you'd run this command:

$ git branch sidebar


## The git checkout Command
Remember that when a commit is made that it will be added to the current branch. So even though we created the new sidebar, 
no new commits will be added to it since we haven't switched to it, yet. If we made a commit right now, that commit would be 
added to the master branch, not the sidebar branch. We've already seen this in the demo, but to switch between branches, 
we need to use Git's checkout command.

$ git checkout sidebar
It's important to understand how this command works. Running this command will:

* remove all files and directories from the Working Directory that Git is tracking
  * (files that Git tracks are stored in the repository, so nothing is lost)
* go into the repository and pull out all of the files and directories of the commit that the branch points to


So this will remove all of the files that are referenced by commits in the master branch. It will replace them with the files 
that are referenced by the commits in the sidebar branch. This is very important to understand, so go back and read these last two sentences.

The funny thing, though, is that both sidebar and master are pointing at the same commit, so it will look like nothing changes 
when you switch between them. But the command prompt will show "sidebar", now:
