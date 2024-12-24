
from todo import TODO
"""
def trigger(line):
    
    nlspace=len(line)-len(line.lstrip())
    lspace, line=line[:nlspace], line[nlspace:]

    line=line.strip()

    todolist=[]
    
    if line=='name = "fast-inserter",':
        todolist.append(('energy_per_movement', '"7kJ"', '"7J"'))
        todolist.append(('energy_per_rotation', '"7kJ"', '"7J"'))
        todolist.append(('rotation_speed', '0.04', '0.5'))
    elif line=='name = "long-handed-inserter",':
        todolist.append(('energy_per_movement', '"5kJ"', '"5J"'))
        todolist.append(('energy_per_rotation', '"5kJ"', '"5J"'))
        todolist.append(('rotation_speed', '0.02', '0.25'))

    return todolist, nlspace
"""

with open('trigger.py', 'w') as f:
    f.write('def trigger(line):\n\n')
    f.write('\tnlspace=len(line)-len(line.lstrip())\n\n')
    f.write('\tline=line.strip()\n\n')
    f.write('\ttodolist=[]\n\n')

    flag=True
    for todo in TODO:
        f.write(f"{'\tif' if flag else '\n\telif'} line=='name = {todo['item']},':\n")
        flag=False
        for entry in todo['entry']:
            f.write(f"\t\ttodolist.append(('{entry[0]}', '{entry[1]}', '{entry[2]}'))\n")
        
    f.write('\n\treturn todolist, nlspace\n')
    f.close()