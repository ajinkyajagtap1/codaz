author__ = 'ajinkya'

def main( ) :
    print("A program that can report the number of times a certain letter appears in a string.")
    inString = input("\nPlease Enter Your String: ")  # Taking Input As string from User
    if inString.isalpha():                              #If condition to check weather input is string or not using isalpha function(very useful of this code)
        inString=inString.lower()                       #Converting User input in lower case string as python is case sensitive
        cchar= input("Now please enter your latter: ")  # Taking Input from user for latter
        cchar=cchar.lower()                             #here also converting input latter in lower case
        x=inString.count(cchar)                         #Created new variable x to store result for simplification
        print("\nTotal Number of Times" ,"''",cchar,"''","Appears = ",x)# print the output as number of times latter appears in string
    else:
            print("Input is not string \n Try Again")   #Print the error message
main()