def factorial(num):
    if num <=1:
        return 1
    else:
        return num*factorial(num-1)


def sum(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0]+sum(arr[1:])


def count(list):
    if list ==[]:
        return 0
    return 1+ count(list[1:])


def max(list):
    if len(list)==2:
        return list[0] if list[0]>list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0]>sub_max else sub_max


def main():
    print(factorial(5))


if __name__ == "__main__":
    main()