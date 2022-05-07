Heads up! We'll be using the following terminal commands in this lesson:

ls - used to list files and directories
mkdir - used to create a new directory
cd - used to change directories
rm - used to remove files and directories

If you want to follow along with me:

create a directory called udacity-git-course
inside that, create another directory called new-git-project
use the cd command to move into the new-git-project directory
If you're a copy/paster like me, just run this command on the terminal - mkdir -p udacity-git-course/new-git-project && cd $_ 


Git Init
Fantastic work - we're all set up and ready to start using the git init command!

This is one of the easiest commands to run. All you have to do is run git init on the terminal.

.Git Directory Contents
We're about to take a look at the .git directory...it's not vital for this course, though, so don't worry about memorizing anything, it's here if you want to dig a little deeper into how Git works under the hood.

Here's a brief synopsis on each of the items in the .git directory:

config file - where all project specific configuration settings are stored.
From the Git Book:

Git looks for configuration values in the configuration file in the Git directory (.git/config) of whatever repository you’re currently using. These values are specific to that single repository.

For example, let's say you set that the global configuration for Git uses your personal email address. If you want your work email to be used for a specific project rather than your personal email, that change would be added to this file.

description file - this file is only used by the GitWeb program, so we can ignore it
hooks directory - this is where we could place client-side or server-side scripts that we can use to hook into Git's different lifecycle events
info directory - contains the global excludes file
objects directory - this directory will store all of the commits we make
refs directory - this directory holds pointers to commits (basically the "branches" and "tags")
Remember, other than the "hooks" directory, you shouldn't mess with pretty much any of the content in here. The "hooks" directory can be used to hook into different parts or events of Git's workflow, but that's a more advanced topic that we won't be getting into in this course.



Working with Git on the command line can be a little bit challenging because it's a little bit like a black box. I mean, how do you know when you should or shouldn't run certain Git commands? Is Git ready for me to run a command yet? What if I run a command but I think it didn't work...how can I find that out? The answer to all of these questions is the git status command!

$ git status
The git status is our key to the mind of Git. It will tell us what Git is thinking and the state of our repository as Git sees it. When you're first starting out, you should be using the git status command all of the time! Seriously. You should get into the habit of running it after any other command. This will help you learn how Git works and it'll help you from making (possibly) incorrect assumptions about the state of your files/repository.

The output tells us two things:

On branch master – this tells us that Git is on the master branch. You've got a description of a branch on your terms sheet so this is the "master" branch (which is the default branch). We'll be looking more at branches in lesson 5
Your branch is up-to-date with 'origin/master'. – Because git clone was used to copy this repository from another computer, this is telling us if our project is in sync with the one we copied from. We won't be dealing with the project on the other computer, so this line can be ignored.
nothing to commit, working directory clean – this is saying that there are no pending changes.
