class convtostr:
    def return42():
        print( "Geeks 4 Geeks !")
    
# convert list of input to string using map
    def joinStr(x):         
        output =''.join(map(str,x))
        print("output type", type(output))
        print("from function")
        return output
    
# find string
    def findStr(str):
        strToFind = input(str)
        with open(r'dBase.txt', 'r') as fp:
        # read all lines in a list
            lines = fp.readlines()
            for line in lines:
        # check if word is present
                if line.find(strToFind) != -1:
                    print(strToFind, 'txt exists in file')
                    print('Line Number:', lines.index(line))
                    print('Line:', line)
        return
    
    def searchstr(inPut):
        with open(r'dBase.txt', 'r') as fp:
        # read all lines in a list
            lines = fp.readlines()
            for line in lines:
        # check if word is present
                if line.find(inPut) != -1:
                    print(input, 'txt exists in file')
                    print('Line Number:', lines.index(line))
                    print('Line:', line)
                    return
                
                
    def 