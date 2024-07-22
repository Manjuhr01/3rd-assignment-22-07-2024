# WAP to extract all the special characters present in string only
# if the ASCII value of the character is even and palindrome.
m=input('string:')
i = 0
special_chars = ""

while i < len(m):
        char = m[i]
        av = ord(char)

        if not m.isalnum() and av % 2 == 0:
            if char[::-1]==m[-1]:
                special_chars += char

        i += 1

print(special_chars)