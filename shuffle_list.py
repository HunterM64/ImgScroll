import os
import random

def shuffle_list(list):
    random.shuffle(list)
    return list

if __name__ == "__main__":
    list1 = os.listdir('./static/images')
    print(list1)
    list2 = shuffle_list(list1)
    print()
    print(list2)