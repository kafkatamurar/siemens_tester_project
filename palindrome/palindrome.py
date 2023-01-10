print("Welcome to the palindrome checker! Type '-exit' to exit the program.")
while True:
    string_inupt = input("Enter a string: ")
    reversed = string_inupt[::-1]

    if string_inupt == "-exit":
        break

    if string_inupt == reversed:
        print("The string is a palindrome. Type '-exit' to exit the program.")
    else:
        print("The string is not a palindrome. Type '-exit' to exit the program.")