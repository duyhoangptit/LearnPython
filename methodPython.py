# method python
def num_vowels(string):
    s = string.lower()
    count = 0
    for c in s:
        if c in ('a','e','i','o','u'):
            count +=1
    return count


str = input("Enter a statement: ")
print("The number of vowels is: ", num_vowels(str),".")
