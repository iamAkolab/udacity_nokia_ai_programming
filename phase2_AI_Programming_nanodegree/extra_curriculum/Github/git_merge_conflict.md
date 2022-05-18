# Git Merge Conflict

Most of the time Git will be able to merge branches together without any problem. However, there are instances when a merge cannot be fully performed automatically. 
When a merge fails, it's called a merge conflict

## What Causes A Merge Conflict
As you've learned, Git tracks lines in files. A merge conflict will happen when the exact same line(s) are changed in separate branches. For example, if you're on a 
alternate-sidebar-style branch and change the sidebar's heading to "About Me" but then on a different branch and change the sidebar's heading to "Information About Me", 
which heading should Git choose? You've changed the heading on both branches, so there's no way Git will know which one you actually want to keep.
