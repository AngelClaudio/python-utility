# imaginary numbers are represented with 'j'
a = 2 + 3j
print(type(a))

# Another way to create complex numbers is using the complex function
a = complex(2, 3)
print(a)

# Arithmetic with imaginary numbers is normal
b = 3 + 3j
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# modulus and floor division are not valid for complex numbers

# complex numbers have 'real' and 'imag' attributes
print(a.real)
print(a.imag)

# comlex numbers also have a conjugate method
print(a.conjugate())

# to find the magnitude of complex numbers, use the abs function
print(abs(a))
print(13 ** .5)  # manually find sqr root of 13 to compare above results