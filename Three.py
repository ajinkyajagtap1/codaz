author__ = 'ajinkya'

def main():
    print("Hello")
    fname=input("Enter File Name(example:'Summery.txt'):")                                                             #Taking File name from User ,TEXT file as "test.txt"
    fh=open(fname,"w")                                                                                              #file is open and writing in file,fh is a counter
    print(""                                                                                              #write all data on specified file
          "\n""I am Ajinkya Jagtap,Computer Engineering Master’s Graduate"
	      "\nI recently completed my Master’s degree in Computer Engineering"
          "\nI am looking for an entry level engineer position."
          "\nI have a strong background in computer engineering, Electrical and Programing languages like c,c++,Python,Java."
          "\nI am keenly interested in working for a firm where I can learn, innovate, and contribute to the challenging real-time happening engineering projects."
          "\nI always believe in learning via practical hands-on training."
          "\nI did many small but effective class projects where I can illustrate my knowledge."
          "\nI am also doing voluntary work in VR modules. "
          "\nI will enjoy working in areas like design, development and testing of software and hardware entities." 
          "\nI would appreciate if you could spare some time to discuss in detail. "
          "\nemail address (ajinkya.jagtap@maine.edu). "
          "\nI would be interested in showing some of my previous works and sharing some experiences from the projects that I have completed." 
          "\nI have attached my resume for your kind perusal. Please find the attachment."
          "\nThank you for the consideration,\n" 
          "\nSincerely, "
          "\nAjinkya",file=fh)                                                                    #All this So you can check on your system with any file name,but make sure it is a text file
    cchar = input("Please Enter the Character you want to Calculate:")                            #Taking input From User for specific word or string or number
    char = cchar.lower()                                                                         #Converting Given word in lower case as python is case sensitive
    fh=open(fname,"r")                                                                            #Now read the same file
    data=fh.read().lower().count(char)                                                           #Data store output of functions,here we read file in lower case and count given input appears
    print("\nProgram Read the File",fname,"where'",cchar,"'is Appears",data,"time.")             #print the Total Number given word appears
    fh.close()                                                                                    #file close
main()