# Markdown Babel

This software is an solution equivalent for the 
org-babel-tangle of org-mode.

## translate:
take all the codeblocks with a filename after the lang specification.

that means only the codeblocks with a filename as a second parameter will
be transfer to that file.

### codeblock taken

    ```python hello.py

    print("hello world")

    ```

this codeblock go to hello.py

## document
completely opposite to the previous function. "document" takes a code file and converts it into a markdown, with all comment blocks as text and all code as code blocks.
write the command:

	python3 babel.py document test1.c
	
test1.c as
```c
#include <stdio>
/*
write test.
# TITLE 1
## Title2 2
### title 3
*/
int main(){
    printf("hello world");
}
/*# second function*/
int n(){
    return 5;
}

```

will be translated to test1.md as

	```c
	#include <stdio>
	```

	writing test.
    # TITLE 1
    ## Title 2
    ### title 3

	```c
	int main(){
		printf("hello world");
	}
	```

    # second function

	```c
	int n(){
		return 5;
	}
	```

## readme:
Write a README.md compiling a list of files in order. If you want to write a README.md with the files module1.md, module2.md, module3.md you need to
write the command:

    
    python3 babel.py readme module1.md module2.md module3.md


the order will be:

    module1
    module2
    module3

