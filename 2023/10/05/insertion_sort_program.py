from timeit import default_timer as timer

start = timer()
def insertion_sort(items):
    # Initialise the variables
    num_items = len(items)

    # Repeat for each item in the list, starting at the second item
    for index in range(1,num_items):
        # Get the value of the next item to insert
        item_to_insert = items[index]
        
        # Get the current position of the last sorted item
        position = index - 1
        print(items)
        # Repeat while there are still items in the list to check
        # and the current sorted items is greater than the item to insert
        while position >= 0 and items[position] > item_to_insert:
            # Copy the value of the sorted item up one place
            items[position + 1] = items[position]
            position = position - 1
        items[position + 1] = item_to_insert
    return items
print("running...")

cards = [0,2,69,5,4,3,9,7,10,6,8]


print(insertion_sort(cards))
end = timer()
print(end - start)