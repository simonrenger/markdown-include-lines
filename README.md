# markdown-include-lines
This is a markdown extension for python which allows you to include lines of a whole source file. This project was inspired by https://github.com/cmacmackin/markdown-include

## What can you do with this extension?

- include a certain range of lines e.h. 5-29
- include the whole file
- include only a certain line
- include certain lines

## The use of this extension is as following:
_([...] subtsitute with the right content)_
```
{[file type] [start at line] - [end at line] [file]}
```
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
```
cd /where/ever/the/files/are
$ pip install .
```
The it should be installed and you can use it like every other markdown extension
