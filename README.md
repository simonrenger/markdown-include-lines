# markdown-include-lines
This is a markdown extension for python allows you to include lines from a source file or a whole source file. This project was inspired by https://github.com/cmacmackin/markdown-include. I tried to make the syntax as simple and intuitive as possible.

## What can you do with this extension?

- include a certain range of lines e.h. 5-29
- include the whole file
- include only a certain line
- include certain lines

## How to use this extension:
_([...] subtsitute with the right content)_
```
{[file type]* [start at line] - [end at line] [file]}
```
_* file type is for the highlight part of the code block._

Range of lines:
```
{python 15-20 include.py}
```
In case you want to include the whole file:
```
{python * include.py}
```
In case you want to include only one line:
```
{python 15 include.py}
```
In case you want to include only certain lines of code:
```
{python [15,20,3] include.py}
```
### Example

In case you want to include only certain lines of code:
```
{python [15,20,3] include.py}
```
The extension will generate the following output:

_I:\Simon\Y1\BlockB\Coding\Project\Game\main.cpp_
```cpp
[...]
#include "Game.h"

[...]
    const float fps = 100;

[...]
    sr::Shader shader("Basic3D");
```
**Note**: [...] are actual part of this extension they get generated when ever you use this:
```
{python [15,20,3] include.py}
```
syntax.

## How to install
You just clone this repo and then you run:
``` bash
cd /where/ever/the/files/are
$ pip install .
```
This should install the exention and then you can use it like any other markdown extension.
