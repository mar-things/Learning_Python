# try at home to make it work 


f = open("Data.txt","r")
lines = f.readlines()
count = 0 


for line in lines:
    words = line.split()
    for i in words:
        for digit in i:
            if(digit.isdigit()):
                
                print(number)




f.close() 