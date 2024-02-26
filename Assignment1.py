def large(num_list):
    l=max(num_list)
    s=min(num_list)
    return l,s
num=[21,90,45,3,5,1,99]
l,s=large(num)
print("Largest of List = ",l)
print("Smallest of List = ",s)   