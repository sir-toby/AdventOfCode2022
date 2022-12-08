from utils import imports

# data model:
#folders = (folderName, parentFolder, size)
#files = (name, size, folder)
# todo: switch from list to key/value


#### TODO: Foldernamen sind nicht eindeutig! ####


def createFolder(folderName, parent, folders):
    folders.append([folderName, parent, 0])
    return folders


def changeToParentFolder(currentFolder, folders):
    for f in folders:
        if f[0] == currentFolder:
            return f[1]


def addFile(line, folder, files):
    # Add file to fileList
    lineList = line.split(" ")
    files.append([lineList[1], lineList[0], folder])
    return files


def calculateSizeOfCurrentFolder(folder, folders, files):
    size = 0
    # files
    for file in files:
        if file[2] == folder:
            size += int(file[1])
    for child in folders:
        if child[1] == folder:
            size += child[2]

    for f in folders:
        if f[0] == folder:
            f[2] = size

    return folders


def createFileDirectory(inputFile):
    folders = [['/', '', 0]]
    files = []
    currentFolder = "/"

    for line in inputFile:
        print(inputFile.index(line))
        if line == "$ cd ..":
            folders = calculateSizeOfCurrentFolder(currentFolder, folders, files)
            currentFolder = changeToParentFolder(currentFolder, folders)
        elif line.startswith("$ cd "):
            currentFolder = line[5:]  # currentFolder is set to current directory
        elif line == "$ ls":
            continue
        elif line.startswith("dir"):  # Add folder to folder list
            folders = createFolder(line[4:], currentFolder, folders)
        else:  # add file to file list
            files = addFile(line, currentFolder, files)
    # make sure to calculate folders if we not end up in root
    while currentFolder != "/":
        folders = calculateSizeOfCurrentFolder(currentFolder, folders, files)
        currentFolder = changeToParentFolder(currentFolder, folders)
    # calculate root folder
    folders = calculateSizeOfCurrentFolder("/", folders, files)

    return files, folders


def foldersWithMaximum(max, folderList):
    size = 0
    for folder in folderList:
        if folder[2] <= max:
            size += folder[2]
    return size


# Main part
fileList, folderList = createFileDirectory(imports.import1d("07 Input.txt", "\n"))
print(folderList)
print(foldersWithMaximum(100000, folderList))
