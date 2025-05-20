# Create a text analyzer that counts characters, words, and performs various string operations.

text = "Python is a powerful and versatile programming language that is widely used in many different fields. From web development to data science, Python offers a clean and readable syntax that makes it ideal for both beginners and professionals."

text2 = "One of the key strengths of Python is its vast collection of libraries and frameworks, which provide support for everything from machine learning and data analysis to game development and automation. Whether you are building a simple script or a complex application, Python helps you get things done quickly and efficiently."

# counting the characters
print(len(text))

# counting the words
words = text.split()
# print(words)
print(len(words))

# Concatenation
print(text+text2)
print(text,text2)

# Repetition
greet = "Hello!"
repeated_text = greet * 3  
print(repeated_text)  

# membership
print("Python" in text)  
print("java" in text)   

print("Python" not in text) 
print("java" not in text)    


# slicing
print(text[0:5])
print(text[7:13])
print(text[:])
print(text[::2])
print(text[-1])
print(text[-6:-1])
print(text[:5])
print(text[7:])
print(text[-2:])     # prints last 2 elemnts
print(text[:-2])     # start from beginning and ends at -2 element



# checking string case
text = "HELLO"
print(text.isupper())  

text = "hello"
print(text.islower()) 

text = "Hello World"
print(text.istitle())  


# replacing characters
text = "apple, banana, cherry"
print(text.replace(",", "|"))  

# strip
text = "   Hello, Python!   "
cleaned = text.strip()
print(cleaned)  