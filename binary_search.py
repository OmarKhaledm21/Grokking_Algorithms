from typing import Counter


def binary_search(list, item):
    counter=0
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            print("\n\n\nresult:")
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        counter+=1
        print(counter)

    return None


def main():
    my_list = [1,2, 3,4, 5,6, 7,8, 9]
    print(binary_search(my_list, 9))



if __name__=="__main__":
    main()


