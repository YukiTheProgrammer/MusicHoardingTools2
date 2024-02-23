import threading

def MultiThreader(targetFunction,listOfArgs = []):
    threads = []
    for args in listOfArgs:
        thread = threading.Thread(target=targetFunction, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()    
