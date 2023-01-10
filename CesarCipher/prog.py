def cesarCipher(message, key, mode):
    newMessage = ""

    for i in range(len(message)):

        if str.isupper(message[i]):
            newMessage += chr((ord(message[i]) + (mode)*key - ord("A")) % 26 + ord("A"))
        elif str.islower(message[i]):
            newMessage += chr((ord(message[i]) + (mode)*key - ord("a")) % 26 + ord("a"))
        elif str.isdigit(message[i]):
            newMessage += chr((ord(message[i]) + (mode)*key - ord("0")) % 10 + ord("0"))
        else:
            newMessage += message[i]

    return newMessage

def help():
    print("Welcome to the Cesar Cipher!")
    print("This program will encrypt or decrypt a message using the Cesar Cipher.")
    print("")
    print("Message: The message you want to encrypt/decrypt.")
    print("Key: The key you want to use to encrypt/decrypt the message.")
    print("Mode: 1 for encrypt, -1 for decrypt.")
    print("")
    print("Example: 'Hello, Siemens' with key 3 and mode 1 will return 'Khoor, Vlhphqv!'.")
    print("")
    print("Type '-exit' to exit the program.")

def main():
    help()

    while True:

        message = input("Enter the message: ")
        if message == "-exit":
            break

        key = (input("Enter the key: "))
        try:
            key = int(key)
        except:
            print("Invalid key!")
            break

        mode = (input("Enter the mode: "))
        try:
            mode = int(mode)
        except:
            print("Invalid mode!")
            break
        if mode != 1 and mode != -1:
            print("Invalid mode!")
            break


        print(cesarCipher(message, key, mode))

main()

        