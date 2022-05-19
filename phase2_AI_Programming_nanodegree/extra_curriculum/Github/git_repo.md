## What is a Remote Repository?

Git is a distributed version control system which means there is not one main repository of information. Each developer has a copy of the repository. 
So you can have a copy of the repository (which includes the published commits and version history) and your friend can also have a copy of the same 
repository. Each repository has the exact same information that the other ones have, there's no one repository that's the main one.


## Ways to access a Remote
Remotes can be accessed in a couple of ways:

* with a URL
* path to a file system
* 
Even though it's possible to create a remote repository on your file system, it's very rarely used. By far the most common way to access a remote 
repository is through a URL to a repository that’s out on the web.

The way we can interact and control a remote repository is through the Git remote command:

$ git remote

## Why Multiple Remotes?
Why would you want to have multiple remote repositories? We'll look at this later but briefly, if you are working with multiple developers then you might want to get changes they're working on in their branch(es) into your project before they merge them into the master branch. You might want to do this if you want to test out their change before you decide to implement your changes.

Another example is if you have a project whose code is hosted on Github but deploys via Git to Heroku. You would have one remote for the master and one for the deployment.
