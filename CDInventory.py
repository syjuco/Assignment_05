#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# SSyjuco, 2022-Feb-27, Modified file to replace inner rows with dicts, add the 'l' and 'd' functionalities
#------------------------------------------#

# -- DATA -- #
# Declare variables with the inner rows as dictionaries instead 

strChoice = '' # User input
lstTbl = []  # list of lists to hold data 
dicRow = {}  # list of data row now as dictionary instead 
strFileName = 'CDInventory.txt' # data storage file 
objFile = None # file object 

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data. THIS IS THE 'R' FUNCTION 
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': lstRow[0], 'Artist': lstRow[1], 'CD Title': lstRow[2]}
            lstTbl.append(dicRow) # simple way to read out the data from the text file as is. it seems to ignore data type. print(objFile.read())  
        print("read the following data from CDInventory.txt:") # added information to let the user know what was read from the file
        for row in lstTbl:
            print(*row.values(), sep = ',')
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data. NEED TO CHANGE THIS TO BE DICTIONARY
        strID = int(input('Enter an ID: '))
        strArtist = input('Enter the CDs Artist: ')
        strTitle = input('Enter the CDs Title: ')
        dicRow = {'id': strID, 'Artist': strArtist, 'CD Title': strTitle} #this defined the dictionary key: values
        lstTbl.append(dicRow)
        print('Added', dicRow, 'to the list.')
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID', 'Artist', 'Title')
        for row in lstTbl:
            print(*row.values(), sep = ',') # prints the values in each row from lstTbl 
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry. High level approach: turned the rows of text in CDInventory to items in a list to facilitate deletion by index. 
        objFile = open(strFileName, 'r')
        lines = objFile.readlines() # reads each line item in the file strFileName and converts each row into an item in a list called 'lines'
        print(lines) #shows the user the CDs in the text file to help them decide the CD to remove by inputting its index number on the list 
        kill = int(input('Select Index of the CD you want to remove from file. This is a list, and the first item is 0: '))
        lines.pop(kill) # removes the CD by referencing its index. this seems to leave a '\n' though in its place. 
        print(lines)
        objFile.close()
        objFile = open(strFileName, 'w')
        for row in lines: #writes the remaining items in the list 'lines' to the file without the removed CD
            strRow =''
            strRow += str(row) + ','
        strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
        print('The following CDs remain in the file CDInventory.txt')
        for row in lines:
            print(row)
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')  # using option 'a' to add data to file instead of 'w' to add multiple files 
        for row in lstTbl:
            strRow = ''
            for item in row.values(): # this is the line that allowed the data to be written to the text file properly 
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        print('Added the following to the file CDInventory.txt') # this line and next 2 lines shows the user what was added to the text file 
        for row in lstTbl: 
            print(*row.values(), sep = ',') #needed to print row.values() to get the values to print and not the keys
        objFile.close()
    
    else:
        print('Please choose either l, a, i, d, s or x!')

