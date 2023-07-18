# Write a RemoveDuplicates() function 
# which takes a list sorted in increasing order and deletes any duplicate nodes from the list. 
# Ideally, the list should only be traversed once. 
# The head of the resulting list should be returned.


def RemoveDuplicates(arr):
    if len(arr) == 0:
        return 'null'
    return list(set(arr))

print(RemoveDuplicates([1,2,3,3,4,4,5,'null']))
print(RemoveDuplicates([]))
