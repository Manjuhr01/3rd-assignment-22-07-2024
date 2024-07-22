# WAP to extract all the integers present in a list only if it is 
# present in odd i.

k=eval(input("enter a list:"))
i = 1  
r = []

while i < len(k):
        if isinstance(k[i], int):
            r.append(k[i])
        i += 2
print(r)