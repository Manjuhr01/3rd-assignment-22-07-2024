##13. WAP to find product of all the floating number present in a 
##tuple collection.
k=eval(input("enter a tupple coll:"))
result = 1
index = 0

while index < len(k):
        if isinstance(k[index], float):
            result *= k[index]
        index += 1
print(result)
