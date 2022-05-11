# Make A Commit
Ok, let's do it!

To make a commit in Git you use the git commit command, but don't run it just yet. Running this command will open the code editor that you configured way back in the first lesson. If you haven't run this command yet:

$ git config --global core.editor <your-editor's-config-went-here>
...go back to the Git configuration step and configure Git to use your chosen editor.

If you didn't do this step and you already ran git commit, then Git probably defaulted to using the "Vim" editor. Vim is a popular editor for people who have been using Unix or Linux systems forever, but it's not the friendliest for new users. It's definitely not in the scope of this course. Check out this Stack Overflow post on how to get out of Vim and return to the regular command prompt.

If you did configure your editor, then go ahead and make a commit using the git commit command:

$ git commit


Code Editor Commit Message Explanation
Ok, switch back to the code editor. Here's what's showing in my editor:

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
#
# Initial commit
#
# Changes to be committed:
#    new file:   css/app.css
#    new file:   index.html
#    new file:   js/app.js
#

Bypass The Editor With The -m Flag
TIP: If the commit message you're writing is short and you don't want to wait for your code editor to open up to type it out, you can pass your message directly on the command line with the -m flag:

$ git commit -m "Initial commit"


# Good Commit Messages


https://docs.github.com/en/get-started/getting-started-with-git/associating-text-editors-with-git

## Do

* do keep the message short (less than 60-ish characters)
* do explain what the commit does (not how or why!)


## Do not

* do not explain why the changes are made (more on this below)
* do not explain how the changes are made (that's what git log -p is for!)
* do not use the word "and"
  * if you have to use "and", your commit message is probably doing too many changes - break the changes into separate commits
  * e.g. "make the background color pink and increase the size of the sidebar"
