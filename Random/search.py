# search word on dBase.txt



wordToSearch = input(str("Any: "))

with open(r'dBase.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if word is present
        if line.find(wordToSearch) != -1:
            print(wordToSearch, 'txt exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)