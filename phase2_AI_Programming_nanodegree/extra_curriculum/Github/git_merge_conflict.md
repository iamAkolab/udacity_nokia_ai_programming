# Git Merge Conflict

Most of the time Git will be able to merge branches together without any problem. However, there are instances when a merge cannot be fully performed automatically. 
When a merge fails, it's called a merge conflict

## What Causes A Merge Conflict
As you've learned, Git tracks lines in files. A merge conflict will happen when the exact same line(s) are changed in separate branches. For example, if you're on a 
alternate-sidebar-style branch and change the sidebar's heading to "About Me" but then on a different branch and change the sidebar's heading to "Information About Me", 
which heading should Git choose? You've changed the heading on both branches, so there's no way Git will know which one you actually want to keep.

Let's force a merge conflict so we can learn to resolve it. Trust me, it's simple once you get the hang of it! Remember that a merge conflict occurs when Git isn't sure which line(s) you want to use from the branches that are being merged. So we need to edit the same line on two different branches...and then try to merge them.


## Merge Conflict Output Explained
The output that shows in the Terminal is:

$ git merge heading-update 
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.


Notice that right after the git merge heading-update command, it tries merging the file that was changed on both branches (index.html), but that there was a conflict. Also, notice that it tells you what happened - "Automatic merge failed; fix conflicts and then commit the result".


## Merge Conflict Indicators Explanation
The editor has the following merge conflict indicators:

* <<<<<<< HEAD everything below this line (until the next indicator) shows you what's on the current branch
* ||||||| merged common ancestors everything below this line (until the next indicator) shows you what the original lines were
* ======= is the end of the original lines, everything that follows (until the next indicator) is what's on the branch that's being merged in
* *>>>>>>>* heading-update is the ending indicator of what's on the branch that's being merged in (in this case, the heading-update branch)

## Resolving A Merge Conflict
Git is using the merge conflict indicators to show you what lines caused the merge conflict on the two different branches as well as what the original line used to have. So to resolve a merge conflict, you need to:

* choose which line(s) to keep
* remove all lines with indicators


## Commit Merge Conflict
Once you've removed all lines with merge conflict indicators and have selected what heading you want to use, just save the file, add it to the staging index, and commit it! Just like with a regular merge, this will pop open your code editor for you to supply a commit message. Just like before, it's common to use the provided merge commit message, so after the editor opens, just close it to use the provided commit message.

And that's it! Merge conflicts really aren't all that challenging once you understand what the merge conflict indicators are showing you.
