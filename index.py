#This code produces the multiplication table for any chosen number
N = int(input("Enter the number whose multiplication table you're looking for: "))
print(f"\nThe multiplcation table for {N} is\n")
for i in range(1, 13):
    print(f"{N} x {i} = {N*i}")
print("Thank you\n")
print("Hello World\n")

multiples =[]
for i in range(1,101):
    if i % 3 == 0:
        multiples.append(i)
print(F" {multiples} is a list of multiple of 3")