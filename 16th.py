#  Consider a homogenous tuple and divide the input into two 
# outputs of even number and odd number
q=eval(input("enter a tuple coll:"))
eve_num = []
odd_num = []
i = 0

while i < len(q):
        if q[i] % 2 == 0:
            eve_num.append(q[i])
        else:
            odd_num.append(q[i])
        i += 1
        
print(f"Even numbers: {eve_num}")
print(f"Odd numbers: {odd_num}")