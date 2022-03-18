#TODO: 4: Classifying Labels as Dogs
Implement the adjust_results4_isadog() function to adjust the results of dictionary(result_dic) to determine if the classifier correctly classified images as 'a dog' or 'not a dog'.

Coding within the check_images.py and adjust_results4_isadog.py
Code to Edit
This section will help you code the undefined function adjust_results4_isadog within adjust_results4_isadog.py.

With this function you will:

Read in the dog names from dognames.txt file into a data structure (like a dictionary)
Compare the dog names to the classifier and pet image labels in the results dictionary
Adjust the results dictionary to indicate whether or not these labels indicate the image is 'of-a-dog'.
Note that the adjust_results4_isadog function will change the results dictionary, but because dictionaries are mutable you won't have to return this dictionary (review the section Mutable Data Types and Functions if you want a more detailed explanation).
Code for the function definition def adjust_results4_isadog(): as indicated by #TODO: 4 within adjust_results4_isadog.py.
Using the comments and docstring within adjust_results4_isadog.py to define adjust_results4_isadog
Code within the main() function within check_images.py indicated by #TODO: 4
Replace None within the function call to adjust_results4_isadog with in_arg.dogfile.
Expected Outcome
When completed this code will have altered the results dictionary (a dictionary of lists) with the pet image filename as the key and the value will be a list for all 40 pet images in the pet_image folder. This list for each key will now contain two additional items: whether the pet image label is of-a-dog (index 3) and whether the classifier label is of-a-dog (index 4).

Checking your code
The check_classifying_labels_as_dogs function within check_images.py will check your code. This function will print out all the matches between the classifier and the pet image labels and all the non-matches between the labels.

Visually check that the results show:

Matches between Classifier and Pet Image Labels have both labels classified as "dogs" or "not dogs" as appropriate for the labels.
Non-matches between Classifier and Pet Image Labels correctly classify each label as "dogs" or "not dogs"
The number of matches added to the number of non-matches totals 40, to account for all 40 images in pet_images folder.
Project Workspace - Adjusting Results
The next concept will have your workspace to work on #TODO: 4
Editing of check_image.py and adjust_results4_isadog.py can be done within the Project Workspace - Adjusting Results
For additional information and help on #TODO: 4, please look at the information below:
Define: "Is a Dog" / "Is NOT a Dog" by Reviewing Dog Names File
Let's remember the principle objectives _1_ and _2_:
Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.
Correctly classify the breed of dog for the images that are of dogs.
To achieve objectives 1 and 2, your program will have to be able to identify if labels from both the classifier function and the pet images are of "a dog" or "not a dog". To be able to classify the labels as "dogs" or "not dogs", your program will need to compare the labels to the list of dogs contained in the dognames.txt file in the workspace.

This dognames.txt file was created from the formatted labels (lower case, whitespace trimmed, etc.). Therefore, when comparing dog names (from dognames.txt) to your labels:

if there is a match between dog name and label, the label "is a dog"
if there isn't a match between dog name and label, the label "is not a dog"
Details about dognames.txt:
There are:

One dog breed name per line
223 dog breeds named
All possible dog breeds that can come from the classifier function and pet image labels
Classifier Function Labels:
Lines 1 (chihuahua) to 118 (Mexican hairless): These should match classifier returned labels as long as those labels are in all lower case letters and have whitespace characters trimmed from the ends.
Pet Image Labels:
Should match the following lines as long as the labels are in all lower case letters, whitespace has been trimmed from the ends, and there is a single space separating the words of a dog's name (if it's composed of multiple words).
Reading In Dogsname.txt
The first task of the adjust_results4_isadog will be to read in all the dog names and store them in a data structure. Given the details above, the most ideal data structure for our dog names is a dictionary with the key as the dog name and a value of 1 (arbitrary value). The reasoning behind this choice is the speed of the look-up of a dictionary. Since we know the labels should match the dog name exactly if there is a match; we can simply look for the label as a key within the dog names dictionary to discover all labels that are dogs. If the label isn't found as a key in the dog names dictionary, then we know that label is not a dog.

In the lesson Scripting, we demonstrated how to open and read information from a file. Please review this section if you are having difficulty reading the dog names from dognames.txt.

Coding recommendation as to prevent issues with adjust_results4_isadog:

Define the dognames_dic prior to opening the dognames.txt file for reading
Use rstrip() to strip off newline characters from each line read from dognames.txt
If a dog name already exists in dognames_dic print a Warning statement because you shouldn't find any duplicate dog names in dognames.txt
Adjusting Results Dictionary
Once you have read the dog names into dognames_dic, you will need to adjust the results dictionary (results_dic) to account for when labels were correctly or incorrectly classified as dogs.

Review section Classifying Labels as Dogs to review how to iterate through the results dictionary to append values onto the list that is the value for each key in the results dictionary. If you want to append both values at the same time, you will need to use the extend list function to add both index 3 and index 4 to the results_dic simultaneously.

results_dic will have the following adjusted format:

key = pet image filename (ex: Beagle_01141.jpg)
value = List with:
index 0 = Pet Image Label (ex: beagle)
index 1 = Classifier Label (ex: english foxhound)
index 2 = 0/1 where 1 = labels match , 0 = labels don't match (ex: 0)
index 3 = 0/1 where 1= Pet Image Label is a dog, 0 = Pet Image Label isn't a dog (ex: 1)
index 4 = 0/1 where 1= Classifier Label is a dog, 0 = Classifier Label isn't a dog (ex: 1)
example_dictionary = {'Beagle_01141.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1]}
