# wap to print all the char of a string present in a evem index without using slicing
mk=input("enter a string:") 
for i in range(len(mk)):
        if i % 2 == 1:
            print(mk[i], end=' ')