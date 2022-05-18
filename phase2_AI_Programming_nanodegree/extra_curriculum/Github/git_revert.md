# What Is A Revert?
When you tell Git to revert a specific commit, Git takes the changes that were made in commit and does the exact opposite of them. 
Let's break that down a bit. If a character is added in commit A, if Git reverts commit A, then Git will make a new commit where 
that character is deleted. It also works the other way where if a character/line is removed, then reverting that commit will add that content back!

## The git revert Command
Now that I've made a commit with some changes, I can revert it with the git revert command

$ git revert <SHA-of-commit-to-revert>
  
This command:

* will undo the changes that were made by the provided commit
* creates a new commit to record the change
  
## Further Research
* git-revert (https://git-scm.com/docs/git-revert) from Git Docs
* git revert (https://www.atlassian.com/git/tutorials/undoing-changes) Atlassian tutorial
