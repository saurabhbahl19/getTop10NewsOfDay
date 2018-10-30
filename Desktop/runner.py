import story
import json
import sys
if __name__ == "__main__":
    path = story.getFilePath()
    rowCount = story.getRowCount(path)
    columnCount = story.getColumnCount(path)
    sheet = story.getSheet(0, path)


    print("Enter 0 to exit")
    print("Enter 1 for Getting all the departments which host hardware")
    print("Enter 2 for Getting a list of all the applications for each department")
    print("Enter 3 for Getting list of all the attributes in that particular column")
    print("Enter 4 for Getting all the list of departments by number of cpu and memory used")
    print("Enter 5 for Getting all the list of Sites by number of cpu and memory used")
    print("Enter 6 for Printing annual cost , cost of three years and Final cost of hosting")

    while(True):
        choice = int(input("Pick the data you want to see"))
        print(choice)
        if (choice == 0):
            sys.exit()
        elif(choice == 1):
            # Generate a list of all departments that have hardware hosted
            print("All the departments which host hardware are :",
                  ','.join(list(story.getAllDepartments(0, 0, rowCount, sheet).keys())))
            print(".............................................................................................")

        elif (choice == 2):
            # Generate a list of all the applications for each department.
            groupDepartmentCountMap = story.getApplicationsForEachDepartment(sheet, rowCount)
            groupDepartmentMap = {}
            for key in groupDepartmentCountMap.keys():
                groupDepartmentMap[key] = list(groupDepartmentCountMap[key])
            print("All the applications for each department:", json.dumps(groupDepartmentMap, indent=4, sort_keys=True))
            print("..............................................................................................")

        elif (choice == 3):
            # Gives you list of all the attributes in that particular column
            departmentList = (list(story.getAllDepartments(0, 0, rowCount, sheet).keys()))
            applicationList = (list(story.getAllApplication(0, 1, rowCount, sheet).keys()))
            dataCenterList = (list(story.getAllDataCenter(0, 11, rowCount, sheet).keys()))
            print("Departmentlist: ")
            result = {}
            # Getting all the list of departments by number of cpu and memory used
            for department in departmentList:
                dep = (story.getGroupCpuRamMap(department, sheet, rowCount, 0))
                result.update(dep)
                print(story.getGroupCpuRamMap(department, sheet, rowCount, 0))
            print("...............................................................................................")

        elif (choice == 4):
            # Getting all the list of Applications by number of cpu and memory used
            print("Applicationlist: ")
            for application in applicationList:
                print(story.getApplicationCpuRamMap(application, sheet, rowCount, 1))
            print("................................................................................................")

        elif (choice == 5):
        # Getting all the list of Sites by number of cpu and memory used
            print("DataCenterlist: ")
            for dataCenter in dataCenterList:
                print(story.getDataCenterCpuRamMap(dataCenter, sheet, rowCount, 11))
            print(".................................................................................................")

        elif(choice == 6):
        #This will print annual cost , cost of three years and Final cost of hosting
           print("Pricing")
           print(story.pricing(result))

        else :
            print("Try again between 1 to 6")