author__ = 'ajinkya'



def main():
    print("\nA Program that Prompts for a string of characters and outputs the checksum\n")

    message = input("Please Enter Your String To Make Digital Signature : ")    #Taking Input as string

    x=0                                                                         #Define variable x with value 0

    for chars in message:                                                        # For Loop through the message
                                                                                 #Using ord function to convert each character into its unicode value
        x=x+ord(chars)                                                          #Adding Each Converted Unicode Value and store in x

    print("\nHere is The Digital Signature for '",message,"' is :",x,"\n NOTE:\nThis is a Sum of Unicode i.e. Checksum")  # Display the Result Checksum of given string


main()

