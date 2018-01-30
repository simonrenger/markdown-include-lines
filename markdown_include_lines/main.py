#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# main.py
#
#Cyroxx Software Lizenz 1.0
#Copyright (c) 30.01.2018, Simon Renger <info@simonrenger.de>
#Alle Rechte vorbehalten.
#Durch diese Lizenz ist der nachfolgende Quelltext in all seinen Erscheinungsformen [Beispiele: Kompiliert, Unkompiliert, Script Code] geschützt.
#Im nachfolgenden Text werden die Worte Werk, Script und Quelltext genutzt Diese drei Wörter sind gleichzusetzen und zu schützen.
#Der Autor dieses Werkes kann für keinerlei Schaden die durch das Werk enstanden sein könnten, entstehen werden verantwortlich gemacht werden.
#  
#Rechte und Pflichten des Nutzers dieses Werkes:
#Der Nutzer dieses Werkes verpflichtet sich, diesen Lizenztext und die Autoren-Referenz auszuweisen und in seiner originalen Erscheinungsform zu belassen.
#Sollte dieses Werk kommerziell genutzt werden, muss der Autor per E-Mail informiert werden, wenn eine E-Mail Adresse angegeben/bekannt ist.
#Das Werk darf solange angepasst, verändert und zu verändertem Zwecke genutzt werden, wie dieser Lizenztext und die Autor(en)-Referenz ausgewiesen wird und
#nicht gegen die Lizenzvereinbarungen verstößt.
#Das Werk darf nicht für illigale Zwecke eingesetzt werden.
#
# This project is ensprired by https://github.com/cmacmackin/markdown-include
#
# the syntax of this project is: [...] subtsitute with the right content
# {[file type] [start at line] - [end at line] [file]}
# example:
# {python 15-20 include.py}
# In case you want to include the whole file:
# {python * include.py}
# In case you want to include only one line:
# {python 15 include.py}
# In case you want to include only certain lines of code:
# {python [15,20,3] include.py}
from __future__ import print_function
import re
import os.path
from codecs import open
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

# version 1.0
#SYNTAX = re.compile(r'\{([a-z]+)\s(([0-9]+)\s-\s([0-9]+)|([0-9]+)-([0-9]+)|([0-9]+)\s-([0-9]+)|([0-9]+)-\s([0-9]+)|\*)\s(.*)}')
#version 1.1
SYNTAX = re.compile(r'\{([a-z]+)\s(([0-9]+)\s-\s([0-9]+)|([0-9]+)-([0-9]+)|([0-9]+)\s-([0-9]+)|([0-9]+)-\s([0-9]+)|\*|([0-9]+)|\[(.*)\])\s(.*)}')

class MarkdownIncludeLines(Extension):
    def __init__(self, configs={}):
        self.config = {
            'base_path': ['.', 'Default location for the file to be checked' \
                'relative paths for the include statement.'],
            'encoding': ['utf-8', 'Encoding of the files ' \
                'statement.']
        }
        for key, value in configs.items():
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add(
            'include_lines', IncLinePreprocessor(md,self.getConfigs()),'_begin'
        )

class IncLinePreprocessor(Preprocessor):
    #member vars:
    #contains
    m_filename = None
    m_code = []
    #methods:
    def __init__(self,md,config):
        super(IncLinePreprocessor, self).__init__(md)
        self.base_path = config['base_path']
        self.encoding = config['encoding']
    def run(self,lines):
        done = False
        while not done:
            for line in lines:
                loc = lines.index(line)
                m = SYNTAX.search(line)
                if m:
                    match = SYNTAX.match(line);
                    codetype = match.group(1)
                    filename = match.group(13)
                    start = -1;
                    end = -1;
                    rangeList = []
                    #print (match.groups())
                    for x in range(2, 13):
                        if match.group(x) != None and match.group(x) != "*" and x != 2 and x != 12:
                            if start == -1:
                                start = int(match.group(x))
                                continue
                            elif end == -1:
                                end = int(match.group(x))
                        elif match.group(x) == "*":
                            break
                        elif x == 12 and match.group(x) != None:
                            rangeList = match.group(x).split(",")
                            break;
                
                    if (start <= 0 or end <= 0) and start <= end and len(rangeList) == 0:
                        lines = lines[:loc] +self.makeCode(filename,codetype,self.parse(filename)) + lines[loc+1:]
                    elif len(rangeList) == 0:
                        lines = lines[:loc] +self.makeCode(filename,codetype,self.parse(filename,start,end,False)) + lines[loc+1:]
                    else:
                        result = []
                        for index in rangeList:
                            result.append("[...]")
                            result.extend(self.parse(filename,int(index),-1,False))
                        lines = lines[:loc] +self.makeCode(filename,codetype,result)+ lines[loc+1:]
                        
                    if filename != self.m_filename:
                        self.m_filename = filename;
                else:
                    done = True
        return lines

    def makeCode(self,filename,codeType,codeList):
        output = [];
        output.append("_"+filename+"_");
        output.append("```"+codeType)
        output.extend(codeList)
        output.append("```")
        return output
    def parse(self,filename,start=0,end=0,wholepage = True):
        #correct start
        if start == 1:
            start -= 1
        #check if filename is not the same then load data
        data = None
        if filename != self.m_filename:
            data = self.readFile(filename)
        else:
            data = self.m_code
        #parse
        outcome = []
        for cnt, line in enumerate(data):
            if cnt >= start and cnt <= end or wholepage == True:
                outcome.append(line)
            elif end == -1 and cnt == start:
                outcome.append(line)
        return outcome        
            
    def readFile(self,filename):
        filename = os.path.expanduser(filename)
        if not os.path.isabs(filename):
            filename = os.path.normpath(
                os.path.join(self.base_path,filename)
            )
        try:
            #open file:
            with open(filename, 'r', encoding=self.encoding) as file:
                self.m_code = file.readlines()
                return self.m_code
        except Exception as e:
            print('Warning: could not find file {}. Ignoring '
                'include statement. Error: {}'.format(self.m_filename, e))
            return ['Warning: could not find file {}. File:'.format(self.m_filename, e)]
        

def makeExtension(*args,**kwargs):
    return MarkdownIncludeLines(kwargs)
