# Doubts raised.
num = int(input("Enter a number : "))
lastDigit = (num%10)*2
num = (num//10)*10 + lastDigit
print(num)
