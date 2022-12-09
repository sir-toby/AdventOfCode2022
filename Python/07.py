from utils import imports
import copy

# data model:
# folders = (folderId, size) folderId = list of path to folder
# files = (name, size, folder)
# todo: switch from list to key/value


#### TODO: Foldernamen sind nicht eindeutig! ####


def createFolder(folderName, dir, folders):

    folders.append([dir+[folderName], 0])
    return folders


def addFile(line, folder, files):
    # Add file to fileList
    lineList = line.split(" ")
    files.append([lineList[1], lineList[0], copy.copy(folder)])
    return files


def calculateSizeOfCurrentFolder(currentFolder, folders, files):
    size = 0
    # files
    for file in files:
        if file[2] == currentFolder:
            size += int(file[1])
    for child in folders:
        if child[0][: -1] == currentFolder:
            size += child[1]

    for f in folders:
        if f[0] == currentFolder:
            f[1] = size

    return folders


def createFileDirectory(inputFile):
    folders = [[['/'], 0]]
    files = []
    currentFolder = []

    for line in inputFile:
        if line == "$ cd ..":
            folders = calculateSizeOfCurrentFolder(currentFolder, folders, files)
            currentFolder.pop()
        elif line.startswith("$ cd "):
            currentFolder.append(line[5:])  # currentFolder is set to current directory
        elif line == "$ ls":
            continue
        elif line.startswith("dir"):  # Add folder to folder list
            folders = createFolder(line[4:], currentFolder, folders)
        else:  # add file to file list
            files = addFile(line, currentFolder, files)
    # make sure to calculate folders if we not end up in root
    while currentFolder != []:
        folders = calculateSizeOfCurrentFolder(currentFolder, folders, files)
        currentFolder.pop()

    return files, folders


def foldersWithMaximum(max, folderList):
    size = 0
    for folder in folderList:
        if folder[1] <= max:
            size += folder[1]
    return size


def largestFolderWith(space, folders):
    tallestSmallFolder = ['0', 70000000]
    sizeList = []
    for folder in folders:
        sizeList.append(folder[1])
        if folder[1] > space and folder[1] < tallestSmallFolder[1]:
            tallestSmallFolder = folder
    sizeList.sort(reverse=True)
    print(sizeList)
    return tallestSmallFolder[1]


# Main part
fileList, folderList = createFileDirectory(imports.import1d("07 Input.txt", "\n"))

# Part1:
print(foldersWithMaximum(100000, folderList))

# Part2:
maxSpace = 70000000
freeSpaceRequired = 30000000
unusedSpace = maxSpace - folderList[0][1]
spaceToFreeUp = freeSpaceRequired-unusedSpace
print(largestFolderWith(spaceToFreeUp, folderList))
