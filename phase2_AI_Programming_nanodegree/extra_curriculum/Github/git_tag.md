# Git Tag

The command we'll be using to interact with the repository's tags is the git tag command:

$ git tag -a v1.0


the -a flag is used. This flag tells Git to create an annotated flag. If you don't provide the flag (i.e. git tag v1.0) 
then it'll create what's called a lightweight tag.

Annotated tags are recommended because they include a lot of extra information such as:

* the person who made the tag
* the date the tag was made
* a message for the tag


Because of this, you should always use annotated tags.

# Verify Tag
So how do we know that a tag was actually added to the project? 
If you type out just $ git tag, it will display all tags that are in the repository.


Git Log's --decorate Flag
As you've learned, git log is a pretty powerful tool for letting us check out a repository's commits. 
We've already looked at a couple of its flags, but it's time to add a new one to our toolbelt. 
The --decorate flag will show us some details that are hidden from the default view.

# Deleting A Tag
What if you accidentally misspelled something in the tag's message, or mistyped the actual tag name (v0.1 instead of v1.0). 
How could you fix this? The easiest way is just to delete the tag and make a new one.

A Git tag can be deleted with the -d flag (for delete!) and the name of the tag:

$ git tag -d v1.0

# Adding A Tag To A Past Commit
Running git tag -a v1.0 will tag the most recent commit. But what if you wanted to tag a commit that occurred farther back in the repo's history?

$ git tag -a v1.0 a87984

$ git tag -a beta
This command will:

add a tag to the most recent commit
add a tag to a specific commit if a SHA is passed

# Further Research
* Git Basics - Tagging from the Git Book (https://git-scm.com/book/en/v2/Git-Basics-Tagging)
* Git Tag from the Git Docs (https://classroom.udacity.com/nanodegrees/nd089/parts/ac9572c6-8411-4686-8f5c-523a54a2ac8e/modules/5df54f2e-1c9f-4b41-9bde-421b8c39b547/lessons/51789de2-57a9-4791-8974-8472035519b3/concepts/35782070-b658-4a89-b045-2cc6b1ce1acb#:~:text=Further%20Research,the%20Git%20Docs)
