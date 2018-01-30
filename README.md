# markdown-include-lines
This is a markdown extension for python which allows you to include lines of a whole source file. This project was enspired by https://github.com/cmacmackin/markdown-include

## What can you do with this extension?

- include a certain range of lines e.h. 5-29
- include the whole file
- include only a certain line
- include certain lines

## The use of this extension is as following:
(_[...] subtsitute with the right content_)
```
{[file type] [start at line] - [end at line] [file]}
```
*Range of lines:*
```
{python 15-20 include.py}
```
*In case you want to include the whole file:*
```
{python * include.py}
```
*In case you want to include only one line:*
```
{python 15 include.py}
```
*In case you want to include only certain lines of code:*
```
{python [15,20,3] include.py}
```
