import os

"""
Input: Artist Name, Directory Path
Output: List Of Albums, List Of Loose Songs, List Of Leaks
"""
def GetAllDownloadedReleases(artistName,dirPath):      
    result = {}
    for root, dirs, files in os.walk(dirPath+"\\"+artistName):
        current_dir = result
        folders = root.split(os.path.sep)[3:]  # Remove the root folder
        for folder in folders:
            if len(files) == 0:
                current_dir = current_dir.setdefault(folder, {})
            else:
                current_dir = current_dir.setdefault(folder, files)
    return result
        
def DisplayDownloadedReleases(dictOfDownloadedReleases,spacing = "  "):
    for key in dictOfDownloadedReleases:
        if isinstance(dictOfDownloadedReleases[key],dict):
            print(spacing + key)
            DisplayDownloadedReleases(dictOfDownloadedReleases[key],spacing+spacing)
        else:
            print(spacing + key)
            for x in dictOfDownloadedReleases[key]:
                print(spacing + spacing + x)

