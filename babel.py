#!/usr/bin/python3
import sys

"""
Author: José Santos L.

Description: 
This software is an equivalent solution for the 
org-babel-tangle of org-mode.

translate:
    take all the codeblocks with a filename after the lang specification.
document:
    write a MarkDown document with the same name of the file. 
readme:
    write a README.md compiling a list of files in order.

"""

def main():
    if len(sys.argv)==1:
        help()
    elif sys.argv[1] == "translate":
        if len(sys.argv)==2:
            print("is missing a filename to convert")
            help()
        else:
            translate(sys.argv[2])
    elif sys.argv[1] == "help":
        help()
    elif sys.argv[1] == "readme":
        if len(sys.argv)==2:
            help()
        else:
            readme()
    elif sys.argv[1] == "document":
        if len(sys.argv)==2:
            help()
        else:
            document()
    else:
        help()


def help():
    print("translate:\n\ttake all the codeblocks with a filename after the lang specification.")
    print("document:\n\twrite a MarkDown document with the same name of the file. Actually just working with /**/ comment blocks.")
    print("readme:\n\twrite a README.md compiling a list of files in order.")
    

def translate(filename):
    fileread = open(filename,'r').readlines()
    listTangledFiles=[]
    filenames = []
    counterCodeBlocks = []

    writing=False
    writingFile=0

    #search the codeblocks
    for line in fileread:
        if "```" in line and writing==True:
            writing=False
        elif "```" in line and writing==False and len(line.split())==2:
            newfilename=line.split()[1]
            if not newfilename in filenames:
                filenames.append(newfilename)
                listTangledFiles.append(open(newfilename,'w'))
                counterCodeBlocks.append(0)
            
            writing=True
            writingFile = filenames.index(newfilename)
            counterCodeBlocks[writingFile]+=1

        elif (not "```" in line) and writing:
            listTangledFiles[writingFile].writelines(line)

    for i in range(len(listTangledFiles)):
        listTangledFiles[i].close()
    for i in range(len(listTangledFiles)):
            print("translated "+str(counterCodeBlocks[i])+" codeblocks to "+listTangledFiles[i].name)
            

def document():

    #open read & write files.
    filename,extension= sys.argv[2].split('.')
    fileread = open(sys.argv[2],'r').readlines()
    writingFile = open(filename+".md",'w')

    #start start & close vars
    start = '/*'
    end   = '*/'

    #soft languages
    if extension in ['py','rb']:
        start='"""'
        end = '"""'

    comment=False
    code   =False

    for line in fileread:
        if not comment and not code and len(line)-1>0:
            if start in line.split()[0] and line[0]!= " ":
                comment=True
            else:
                code=True
                writingFile.writelines("```"+extension+"\n")

        if comment:#comment
            if end in line:
                writingFile.writelines(line.replace(end,""))
                writingFile.writelines("```"+extension+"\n")
                comment=False
                code   =True
            else:
                writingFile.writelines(line)
        else:#code
            if start in line.split()[0] and line[0]!=" " and not end in line:
                writingFile.writelines("```\n")
                writingFile.writelines(line.replace(start,""))
                comment=True
                code   = False
            elif start in line.split()[0] and line[0]!=" " and end in line and start!=end:
                writingFile.writelines("```\n")
                writingFile.writelines(line.replace(start,"").replace(end,""))
                writingFile.writelines("```"+extension+"\n")

            else:
                writingFile.writelines(line)
    if code:
        writingFile.writelines("```")

    #close file
    writingFile.close()
    print(sys.argv[2]+" convrted to "+filename+".md")


def readme():
    readmeFile= open("README.md",'w')
    fileread=None
    for i in range(2,len(sys.argv)):
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
