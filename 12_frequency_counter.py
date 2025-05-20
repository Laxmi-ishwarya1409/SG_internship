# Create a frequency counter for words in a text
def frequency_counter(): 
    try:  
        frequency_counter = {}
        text = input("Enter your text: ").strip()

        if not text:
            raise ValueError("Input cannot be empty.")
        
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

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

frequency_counter()