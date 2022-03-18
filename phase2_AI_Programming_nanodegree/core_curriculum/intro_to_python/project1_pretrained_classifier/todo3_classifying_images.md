#TODO: 3: Classifying Images
Implement the classify_images() function to create the classifier labels with the classifier function using in_arg.arch. Compare the labels, and create a dictionary of results (result_dic).

Code within the check_images.py and classify_images.py
Code to Edit
This section will help you code the function classify_images within classify_images.py. With this function, you will be creating the labels for the images using the classifier function. Additionally, you will be comparing these classifier's labels to the pet image labels. Finally, you will be storing the classifier generated labels, and the comparison of labels in the results dictionary (complex data structure) that was returned by get_pet_labels function.

Code within the function def classify_images() as indicated by #TODO: 3 within classify_images.py
Using the comments and docstring within classify_images.py to define classify_images
Code within the main() function within check_images.py indicated by #TODO: 3
Replace the first None within the function call to classify_images with in_arg.dir and replace the last None in the function call with in_arg.arch
Expected Outcome
When completed this code will return a dictionary of lists with the pet image filename as the key and the value will be a list for all 40 pet images in the pet_image folder. This list will contain the following items:

Pet image label (index 0)
Classifier label (index 1)
Comparison of labels (index 2)
Checking your code
The check_classifying_images function within check_images.py will check your code. This function will print out all the matches between the classifier and pet image labels and then all the non-matches between the labels.

Visually check that the results show:

Matches between Classifier and Pet Image Labels are real matches
Non-matches between Classifier and Pet Image Labels are real non-matches
The number of matches added to the number of non-matches totals 40, to account for all 40 images in pet_images folder
Project Workspace - Classifying Images
The next concept will have your workspace to work on #TODO: 3
Editing of check_image.py and classify_Images.py can be done within the Project Workspace - Classifying Images
For additional information and help on #TODO: 3, please look at the information below:
How to use the Classifier Function
Testing the classifier function
Test the environment and the classifier function that we will be using to classify the pet images. This function is located in the classifier.py program. Test your environment by running the test_classifier.py program following the instructions below. You can look at the test_classifier.py program to see how to use the classifier function within classify_images.py.

Go to the Lab Workspace - Classifying Images concept.
Open a terminal.
Type the following on the command line to test the classifier.py program. The image of the collie should be correctly classified as a collie.
python test_classifier.py 
Details on test_classifier.py
Look at the test_classifier.py program you will notice the following:

The classifier function has to be imported into your program (this is already done in classify_images.py).
The classifier function takes in two arguments:
The full image path (includes folder and filename).
Folder and filename stored as separate variables can be concatenated together into a single string.
The CNN model architecture.
Must be resnet, vgg or alexnet
To view the code of test_classifier.py open the program in the Project Workspace - Classifying Images.

Classifier Label Format for Label Matching
Your function will need to be able to determine matches between the pet image labels and the labels the classifier function returns. To be able to accomplish this matching task with your function, you will need to understand the format of the classifier labels. Below is a detailed description of the format of the classifier labels.

Classifier Labels
Labels are located in the file imagenet1000_clsid_to_human.txt that you will see in the project workspace.

Label Information:

1000 total labels
associated to 118 different dog breeds
dog breeds are associated to Ids 151: Chihuahua to 268: Mexican hairless
associated to 882 images that aren't dogs
label format:
a mixture of upper and lower case letters
a single word that identifies the image
Ex. beagle
multiple words separated by spaces that identify the image
Ex. German shorthaired pointer
a number of different terms separated by a comma (,) that all identify the same image
Ex. cocker spaniel, English cocker spaniel, cocker
Comparing Pet Image Labels to Classifier Labels
In the Creating Pet Image Labels concept we formatted the pet image labels to be:

Label composed of all lower case letters
Blank space separating each word in label composed of multiple words
Whitespace characters stripped from front & end of label
Examples:
beagle
cocker spaniel
polar bear
Looking at the classifier label format above, the only processing you will need to do is to put all the letters in lower case and to strip off any leading/trailing whitespace characters. The in operation can be used to determine if the pet image label matches one of the terms that compose the classifier label. The pet image labels are always only one term (even if multiple words make up that term). Therefore, if you discover (using the in operation) that your pet image label matches one term in the term (or terms) that make up a classifier label - then there's a match.

In the Lesson Data Types and Operators (of the Python lesson) you first learned about the string data type. To accomplish these formatting and matching tasks use the following string functions:

lower() - places letters in lower case only.
strip() - returns string with leading & trailing characters removed. If no characters are provided strips leading & trailing whitespace characters.
in operation - returns True when a string exists within another string, otherwise returns False.
Data Structure for Results
Compound Data Structures
In the lesson Data Types and Operators, you first learned about dictionaries. The get_pet_labels function returns a dictionary with the filenames as the keys and a list that contains only the pet image labels as the values. For the classify_images function, you can use the extend list function to add both the classifier label and the comparison to the results dictionary simultaneously.

In the lesson Data Types and Operators, you first learned about compound data structures. You created and used a nested dictionary to hold information about the elements. For the compound data structure, we recommend using a dictionary of lists(values). If you choose to use a different compound data structure the following check functions will not work:

check_creating_pet_image_labels
check_classifying_images
check_classifying_labels_as_dogs
check_calculating_results
The reason behind this choice of data structures is:

It's easier to access elements of the list using index values
You can use the sum() function with slicing to quickly classify the results
Computing the Results
For this function you will be inputing the results_dic dictionary that contains:

The filenames as keys
A list whose only item is the pet image label.
You will need to:

1) Iterate through this dictionary (results_dic) processing each pet image (filename) with the classifier function to get the classifier label.

2) Compare the pet image and classifier labels to determine if they match.

3) Add the results to the results dictionary (results_dic).

(In Mutable Data Types and Functions you learned that because the results dictionary is a mutable data type you don't need to return it from the classify_images function).

Coding recommendations to prevent issues with classify_images:

With the classifier function, be certain to concatenate the images_dir with the filename to represent the full path to each pet image file.
Put classifier labels in all lower case letters, stripping leading and trailing whitespace from the label.
results_dic will have the following format:
key = pet image filename (ex: Beagle_01141.jpg)
value = List with:
index 0 = Pet Image Label (ex: beagle)
index 1 = Classifier Label (ex: english foxhound)
index 2 = 0/1 where 1 = labels match , 0 = labels don't match (ex: 0)
example_dictionary = {'Beagle_01141.jpg': ['beagle', 'english foxhound', 0]}
To initialize a key in results_dic, use the assignment operator ( = ) to assigning the value of a list.
To add a single item to the list of an existing key in results_dic, append to the list using either += operator or the append function.
To add multiple items simultaneously to the list of an existing key in results_dic, use the extend list function.
For more details on using a dictionary of lists see the example code below. This demonstrates the difference between initializing a key-value pair and adding to the list of an existing key-value pair. The code also demonstrates how to iterate through a dictionary of lists to access each element of the list.

# Defining lists to populate dictionary 
filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_labels = ["walker hound, walker foxhound", "beagle",
                     "skunk, polecat, wood pussy"]
pet_label_is_dog = [1, 1, 0]
classifier_label_is_dog = [1, 1, 0]

# Defining empty dictionary
results_dic = dict()

# Populates empty dictionary with both labels &indicates if they match (idx 2)
for idx in range (0, len(filenames), 1):
    # If first time key is assigned initialize the list with pet & 
    # classifier labels
    if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [ pet_labels[idx], classifier_labels[idx] ]

    # Determine if pet_labels matches classifier_labels using in operator
    # - so if pet label is 'in' classifier label it's a match
    # ALSO since Key already exists because labels were added, append 
    # value to end of list for idx 2 
    # if pet image label was FOUND then there is a match 
    if pet_labels[idx] in classifier_labels[idx]:
        results_dic[filenames[idx]].append(1)

    # if pet image label was NOT found then there is no match
    else:
        results_dic[filenames[idx]].append(0)

# Populates dictionary with whether or not labels indicate a dog image (idx 3&4)
for idx in range (0, len(filenames), 1):
    # Key already exists, extend values to end of list for idx 3 & 4
    results_dic[filenames[idx]].extend([pet_label_is_dog[idx], 
                                       classifier_label_is_dog[idx]])

# Iterates through the list to print the results for each filename
for key in results_dic:
    print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",
          results_dic[key][2], "\nImage is dog=", results_dic[key][3],
          "\nClassifier is dog=", results_dic[key][4])                        

    # Provides classifications of the results
    if sum(results_dic[key][2:]) == 3:
        print("*Breed Match*")
    if sum(results_dic[key][3:]) == 2:
        print("*Is-a-Dog Match*")
    if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
        print("*NOT-a-Dog Match*")
