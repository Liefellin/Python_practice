# Zala Weyker
# 12/8/2023
# File Search
# This program will display all paths to a given directory name
import os
from pathlib import Path


def findplib(path, dir):
    tagged = []

    home = Path(path)

    def checktag(path):
        return path in tagged

    def leavetag(path):
        tagged.append(path)

    volatile_path = home

    while True:
        tags = 0
        if checktag(home):
            break
        if not [thing for thing in volatile_path.iterdir()]:
            leavetag(volatile_path)
        if checktag(volatile_path):
            volatile_path = volatile_path.parent
        for branch in volatile_path.iterdir():
            if checktag(volatile_path / branch):
                tags += 1
                if tags >= len([thing for thing in volatile_path.iterdir()]):
                    leavetag(volatile_path)
                    volatile_path = volatile_path.parent
                    break
            elif str(branch.name) == dir:
                yield f"{volatile_path / branch}"
                leavetag(volatile_path / branch)
            else:
                volatile_path = volatile_path / branch
                break


def find(path, dir):
    tagged = []

    def checktag(path):
        return path in tagged

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


for i in findplib("C:\\Users\\weyke\\Documents\\Coding\\Work\\Files\\tree", "python"):
    print (i)
