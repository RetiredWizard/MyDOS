## MyDOS
**Early Proof of Concept version of PyDOS

**MicroPython/CircuitPython DOS-like shell for microcontroller boards**   

I have gotten used to having PyDOS installed on microcontrllers I'm working with but on boards with limited FLASH or RAM PyDOS won't run. That's where this
early prototype version has come in useful.

To launch MyDOS, type **import MyDOS**

**Notes:**

- Unlike PyDOS, When running Python scripts from the MyDOS prompt you must include the .py extension.
- Directory Paths are not supported so you must use the **CD** command if you want to run scripts from subdirectories
