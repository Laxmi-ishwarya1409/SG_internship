def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(3)
print(next(counter))  
print(next(counter))  
print(next(counter))  




def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)



def count_up_to(max):
    current = 1
    while current <= max:
        yield current
        current += 1

# Using the generator
for number in count_up_to(5):
    print(number)







def print_in_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        print(batch)

numbers = list(range(1, 11))  # [1 to 10]
print_in_batches(numbers, 3)




def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Usage
for batch in batch_generator(range(1, 11), 4):
    print(batch)



