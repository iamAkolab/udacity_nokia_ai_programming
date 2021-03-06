# The git reset Command

The git reset command is used to reset (erase) commits:

$ git reset <reference-to-commit>
It can be used to:

* move the HEAD and current branch pointer to the referenced commit
* erase commits
* move committed changes to the staging index
* unstage committed changes

## Git Reset's Flags
The way that Git determines if it erases, stages previously committed changes, or unstages previously committed changes is by the flag that's used. The flags are:

* --mixed
* --soft
* --hard

💡 Backup Branch 💡
Remember that using the git reset command will erase commits from the current branch. So if you want to follow along with all the resetting stuff that's coming up, you'll need to create a branch on the current commit that you can use as a backup.

Before I do any resetting, I usually create a backup branch on the most-recent commit so that I can get back to the commits if I make a mistake:

$ git branch backup
  
## Reset's --mixed Flag
Let's look at each one of these flags.

* 9ec05ca (HEAD -> master) Revert "Set page heading to "Quests & Crusades""
* db7e87a Set page heading to "Quests & Crusades"
* 796ddb0 Merge branch 'heading-update'
  
Using the sample repo above with HEAD pointing to master on commit 9ec05ca, running git reset --mixed HEAD^ will take the changes made in commit 9ec05ca and move them to the working directory.  
 
 💡 Back To Normal 💡
If you created the backup branch prior to resetting anything, then you can easily get back to having the master branch point to the same commit as the backup branch. You'll just need to:

remove the uncommitted changes from the working directory
merge backup into master (which will cause a Fast-forward merge and move master up to the same point as backup)
$ git checkout -- index.html
$ git merge backup 
 
## Reset's --soft Flag
Let's use the same few commits and look at how the --soft flag works:

* 9ec05ca (HEAD -> master) Revert "Set page heading to "Quests & Crusades""
* db7e87a Set page heading to "Quests & Crusades"
* 796ddb0 Merge branch 'heading-update'
Running git reset --soft HEAD^ will take the changes made in commit 9ec05ca and move them directly to the Staging Index. 
  
##   Reset's --hard Flag
Last but not least, let's look at the --hard flag:

* 9ec05ca (HEAD -> master) Revert "Set page heading to "Quests & Crusades""
* db7e87a Set page heading to "Quests & Crusades"
* 796ddb0 Merge branch 'heading-update'
  
Running git reset --hard HEAD^ will take the changes made in commit 9ec05ca and erases them.
  
  
## Reset vs Revert
At first glance, resetting might seem coincidentally close to reverting, but they are actually quite different. Reverting creates a new commit that reverts or undos 
a previous commit. Resetting, on the other hand, erases commits!
  
⚠️ Resetting Is Dangerous ⚠️
You've got to be careful with Git's resetting capabilities. This is one of the few commands that lets you erase commits from the repository. 
If a commit is no longer in the repository, then its content is gone.

To alleviate the stress a bit, Git does keep track of everything for about 30 days before it completely erases anything. To access this content, 
you'll need to use the git reflog command. Check out these links for more info:

* git-reflog (https://git-scm.com/docs/git-reflog)
* Rewriting History (https://www.atlassian.com/git/tutorials/rewriting-history)
* reflog, your safety net (http://gitready.com/intermediate/2009/02/09/reflog-your-safety-net.html)
  
  
## Relative Commit References
You already know that you can reference commits by their SHA, by tags, branches, and the special HEAD pointer. Sometimes that's not enough, though. 
There will be times when you'll want to reference a commit relative to another commit. For example, there will be times where you'll want to tell 
Git about the commit that's one before the current commit...or two before the current commit. There are special characters called "Ancestry References" 
that we can use to tell Git about these relative references. Those characters are:

* ^ – indicates the parent commit
* ~ – indicates the first parent commit
  
Here's how we can refer to previous commits:

* the parent commit – the following indicate the parent commit of the current commit
  * HEAD^
  * HEAD~
  * HEAD~1
  
* the grandparent commit – the following indicate the grandparent commit of the current commit
  * HEAD^^
  * HEAD~2

* the great-grandparent commit – the following indicate the great-grandparent commit of the current commit
  * HEAD^^^
  * HEAD~3
  
The main difference between the ^ and the ~ is when a commit is created from a merge. A merge commit has two parents. With a merge commit, 
the ^ reference is used to indicate the first parent of the commit while ^2 indicates the second parent. The first parent is the branch you 
were on when you ran git merge while the second parent is the branch that was merged in.

## reseting 

  You did so well on that last one, why not give this one a go! Using the same repository, which commit is referenced by HEAD~4^2?
  
That's right! HEAD~4 references the fourth parent commit of the current one and then the ^2 tells us that it's the second parent of the merge commit (the one that got merged in!).

  
## Further Research
* git-reset from Git docs (https://git-scm.com/docs/git-reset)
* Reset Demystified from Git Blog (https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)
* Ancestry References from Git Book (https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#Ancestry-References)
