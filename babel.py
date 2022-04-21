#!/usr/bin/python3
import sys

"""
Author: José Santos L.

Description: 
This software is an equivalent solution for the 
org-babel-tangle of org-mode.

tangle:
    take all the codeblocks with a filename after the lang specification.
readme:
    write a README.md compiling a list of files in order.

"""

def main():
    if len(sys.argv)==1:
        help()
    elif sys.argv[1] == "tangle":
        if len(sys.argv)==2:
            print("is missing a filename to convert")
            help()
        else:
            tangle(sys.argv[2])
    elif sys.argv[1] == "help":
        help()
    elif sys.argv[1] == "readme":
        if len(sys.argv)==2:
            help()
        else:
            readme()
    else:
        tangle(sys.argv[2])


def help():
    print("tangle:\n\ttake all the codeblocks with a filename after the lang specification")
    print("readme:\n\nwrite a README.md compiling a list of files in order.")
    

def tangle(filename):
    fileread = open(filename,'r').readlines()
    listTangledFiles=[]
    filenames = []
    counterCodeBlocks = 0

    writing=False
    writingFile=0

    #search the codeblocks
    for line in fileread:
        if "```" in line and writing==True:
            writing=False
        elif "```" in line and writing==False and len(line.split())==2:
            newfilename=line.split()[1]
            counterCodeBlocks+=1
            if not newfilename in filenames:
                filenames.append(newfilename)
                listTangledFiles.append(open(newfilename,'w'))
            
            writing=True
            writingFile = filenames.index(newfilename)

        elif (not "```" in line) and writing:
            listTangledFiles[writingFile].writelines(line)

    for i in range(len(listTangledFiles)):
        listTangledFiles[i].close()
    print("tangled "+str(counterCodeBlocks)+" codeblocks.")

def readme():
    readmeFile= open("README.md",'w')
    fileread=None
    for i in range(1,len(sys.argv)):
        try:
            fileread = open(sys.argv[i],'r')
        except:
            print("can't found the file "+sys.argv[i])
            continue

        #read all the file and rewrite it to the README.md
        readmeFile.writelines(fileread.readlines())

        fileread.close()
    readmeFile.close()
        
if __name__ == "__main__":
    main()
