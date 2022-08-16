
import re


def NarrowRange(nums, target):
    # We are finding out the starting and last index of required words only by BINARY SEARCH
    # Example Input word = zoo
    # We will find out all the indices of the words starting with Z from our LIST.TXT
    result = [-1, -1]
    result[0] = findStartingIndex(nums, target)
    result[1] = findEndingIndex(nums, target)

    return result


def findStartingIndex(nums, target):
    index = -1
    low, high = 0, len(nums) - 2

    while low <= high:
        mid = low + (high - low)//2
        if ord(nums[mid][0]) == ord(target[0]):
            index = mid
            high = mid - 1
        elif ord(nums[mid][0]) > ord(target[0]):
            high = mid - 1
        else:
            low = mid + 1

    return index


def findEndingIndex(nums, target):
    index = -1
    low, high = 0, len(nums) - 2
    while low <= high:
        mid = low + (high - low)//2
        if ord(nums[mid][0]) == ord(target[0]):
            index = mid
            low = mid + 1
        elif ord(nums[mid][0]) > ord(target[0]):
            high = mid - 1
        else:
            low = mid + 1
    return index
# We are using BINARY SEARCH to reduce the time complexity to O(Logn)


word_List = open(ENTER_FILE_PATH,
                 "r")  # Enter the path of List.Txt

List = word_List.read()

Dictionary = List.split("\n")

# We have converted the given data text file into Array data structures.

Search_word = input("Enter the word: ")
count = 0
# We are keeping the count of resemble words to handle corner case of having no matching word

final_range = NarrowRange(Dictionary, Search_word)

Narrow_list = Dictionary[final_range[0]:final_range[1]+1]
# We have created new list with the generated starting and ending index to narrow are search range

if len(Search_word) < 1:
    # To find input entered is empty
    print("Input is Empty")
elif re.sub(r'(?:[^\W\d]+\d|\d+[^\W\d])[^\W]*|[^\W\d]+', '', Search_word):
    # To find input entered contains special character and numbers
    print("Special Characters and Numbers not allowed")
else:
    for word in range(len(Narrow_list)):
        if Search_word in Narrow_list[word] and Search_word[0] == Narrow_list[word][0]:
            print(Narrow_list[word])
            count += 1
    if count == 0:
        print("Sorry word does not exist")

# TIME COMPLEXITY
# We have used BINARY SEARCH twice so the time complexity becomes
# 2*O(Logn) which is equal to O(Logn)
# After that we have used a for-loop to find all the matching words
# So the final TIME COMPLEXITY BECOMES O(Logn+X)
# Where X is the length of Narrowed List(Narrow_list).


# SPACE COMPLEXITY
# We have used BINARY SEARCH so the space complexity becomes O(1).
# We converted the list.txt Into Array Data Structures which have space Complexity of O(n).
# Where n is the length of the Array.
# we created new Narrowed List which have length X
# So the space complexity becomes O(X)
# Calculating the Final Space Complexity
# O(1)+O(n)+O(X) which is equal to O(n+X)
