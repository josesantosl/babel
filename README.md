# Markdown Babel

This software is an solution equivalent for the 
org-babel-tangle of org-mode.

## __tangle__:
take all the codeblocks with a filename after the lang specification.

that means only the codeblocks with a filename as a second parameter will
be transfer to that file.

### codeblock taken
'''

'''python3 hello.py

print("hello world")
'''

'''

this codeblock go to hello.py


