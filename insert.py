import re
import os

from triggers import *

def check(line, nlspace):
    if line.lstrip().startswith('}') and len(line)-len(line.lstrip())<nlspace:
        # print(line)
        # print(len(line)-len(line.lstrip()), nlspace)
        assert(0)


def insert(line, todo):
    nlspace=len(line)-len(line.lstrip())
    lspace, line=line[:nlspace], line[nlspace:]


    if todo[0]=='add_full_resistances':
        return lspace+'resistances = full_resistances(),\n'+lspace+line
    
    if todo[0]=='add_light':
        return lspace+'light = {intensity = 0.9, size = 40, color = {1, 1, 0.75}},\n'+lspace+line

    if line.startswith(todo[0]+' ='):
        if todo[0]=='resistances':
            return 'remove_resistances'
        
        if line.startswith(todo[0]+' = '+todo[1]):
            # print(line)
            return lspace+re.sub(todo[0]+' = '+todo[1], todo[0]+' = '+todo[2], line)
        
        assert(0)

    #print(f'{line} does not match {todo[0]}')          
    return ''


def add_function_full_resistance(fo):
    with open('full_resistances.lua', 'r') as fi:
        while 1:
            line=fi.readline()
            if not line:
                break
            fo.write(line)

"""


# entity/entities.lua

with open('entity/entities.lua', 'r') as fi, open('entity/temp.lua', 'w') as fo:
    while 1:
        line=fi.readline()
        if not line:
            break
        fo.write(line)
        todolist, nlspace=trigger(line)
        if len(todolist):
            for todo in todolist:
                while 1:
                    line=fi.readline()
                    check(line, nlspace)
                    newline=insert(line, todo)
                    if len(newline):
                        fo.write(newline)
                        break
                    else:
                        fo.write(line)
        

"""
        

fl=open('log.txt', 'w')

with open('../base/prototypes/entity/entities.lua', 'r') as fi, open('../base/prototypes/entity/temp.lua', 'w') as fo:
# with open('t1.lua', 'r') as fi, open('t2.lua', 'w') as fo:
    add_function_full_resistance(fo)
    while 1:
        line=fi.readline()
        if not line:
            break

        fo.write(line)
        todolist, nlspace=trigger_base_entity_entities(line)
        if len(todolist):
            
            fl.write('\n')
            fl.write(line)

            for todo in todolist:
                while 1:
                    line=fi.readline()
                    check(line, nlspace)
                    newline=insert(line, todo)
                    if len(newline):
                        if newline=='remove_resistances':
                            nesting=line.count('{')
                            flag=False
                            while 1:
                                if nesting>0: flag=True
                                nesting-=line.count('}')
                                if nesting==0 and flag:
                                    break
                                line=fi.readline()
                                nesting+=line.count('{')
                            fl.write('resistances removed\n')
                        else:
                            fo.write(newline)
                            fl.write(f'changes on {todo[0]} applied\n')
                        break
                    else:
                        fo.write(line)
os.remove('../base/prototypes/entity/entities.lua')
os.rename('../base/prototypes/entity/temp.lua', '../base/prototypes/entity/entities.lua')

fl.close()