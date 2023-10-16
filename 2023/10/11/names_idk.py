names = ["ben","dover","bangding","ow","sumting","wong"]

# define a function to sort the list
def alphabetical_sort(lst):
    # create an empty list to store the sorted names
    sorted_lst = []
    # define alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # loop through each letter in the alphabet
    for letter in alphabet:
        # loop through each name in the list
        for name in lst:
            # if the first letter of the name matches the current letter in the alphabet
            if name[0] == letter:
                # add the name to the sorted list
                sorted_lst.append(name)
    # return the sorted list
    return sorted_lst

# call the function to sort the names list
names = alphabetical_sort(names)
print(names)
