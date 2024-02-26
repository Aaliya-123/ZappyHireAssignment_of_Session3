def swap(a,b):
    return b,a

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("Original Value a =",a,"b =",b)
a,b=swap(a,b)
print("Swapped Value a =",a,"b =",b)