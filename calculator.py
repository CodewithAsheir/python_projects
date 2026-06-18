print("Simple Calculator")

a = float(input("First number:"))
b = float(input("Second number:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("choose option:")

if choice == "1":
    print("Answer:",a + b)

elif choice == "2":
    print("Answer:",a - b)

elif choice == "3":
    print("Answer:",a * b)

elif choice == "4":
    print("Answer:",a / b)

else:
    print("Wrong choice")