import fileManager as fm
import requests, json, time, os

token = ""

env = open(".env", "r")
env_data = env.read()
env.close()

token = env_data.strip('token = "').strip('"')

if(token == ""):
    token = input("[+] Token: ")

def save_load():
    response=requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'authorization': token})
    fm.make_file('user_data', response.text)

def lookup(id=None, username=None, filebasename=None, lista=[None]):
    user_data = None
    if(lista == [None]):
        file = fm.loadJson(fm.openlast(filebasename))
        for user in file:
            if(id == None):
                name, tag = username.split("#")
                if(user['user']['username'] == name and user['user']['discriminator'] == tag):
                    user_data=(user['user'])
            else:
                if(user['id'] == id):
                    user_data=(user['user'])

    elif(lista == ["all"]):
        allFiles = fm.getAllFiles(filebasename)
        multiFileObj = []
        for filename in allFiles:
            file = fm.loadJson(filename)

            for user in file:
                if(id == None):
                    name, tag = username.split("#")
                    if(user['user']['username'] == name and user['user']['discriminator'] == tag):
                        user_file_obj = [filename, user['user']]
                        multiFileObj.append(user_file_obj)
                else:
                    if(user['id'] == id):
                        user_file_obj = [filename, user['user']]
                        multiFileObj.append(user_file_obj)

        user_data=multiFileObj

    else:
        if('.' in str(lista[0])):
            allFiles = lista
            multiFileObj = []
            for filename in allFiles:
                file = fm.loadJson(filename)

                for user in file:
                    if(id == None):
                        name, tag = username.split("#")
                        if(user['user']['username'] == name and user['user']['discriminator'] == tag):
                            user_file_obj = [filename, user['user']]
                            multiFileObj.append(user_file_obj)
                    else:
                        if(user['id'] == id):
                            user_file_obj = [filename, user['user']]
                            multiFileObj.append(user_file_obj)

            user_data=multiFileObj
        else:
            allFiles = []
            for i in lista:
                allFiles.append(filebasename+str(i)+".json")
            multiFileObj = []
            for filename in allFiles:
                file = fm.loadJson(filename)

                for user in file:
                    if(id == None):
                        name, tag = username.split("#")
                        if(user['user']['username'] == name and user['user']['discriminator'] == tag):
                            user_file_obj = [filename, user['user']]
                            multiFileObj.append(user_file_obj)
                    else:
                        if(user['id'] == id):
                            user_file_obj = [filename, user['user']]
                            multiFileObj.append(user_file_obj)
            user_data=multiFileObj

    return user_data


def usage():
    print("Usage: ")
    print("    save\n    lookup\n       -*id <USER ID>\n       -*username <NAME#TAG>\n       -filebasename user_data\n       -fs ['all']")

usage()
while(True):
    cmd = input("[+] User: ")
    if(cmd == "save"):
        save_load()
    elif("lookup" in cmd):
        
        cmd = cmd.split("-")

        if(len(cmd) == 4):
            if('id' in cmd[1]):
                print(
                    lookup(id=cmd[1].strip("id ").replace(" ", ''), filebasename=cmd[2].strip("filebasename").replace(" ", ''), lista = json.loads(cmd[3].strip("fs ").replace(" ", '')))
                )
            elif("username" in cmd[1]):
                print(
                    lookup(username=cmd[1].strip("username ").replace(" ", ''), filebasename=cmd[2].strip("filebasename").replace(" ", ''), lista = json.loads(cmd[3].strip("fs ").replace(" ", '')))
                )
            else:
                usage()
        else:
            usage()
    else:
        usage()
