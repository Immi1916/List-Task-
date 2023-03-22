# - Create a variable named `firstArrayOfNumbers`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `secondArrayOfNumbers`
#   with the following content: `[4, 5]`
# - Print "secondArrayOfNumbers is longer" if `secondArrayOfNumbers` has more
#   elements than `firstArrayOfNumbers`
# - Otherwise print: "firstArrayOfNumbers is the longer one"
FirstArrayOfNumbers = [1, 2, 3]
SecondArrayOfNumbers = [4, 5]
if len(SecondArrayOfNumbers) > len(FirstArrayOfNumbers):
    print("SecondArrayOfNumbers has more element")
else:
    print("FirstArrayOfNumbers is longer one")
