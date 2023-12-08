# Zala Weyker
# 12/8/2023
# File Search
# This program will display all paths to a given directory name
import os


def find(path, dir):
    tagged = []

    def checktag(path):
        if path in tagged:
            return True
        else:
            return False

    def leavetag(path):
        tagged.append(path)

    volatile_path = path
    results=[]
    os.chdir(path)
    while True:
        tags = 0
        try:
            if not os.listdir(volatile_path) or checktag(volatile_path):
                leavetag(volatile_path)
                x=volatile_path.split('\\')
                x.pop()
                volatile_path = "\\".join(x)
        except NotADirectoryError:
            pass
        if checktag(path):
            return results
        for branch in os.listdir(volatile_path):
            if checktag(f"{volatile_path}\\{branch}"):
                tags+=1
                if tags >= len(os.listdir(volatile_path)):
                    leavetag(volatile_path)
                    x = volatile_path.split('\\')
                    x.pop()
                    volatile_path = "\\".join(x)
                    break
            elif branch == dir:
                results.append(f"{volatile_path}\\{branch}")
                leavetag(f"{volatile_path}\\{branch}")
            else:
                volatile_path = f"{volatile_path}\\{branch}"
                break


print(find("C:\\Users\\weyke\\Documents\\Coding\\Work\\Files\\tree", "python"))