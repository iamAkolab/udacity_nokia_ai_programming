
iam_Akolab@akolab MINGW64 ~
$ cd

iam_Akolab@akolab MINGW64 ~
$ start .

iam_Akolab@akolab MINGW64 ~
$ mv bash_profile .bash_profile

iam_Akolab@akolab MINGW64 ~
$ mv udacity-terminal-config .udacity-terminal-config

iam_Akolab@akolab MINGW64 ~
$



First Time Git Configuration
Before you can start using Git, you need to configure it. Run each of the following lines on the command line to make sure everything is set up.

# sets up Git with your name
git config --global user.name "<Your-Full-Name>"

# sets up Git with your email
git config --global user.email "<your-email-address>"

# makes sure that Git output is colored
git config --global color.ui auto

# displays the original state in a conflict
git config --global merge.conflictstyle diff3

git config --list
