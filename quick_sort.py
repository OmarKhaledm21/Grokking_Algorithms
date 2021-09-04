def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <=pivot]
        greater = [i for i in arr[1:] if i>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)


def quicksortBetter(arr):
    if len(arr) < 2:
        return arr
        
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortBetter(left) + middle + quicksortBetter(right)


def main():
    print(quicksortBetter([10, 5, 2, 3]))


if __name__=="__main__":
    main()