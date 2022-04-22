# Markdown Babel

This software is an solution equivalent for the 
org-babel-tangle of org-mode.

## __tangle__:
take all the codeblocks with a filename after the lang specification.

that means only the codeblocks with a filename as a second parameter will
be transfer to that file.

### codeblock taken
    ```python hello.py

    print("hello world")

    ```



this codeblock go to hello.py

## __readme__:
Write a README.md compiling a list of files in order. If you want to write a README.md with the files module1.md, module2.md, module3.md you need to
write the command:

    
    python3 babel.py readme module1.md module2.md module3.md


the order will be:

    module1
    module2
    module3

