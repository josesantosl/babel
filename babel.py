#!/usr/bin/python3
import sys

"""
Author: José Santos L.

Description: 
This software is an solution equivalent for the 
org-babel-tangle of org-mode.

tangle:
    take all the codeblocks with a filename after the lang specification


"""

def main():
    print("entro")
    if sys.argv[1] == "tangle":
        if len(sys.argv)==2:
            print("is missing a filename to convert")
        else:
            tangle(sys.argv[2])

def tangle(filename):
    fileread = open(filename,'r').readlines()
    listTangledFiles=[]
    filenames = []
    counterCodeBlocks = 0

    writing=False
    writingFile=0

    #search the codeblocks
    for line in fileread:
        if "'''" in line and writing==True:
            writing=False
        elif "'''" in line and writing==False and len(line.split())==2:
            newfilename=line.split()[1]
            counterCodeBlocks+=1
            if not newfilename in filenames:
                filenames.append(newfilename)
                listTangledFiles.append(open(newfilename,'w'))
            
            writing=True
            writingFile = filenames.index(newfilename)

        elif (not "'''" in line) and writing:
            listTangledFiles[writingFile].writelines(line)

    for i in range(len(listTangledFiles)):
        listTangledFiles[i].close()
    print("tangled "+str(counterCodeBlocks)+" codeblocks.")

if __name__ == "__main__":
    main()
