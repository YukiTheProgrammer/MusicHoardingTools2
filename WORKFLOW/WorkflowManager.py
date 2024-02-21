import os

def CreateFile(fileName):
    f = open(fileName,"x")
    f.close()
    print(f'Created {fileName}')

def CreateWorkflowCategories(listOfCategories):
    x = 0
    for category in listOfCategories:
        CreateFile(str(x)+"00 ---"+category+"---")
        x += 1
def CreateCategories(listOfCategories,numOfWorkflowCategories):
    for i in range(numOfWorkflowCategories):
        x = 1
        for category in listOfCategories:
            CreateFile(str(i) + str(x) + "0 " + category)
            x += 1
def CreateTasks(listOfTasks):
    x = 1
    for tasks in listOfTasks:
        for i in range(len(tasks)):
            CreateFile("0"+str(x)+str(i+1)+ " "+tasks[i])
        x += 1
    
def InitializeWorkflow():
    listOfWorkflowCategories = ["TODO","DOING","DONE"]
    listOfCategories = ["INFORMATION","DOWNLOADING","PROCESSING"]
    listOfTasks = [
                   ["Get Already Downloaded Files",
                    "Get List Of Leaks",
                    "Get List Of All Releases",
                    "Get List Of All Streaming Releases",
                    "Package Information"],
                   ["Download from Leakedcx",
                    "Download from Youtube",
                    "Download from Soundcloud",
                    "Download From Bandcamp"
                    ],
                   ["Tag Tracks",
                    "Organize Tracks Into Folders",
                    "Put Folders Into Artist Folder"
                    ]
                   ]
    CreateWorkflowCategories(listOfWorkflowCategories)
    CreateCategories(listOfCategories,len(listOfWorkflowCategories))
    CreateTasks(listOfTasks)

def ShowWorkflow():
    workflow_raw = os.listdir()
    tasks = []
    x = 0
    for element in workflow_raw:
        if element == "WorkflowManager.py":
            x = 0
        elif (element.isupper() or '---' in element):
            print(element[4:])
        else:
            print(str(x) + " " + element[4:])
            tasks.append(element)
            x += 1
    return(tasks)

def UpdateWorkflow():
    tasks = ShowWorkflow()
    taskToMove_index = int(input("Which task do you want to update"))
    taskToMove = tasks[taskToMove_index]
    if taskToMove[0] == "0":
        os.rename(taskToMove,"1"+taskToMove[1:])
        print(f"'{taskToMove[4:]}' task has been updated")
    elif taskToMove[0] == "1":
        os.rename(taskToMove,"2"+taskToMove[1:])
        print(f"'{taskToMove}' task has been updated")

def WorkflowUI():
    while True:
        option = input("0: View Workflow\n1: Update Workflow\n> ")
        if option == "0":
            ShowWorkflow()
            print("\n\n")
        elif option == "1":
            UpdateWorkflow()
            print("\n\n")
        else:
            break
            
WorkflowUI()
