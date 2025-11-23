# Swapping of Two Numbers

# Method - 1
a = 5
b = 10
print(a, b) # 5 10
a, b = b, a
print(a, b) # 10 5

# Method - 2 (Universal Swapping Method)
c = 2
d = 15
print(c, d) # 2 15

temp = c;
c = d;
d = temp;
print(c, d) # 15 2

# Method - 3 (Without any variable)
n1 = 20
n2 = 30
print(n1, n2)

n1 = n1 + n2;
n2 = n1 - n2;
n1 = n1 - n2;
print(n1, n2)

# Method - 4 (Without any variable)
num1 = 200
num2 = 300
print(num1, num2)

num1 = num1 * num2;
num2 = num1 / num2;
num1 = num1 / num2;
print(num1, num2)
















