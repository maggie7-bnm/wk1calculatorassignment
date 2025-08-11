num1 = float (input("Enter First Number"))
num2 = float (input("Enter Second Number"))
operator = input("Enter operation (+,-,*,/): ")
if operator == '+':
   result = num1 + num2

elif operator == '-':
   result = num1 - num2

elif operator =='*':
   result = num1 * num2

elif operator =='/':
   if num2 != 0:
      result = num1 / num2
   else:
     result = "Error! Division by zero"
else:
   result = "Invalid operation"
print(f"{num1} {operator} {num2} = {result}" )
