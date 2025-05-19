# Create a frequency counter for words in a text
    
frequency_counter = {}
text = input("Enter your text: ")
words = text.split()
for word in words:
    word = word.lower()
    if word in frequency_counter:
        frequency_counter[word] += 1
    else:
        frequency_counter[word] = 1

print("Word Frequencies:")
for word, count in frequency_counter.items():
    print(f"{word}:{count}")