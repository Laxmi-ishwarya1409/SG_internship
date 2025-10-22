class MyCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value

counter = MyCounter(1, 3)
for num in counter:
    print(num)




def print_in_batches(data,batch_size):
    for i in range(0, len(data),batch_size):
        batch = data[i:i+batch_size]
        print(batch)

numbers = list(range(1,11))
print_in_batches(numbers,3)






class EvenNumberBatchIterator:
    def __init__(self,iterator,batch_size):
        self.iterator = iterator
        self.batch_size = batch_size


    def __iter__(self):
        return self
    
    def __next__(self):
        batch = []
        for i in range(self.batch_size):
            if i % 2 == 0:
                batch.append(i)
        return batch
    
numbers = range(1,11)
batch_iter = EvenNumberBatchIterator(numbers,3)
for batch in batch_iter:
    print(batch)