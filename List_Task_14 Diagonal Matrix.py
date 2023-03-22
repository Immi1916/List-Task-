# Write a program that asks for an integer n,
# then it creates a two-dimensional array (of integers) of the specified
# size (nxn) with the value of 1 on the main diagonal and the value of 0
# everywhere else. Print the 2d array into the output
# Example:
# Please enter the array (matrix) size: 4
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

Matirx =int(input("Enter the Parameter "))
for a in range(Matirx):
    for b in range(Matirx):
        if a==b:
            print(1,end="")
        else:
            print(0,end="")
    print()
