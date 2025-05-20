# Experiment with different data types and conversions.

x = 1
y = 1.456
z = complex(5,9)
z1 = complex(5,9.258)
p = "123"
p1 = "ish"


a = float(x)
b = int(y)
# b1 = int(z)     # int() argument must be a string, a bytes-like object or a real number, not 'complex'
d = complex(y)
b2 = int(p)
a1 = float(p)
# c = int(p1)   # int() argument must be a string, a bytes-like object or a real number, not 'complex'
f = str(y)



print(type(a))
print(type(b))
print(type(d))
print(type(b2))
print(type(a1))
print(type(f))