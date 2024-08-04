#This code produces the multiplication table for any chosen number
n = int(input("Enter the number whose multiplication table you're looking for: "))
print(f"\nThe multiplcation table for {n} is\n")
for i in range(1, 13):
    print(f"{n} x {i} = {n * i} \n")
print("Hello World\n")

multiples =[]
for k in range(1,101):
    if k % 3 == 0:
        multiples.append(k)
print(F" {multiples} is a list of multiple of 3")
