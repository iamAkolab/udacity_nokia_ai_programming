#TODO: 2: Creating Pet Image Labels
Fill the get_pet_labels() function to create pet image labels by creating a dictionary with key=filename and value=file label. (We will later use this to check the accuracy of the classifier function)

Coding within the check_images.py and get_pet_labels.py
Code to Edit
This section will help you code the function get_pet_labels within get_pet_labels.py. With this function you will be creating the labels for the pet images, using the filenames of the pet images in the pet_images folder. These images filenames represent the identity of the pet in the image. The pet image labels are considered to represent the "truth" about the classification of the image. Your function will return the Results Dictionary that will contain the pet image filenames and labels.

Code for the function definition def get_pet_labels(): as indicated by #TODO: 2 within get_pet_labels.py.
Follow the comments and the docstring within get_pet_labels.py to implement get_pet_labels
Code within the main() function within check_images.py indicated by #TODO: 2
Replace None within the function call with in_arg.dir to specify the appropriate directory.
Expected Outcome
When completed this code will return a dictionary with the pet image filename as the key and a List that contains only the pet image label as the value for all 40 pet images in the pet_image folder.

Checking your code
The check_creating_pet_image_labels function within check_images.py will check your code by printing out the number of key-value pairs and the first 10 key-value pairs.

You will need to visually check that the results show:

The dictionary containing 40 key-value pairs (e.g. dictionary length is 40).
The pet image labels the following way:
Lower case letters
Single space separating each word
Correct representation of the filenames (from the 10 key-value pairs)
Project Workspace - Pet Image Labels
The next concept will have your workspace to work on #TODO: 2
Editing of check_image.py and get_pet_labels.py can be done within the Project Workspace - Pet Image Labels
For additional information and help on #TODO: 2, please look at the information below:
How to Read Filenames from a Folder of Files
The folder pet_images/ in the lab workspace contains the 40 images you will be testing the classifier algorithms on. The filenames of the images in pet_images/ identify the animal in each image.

To create the labels for pet images you will need to:

Read all the files' names in the pet_image/ folder
Process the filenames to create the pet image labels
Format the pet image labels such that they can be matched to:
The classifier function labels
The dog names in dognames.txt
In the first task, the function will need to read the filenames from a folder. To achieve this task you will need to only import the listdir method from the os python module. The listdir method retrieves all filenames from the files within a folder. These filenames are returned from listdir as a list. The code below demonstrates how to perform this import and retrieval.

# Imports only listdir function from OS module 
from os import listdir  

# Retrieve the filenames from folder pet_images/
filename_list = listdir("pet_images/")

# Print 10 of the filenames from folder pet_images/
print("\nPrints 10 filenames from folder pet_images/")
for idx in range(0, 10, 1):
    print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
How to Create a Dictionary of Lists (similar to the Results Dictionary)
The Python Dictionary is the data structure you should use for the Pet Image filenames (as keys) and a List that contains the filenames associated labels (as values). The following are reasons for this data structure choice:

The key-value pairs of a dictionary are a logical choice because of the need to process the same filenames (keys) with the classifier function and compare its returned labels to those of pet image (values)
Given an input key, retrieval of the associated value is quicker than retrieval from other data structures (e.g. lists).
Dictionary Usage Review
In the Data Types and Operators lesson, you first learned about dictionaries. The code below will help you use Python dictionaries.

Creating an empty dictionary
Creating a dictionary that contains a List as the value.
Determines the number of items in a dictionary
Adds key-value pairs to the dictionary if the key doesn't already exist in the dictionary
Iterates through a dictionary printing all key-value pairs in a dictionary
# Creates empty dictionary named results_dic
results_dic = dict()

# Determines number of items in dictionary
items_in_dic = len(results_dic)
print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

# Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
# a List that contains only one item - the pet image label
filenames = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
pet_labels = ["beagle", "boston terrier"]
for idx in range(0, len(filenames), 1):
    if filenames[idx] not in results_dic:
         results_dic[filenames[idx]] = [pet_labels[idx]]
    else:
         print("** Warning: Key=", filenames[idx], 
               "already exists in results_dic with value =", 
               results_dic[filenames[idx]])

#Iterating through a dictionary printing all keys & their associated values
print("\nPrinting all key-value pairs in dictionary results_dic:")
for key in results_dic:
    print("Filename=", key, "   Pet Label=", results_dic[key][0])
(For more details on the dictionary of lists see the Classifying Images section that's after the Project Workspace - Pet Image Labels).

Pet Image File Format for Label Matching
With this project, you will need to determine matches between the pet image labels and the classifier labels. To be able to accomplish this matching task with your function, you will need to understand the format of both labels. Below is a detailed description of the format of the pet image filenames that you will be using to create the pet image labels.

Pet Image Files
The pet image files are located in the folder 'pet_images', in the workspace. Some examples of the filenames you will see are: Basenji_00963.jpg, Boston_terrier_02259.jpg, gecko_80.jpg, fox_squirrel_01.jpg

There are:

40 total images pet images
30 images of dogs
10 images of animals that aren't dogs
Name (label) of image (needed for comparison)
contains upper and lower case letters
contains one or more words to describe the image (label)
words are separated by an underscore (_)
Python Functions to Create Pet Image Labels
The best format for each pet image name would be:

Label: with only lower case letters
Blank space separating each word in a label composed of multiple words
Whitespace characters stripped from front & end of label
In the Lesson Data Types and Operators the sections on Strings and String Methods, you first learned about the string data type. Based upon the pet image filename format above, you can use the following string functions to achieve the label format:

lower() - places letters in lower case only.
split() - returns a list of words from a string, where the words have been separated (split) by the delimiter provided to the split function. If no delimiter is provided, splits on whitespace.
strip() - returns a string with leading & trailing characters removed. If no characters are provided, strips leading & trailing whitespace characters.
isalpha() - returns true only when a string contains only alphabetic characters, returns false otherwise.
Below you will find some code that demonstrates the use of the above string functions.

# Sets pet_image variable to a filename 
pet_image = "Boston_terrier_02259.jpg"

# Sets string to lower case letters
low_pet_image = pet_image.lower()

# Splits lower case string by _ to break into words 
word_list_pet_image = low_pet_image.split("_")

# Create pet_name starting as empty string
pet_name = ""

# Loops to check if word in pet name is only
# alphabetic characters - if true append word
# to pet_name separated by trailing space 
for word in word_list_pet_image:
    if word.isalpha():
        pet_name += word + " "

# Strip off starting/trailing whitespace characters 
pet_name = pet_name.strip()

# Prints resulting pet_name
print("\nFilename=", pet_image, "   Label=", pet_name)
