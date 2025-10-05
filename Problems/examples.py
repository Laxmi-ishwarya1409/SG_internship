def chunk(lst: list, size: int) -> list[list]:
    result = []
    if not lst:
        return []
    elif size == 0:
        raise ValueError
    elif size >len(lst):
        result.append(lst)
        return result
    else:
        for i in range(0,len(lst),size):  
            slice = lst[i:i+size]
            result.append(slice)
        return result


print(chunk([1,2,3,4,5], 2))
print(chunk([1,2,3,4,5,47,89], 3))
print(chunk([1,2,3,4,5], 10))
# # print(chunk([1,2,3,4,5], 0))





def freq_count(lst: list) -> dict:
    result = {}
    for i in lst:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

print(freq_count([1, 2, 1, 3]))
print(freq_count([1, 2, 1, 3, 2, 2, 4, 5, 7, 1, 4, 5]))
print(freq_count(["a","b","a","c"]))






def running_avg(lst: list[float]) -> list[float]:
    result = []
    total = 0
    for i in range(len(lst)):
        total += lst[i]     # total = 0 + 1 = 1
        average = total / (i + 1)   # average = 1 /(0+1) = 1/1 = 1
        result.append(average)
    return result

print(running_avg([1, 2, 3, 4])   ) #  [1, 1.5, 2, 2.5]
print(running_avg([10, 10, 10]))
print(running_avg([]))








# linear search
def linear_search(lst, target):
    for i in range(len(lst)):          
        if lst[i] == target:  
            return i                  
    return -1       

numbers = [10, 20, 30, 40, 50]
target = 30

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")








def linear_search(lst, target):
    indices = []         
    for i in range(len(lst)):
        if lst[i] == target:
            indices.append(i)
    return indices           


numbers = [2, 4, 6, 4, 8, 4]
target = 4

result = linear_search(numbers, target)

if result:
    print(f"Element found at indexes: {result}")
else:
    print("Element not found")







# binary_search
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2 

        if lst[mid] == target:
            return mid          
        elif lst[mid] < target:
            low = mid + 1         
        else:
            high = mid - 1        

    return -1             




numbers = [1, 3, 5, 7, 9, 11, 13]
target = 9

result = binary_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")