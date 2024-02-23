import threading

def PackForMultiThread(mainList,argsToPackIn):
    for i in range(len(mainList)):
        mainList[i] = [mainList[i]]+argsToPackIn
    return(mainList)
def MultiThreader(targetFunction,listOfArgs = []):
    threads = []
    if len(listOfArgs) > 1:
        listOfArgs = PackForMultiThread(listOfArgs[0],listOfArgs[1:])
    for args in listOfArgs:
        thread = threading.Thread(target=targetFunction, args=tuple(args))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()    


