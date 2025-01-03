import re
import os

def check(line, nlspace):
    if line.lstrip().startswith('}') and len(line)-len(line.lstrip())<nlspace:
        # print(line)
        # print(len(line)-len(line.lstrip()), nlspace)
        assert(0)


def insert(line, adjustment):
    nlspace=len(line)-len(line.lstrip())
    lspace, line=line[:nlspace], line[nlspace:]


    if adjustment[0]=='add_full_resistances':
        return lspace+'resistances = full_resistances(),\n'+lspace+line
    
    if adjustment[0]=='add_light':
        return lspace+'light = {intensity = 0.9, size = 40, color = {1, 1, 0.75}},\n'+lspace+line

    if line.startswith(adjustment[0]+' ='):
        if adjustment[0]=='resistances':
            return 'remove_resistances'
        
        if line.startswith(adjustment[0]+' = '+adjustment[1]):
            # print(line)
            return lspace+re.sub(adjustment[0]+' = '+adjustment[1], adjustment[0]+' = '+adjustment[2], line)
        
        # something is wrong with that and may cause problems
        if line.startswith(adjustment[0]+' = '+adjustment[2]):
            return 'already_applied'

        assert(0)

    #print(f'{line} does not match {todo[0]}')          
    return ''


def add_full_resistances_function(fo, fl):
    with open('full_resistances.lua', 'r') as fi:
        while 1:
            line=fi.readline()
            if not line:
                break
            fo.write(line)
    fl.write('\nfunction full resistance added\n')


from todo import TODOS

if __name__=='__main__':

    workdir=os.path.dirname(os.getcwd())

    with open('log.txt', 'w') as fl:
        assert(fl)
        for TODO in TODOS:
            if TODO['special']:
                if TODO['TODO'][0]['item']=='adjust_function_resource':
                    pass
                elif TODO['TODO'][0]['item']=='adjust_agricultural_science_pack_technology':
                    pass
                elif TODO['TODO'][0]['item']=='adjust_agricultural_science_pack_recipe':
                    pass
                elif TODO['TODO'][0]['item']=='vulcanus_mineral_production_increase':
                    pass
            else:
                if len(TODO['TODO']):
                    filepath=os.path.join(workdir, TODO['file'])
                    with open(filepath, 'r') as fi, open('temp.lua', 'w') as fo:
                        assert(fi)
                        assert(fo)
                        fl.write('\n')
                        fl.write(TODO['file'])
                        if TODO['TODO'][0]['item']=='add_full_resistances_function':
                            add_full_resistances_function(fo, fl)
                            remove_old_full_resistances=True
                        else:
                            remove_old_full_resistances=False
                    
                        while 1:
                            line=fi.readline()
                            if not line:
                                break

                            if remove_old_full_resistances and line.startswith('local full_resistances = function()'):
                                while 1:
                                    line=fi.readline()
                                    if line.startswith('end'):
                                        fl.write('\nold full resistances function removed\n')
                                        remove_old_full_resistances=False
                                        break
                                continue
                            
                            fo.write(line)
                            
                            nlspace=len(line)-len(line.lstrip())
                            line=line.strip()



                            if line.startswith('name = '):
                                item=line.split('name = ')[1].rstrip(',')
                                for todo in TODO['TODO']:
                                    if item==todo['item']:
                                        if len(todo['adjustments']):
                                            fl.write('\n')
                                            fl.write(line)
                                            fl.write('\n')
                                            for adjustment in todo['adjustments']:
                                                while 1:
                                                    line=fi.readline()
                                                    check(line, nlspace)
                                                    newline=insert(line, adjustment)
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
                                                            fl.write('old resistances removed\n')
                                                        # something is wrong with that and may cause problems
                                                        elif newline=='already_applied':
                                                            fo.write(line)
                                                            fl.write(f'changes on {adjustment[0]} have been applied before\n')
                                                        else:
                                                            fo.write(newline)
                                                            fl.write(f'changes on {adjustment[0]} applied\n')
                                                        break
                                                    else:
                                                        fo.write(line)
                    
                    os.remove(filepath)
                    os.rename('temp.lua', filepath)

    print('all changes applied\n')