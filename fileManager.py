from os.path import exists
from os import getcwd
from os import walk
from os import remove
from json import loads

def openlast(name):
    index = 0
    for root, dirs, files in walk(getcwd()):
        if(root == getcwd()):
            for file in files:
                if(".json" in file and name in file):
                    if(int(file.strip(name).strip(".json")) > index):
                        index = int(file.strip(name).strip(".json"))
    return getcwd()+'/'+name+str(index)+".json"

def getAllFiles(name):
    files_r = []
    for root, dirs, files in walk(getcwd()):
        if(root == getcwd()):
            for file in files:
                if(".json" in file and name in file):
                    files_r.append(file)
    return files_r

def make_file(name, dump: str, index=None):
    if(index == None):
        index = 0
        for root, dirs, files in walk(getcwd()):
            if(root == getcwd()):
                for file in files:
                    if(".json" in file and name in file):
                        if(int(file.strip(name).strip(".json")) > index):
                            index = int(file.strip(name).strip(".json"))
        index+=1

    newFile = getcwd()+'/'+name+str(index)+".json"
    
    if(exists(newFile)):
        print("Fatal Error!")
        exit()
    
    file = open(newFile, 'x')
    file.write(dump)
    file.close()


def clearAll(name):
    for root, dirs, files in walk(getcwd()):
        if(root == getcwd()):
            for file in files:
                if(".json" in file and name in file):
                    remove(file)

def loadJson(name):
    file = open(name, "r")
    parse = file.read()
    file.close()
    return loads(parse)