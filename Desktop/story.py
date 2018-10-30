import xlrd

'''
Gets the filepath for excel sheet, File should be excel, it takes path of file
'''
def getFilePath():
    fileLocation = input("\n Enter path to your file and press 'Enter' e.g. C:/Users/Ultrabook/Desktop/story1/hardware.xlsx: ")
    # loc = "C:/Users/Ultrabook/Desktop/story1/hardware.xlsx"
    return fileLocation

'''
Calculate the number of rows in sheet 
@param fileLocation - Location of file
'''
def getRowCount(fileLocation):
    sheet = getSheet(0, fileLocation)
    numOfRows = sheet.nrows
    return numOfRows
'''
Calculate the number of columns in sheet
@param fileLocation - Location of file
'''
def getColumnCount(fileLocation):
    sheet = getSheet(0, fileLocation)
    numOfColumns = sheet.ncols
    return numOfColumns
'''
Returns the sheet for corresponding sheetnumber and filelocation
@param sheetNumber - sheet number
@param fileLocation - Location of file
'''
def getSheet(sheetNumber, fileLocation):
    wb = getWorkbook(fileLocation)
    sheet = wb.sheet_by_index(sheetNumber)
    return sheet

'''
Return the workbook
@param fileLocation - Location of file
'''
def getWorkbook(fileLocation):
    return xlrd.open_workbook(fileLocation)

'''
This method is used for get all the list of attributes in the list
@param columnCount - number of columns in a sheet
@param sheet - current workskeet 
'''
def getAllHeadings(columnCount, sheet):
    headings = []
    print("The list of columns  are ")
    for head in range(columnCount):
        headings.append(sheet.cell(0, head).value)
    return headings

'''
Used to get all the attributes in department/group column
@param row - row number of the group
@param column - column number of the group
@param rowCount - number of columns in a sheet
@param sheet - current workskeet 
'''
def getAllDepartments(row, column, rowCount, sheet):
    return getAllRows(row, column, rowCount, sheet)


'''
Used to get all the attributes in Application
@param row - row number of the group
@param column - column number of the group
@param rowCount - number of columns in a sheet
@param sheet - current workskeet 
'''
def getAllApplication(row, column, rowCount, sheet):
    return getAllRows(row, column, rowCount, sheet)

'''
Used to get all the attributes in DataCenter
@param row - row number of the group
@param column - column number of the group
@param rowCount - number of columns in a sheet
@param sheet - current workskeet 
'''
def getAllDataCenter(row, column, rowCount, sheet):
    return getAllRows(row, column, rowCount, sheet)

'''
Used to get all the rows in Department/group
@param row - row number of the group
@param column - column number of the group
@param rowCount - number of columns in a sheet
@param sheet - current workskeet 
'''
def getAllRows(row, columns, rowCount, sheet):
    rowsMap = {}
    for row in range(1, rowCount):
        key = sheet.cell(row, columns).value
        if key not in rowsMap.keys():
            rowsMap[key] = 0
        rowsMap[key] += 1
    return rowsMap

'''
Used to get number of applications in each department
@param sheet - current worksheet
@rowCount - total number of rows
'''
def getApplicationsForEachDepartment(sheet, rowCount):
    result = {}

    for row in range(1, rowCount):
        groupKey = sheet.cell(row, 0).value
        applicationKey = sheet.cell(row, 5).value
        if (groupKey in result.keys()):
            if (applicationKey not in result[groupKey].keys()):
                result[groupKey][applicationKey] = 0
            result[groupKey][applicationKey] += 1
        else:
            applicationMap = {}
            applicationMap[applicationKey] = 1
            result[groupKey] = applicationMap
    return (result)

'''
Used to get the number of CPUs and memory used by each department
@param columName - column name of the group
@param sheet - current workskeet 
@param rowCount - total number of rows
@param column - column number of group
'''
def getGroupCpuRamMap(columName, sheet, rowCount, column):
    return getColumnToColumnMap(columName, sheet, rowCount, column)

'''
Used to get the number of CPUs and memory used by each Application
@param columName - column name of the group
@param sheet - current workskeet 
@param rowCount - total number of rows
@param column - column number of group
'''
def getApplicationCpuRamMap(columName, sheet, rowCount, column):
    return getColumnToColumnMap(columName, sheet, rowCount, column)

'''
Used to get the number of CPUs and memory used by each Application
@param columName - column name of the group
@param sheet - current workskeet 
@param rowCount - total number of rows
@param column - column number of group
'''
def getDataCenterCpuRamMap(columName, sheet, rowCount, column):
    return getColumnToColumnMap(columName, sheet, rowCount, column)


'''
Used to get the number of CPUs and memory used by each column passed
@param columName - column name of the group
@param sheet - current workskeet 
@param rowCount - total number of rows
@param column - column number of group
'''
def getColumnToColumnMap(columName, sheet, rowCount, column):
    result = {}
    cpuMap = {}
    ramMap = {}

    for row in range(1, rowCount):
        appKey = sheet.cell(row, column).value
        cpuKey = sheet.cell(row, 6).value
        ramKey = sheet.cell(row, 7).value

        if (appKey == columName):
            if (appKey in result.keys()):
                if (cpuKey not in result[appKey].keys()):
                    ramMap = {}
                    ramMap[ramKey] = 1
                    cpuMap[cpuKey] = ramMap
                    result[appKey] = cpuMap
                else:
                    if (ramKey not in result[appKey][cpuKey].keys()):
                        result[appKey][cpuKey][ramKey] = 1
                    else:
                        result[appKey][cpuKey][ramKey] += 1
            else:
                cpuMap = {}
                ramMap = {}
                ramMap[ramKey] = 1
                cpuMap[cpuKey] = ramMap
                result[appKey] = cpuMap

    return (result)


'''
Used to get annual cost of each application
@param applicationDict - takes the dictionary of all the applications with cpu core and ram 
'''
def annualCost(applicationDict):
    pricingDict = {1.0: {4096.0: 0.023, 2048.0: 0.023, 16384.0: 0.023, 8192.0: 0.023},
                    2.0: {8192.0: .464, 16384.0: .51, 4096.0: .126, 8.0: .01}, 16.0: {16384.0: .51},
                    4.0: {16384.0: .226, 8192.0: .180, 24576.0: .250, 32768.0: .288},
                    8.0: {32768.0: .53, 65536.0: .576, 16384.0: .51}}
    finalDict = applicationDict
    totalAmount = []
    for key in pricingDict.keys():
        if key in finalDict:
            pricingDictValue = pricingDict[key]
            finalDictValue = finalDict[key]
            for inside_key in pricingDictValue.keys():
                if inside_key in finalDictValue.keys():
                    amount = pricingDict[key][inside_key] * finalDict[key][inside_key]
                    totalAmount.append(amount)
    annualAmount = sum(map(float,totalAmount))
    return(annualAmount)



'''
This method is used to calculate the price of each attribute in application.
@param applicationDict - takes the dictionary of dictionary of all the applications with cpu core and ram 
'''
def pricing(groupDict):
    finalCost = 0
    for group in groupDict.keys():
        groupDictValue =(groupDict[group])
        annualAmount =annualCost(groupDictValue) * 24 * 7 * 365

        print("The annual cost of %s : $%d" %(group, annualAmount))
        if group == 'Engineering':

            print("The cost of %s end of year 1 would be %d" %(group, 1.1*annualAmount))
            print("The cost of %s end of year 2 would be %d" % (group, 1.25*1.1*annualAmount))
            print("The cost of %s end of year 3 would be %d" % (group ,1.40*1.25*1.1 * annualAmount))
            finalCost = annualAmount*1.1+ annualAmount*1.25*1.1 + annualAmount*1.4*1.25*1.1
        elif group == 'Sales':
            print("The cost of %s end of year 1 would be %d" % (group, 0.2 * annualAmount))
            finalCost = annualAmount*.2
        else:

            finalCost = annualAmount*3

            print("The cost of %s end of year 1 would be %d" % (group, annualAmount))
            print("The cost of %s end of year 2 would be %d" % (group, annualAmount))
            print("The cost of %s end of year 3 would be %d" % (group, annualAmount))
        print("Final cost of %s over three years is $%d " %(group.upper(), finalCost))
        print('')
