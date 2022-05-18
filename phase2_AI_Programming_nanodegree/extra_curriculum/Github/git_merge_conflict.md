# Git Merge Conflict

Most of the time Git will be able to merge branches together without any problem. However, there are instances when a merge cannot be fully performed automatically. 
When a merge fails, it's called a merge conflict

## What Causes A Merge Conflict
As you've learned, Git tracks lines in files. A merge conflict will happen when the exact same line(s) are changed in separate branches. For example, if you're on a 
alternate-sidebar-style branch and change the sidebar's heading to "About Me" but then on a different branch and change the sidebar's heading to "Information About Me", 
which heading should Git choose? You've changed the heading on both branches, so there's no way Git will know which one you actually want to keep.

Let's force a merge conflict so we can learn to resolve it. Trust me, it's simple once you get the hang of it! Remember that a merge conflict occurs when Git isn't sure which line(s) you want to use from the branches that are being merged. So we need to edit the same line on two different branches...and then try to merge them.
