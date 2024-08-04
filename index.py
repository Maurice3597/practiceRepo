#This code produces the multiplication table for any chosen number
N = int(input("Enter the number whose multiplication table you're looking for: "))
print(f"\nThe multiplcation table for {N} is\n")
for i in range(1, 13):
    print(f"{N} x {i} = {N*i}")
print("Thank you")
print("Hello World")
