#  WAP to store the factors of a integer number in a tuple.
# Ex1: n = 6
# o/p = [1,2,3,6]
# Ex2: n=20
# o/p = [1,2,5,10,20]
Tuple=eval(input("enter a tup coll:"))
factors = []
i = 1

while i <= Tuple:
        if Tuple % i == 0:
            factors.append(i)
        i += 1
print(factors)