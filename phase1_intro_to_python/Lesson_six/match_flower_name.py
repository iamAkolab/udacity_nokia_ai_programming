# function that creates a flower_dictionary from filename

def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()

#------------------------------------------------------------------------------------------------------------------------------------
""""
flowers.txt
A: African Daisy
B: Bellflower
C: Coral Bells
D: Desert Rose
E: English Bluebell
F: Forget Me Not
G: Goldenrod
H: Heliotrope
I: Impatiens
J: Jamesia americana
K: Kangaroo Paw
L: Lily of the Valley
M: Monks Hood
N: Nemophila
O: Ox Eye Daisy
P: Peace Lily
Q: Quaker Ladies
R: Rain Lily
S: Snapdragon
T: Trumpet Vine
U: Urn Plant
V: Viola wittrockiana
W: Whirling Butterflies
X: Xanthoceras sorbifolium
Y: Yellow Archangel
Z: Zinnia elegans
""""
