# Notes from videos

To get the package ready so they can be pip install you need to created the folder
The folder is a package if it contains the __init__.py
to import the class you add (.) dot before the file as its required in python3

The __init__ file is telling python that the folder contains a package
A package always needs to have an init file even if the fole is completely empty
The code inside the __init__ file is run whenever you import a package inside a python program

The setup.py file is necessary for pip installing
In this file we have meta data about the distribution package name, the version, the package etc.

To install the package, go to the terminal then go to the dir level of setup.py file
then type

$ pip install .
The . tells pip to look for setup.py file in the current folder

# make sure you create a virtual environment for your package
Conda
Conda does two things: manages packages and manages environments.

As a package manager, conda makes it easy to install Python packages, especially for data science. 
For instance, typing conda install numpy installs the numpy package.

As an environment manager, conda allows you to create silo-ed Python installations. 
With an environment manager, you can install packages on your computer without affecting your main Python installation.

The command line code looks something like the following:

conda create --name environmentname
source activate environmentname
conda install numpy


pip and Venv
There are other environmental managers and package managers besides conda. 
For example, venv is an environment manager that comes preinstalled with Python 3. pip is a package manager.

pip can only manage Python packages, whereas conda is a language-agnostic package manager. 
In fact, conda was invented because pip could not handle data science packages that depended on libraries outside of Python. 
If you look at the history of conda, you'll find that the software engineers behind conda needed a way to manage data science 
packages (such as NumPy and Matplotlib) that relied on libraries outside of Python.

conda manages environments and packages. pip only manages packages.

To use venv and pip, the commands look something like the following:

python3 -m venv environmentname
source environmentname/bin/activate
pip install numpy
