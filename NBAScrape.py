
#!/usr/bin/env python
from decorator import decorator

import pandas as pd
import sys
import lxml.html as lh
import requests


@decorator
def on_start(func,*args, **kwargs):
    if kwargs !={}:
        try:
            if kwargs['Start']:
                if 'Verbose' in kwargs['Settings']:
                    if kwargs['Settings']['Verbose']:
                        print(func)
                        pass
                response= func(*args,**kwargs)
                return response
            else:
                kwargs['Start'] = False
                print(func,"DID NOT START")
                return(kwargs)
        except Exception as e:
            print('NODE ERROR OCCURED TRYING TO START NODE FUNCTION:')
            print('===========================================')
            print(func,e)
            print('===========================================')
            print('LAST STATE SET TO:')
            print('===========================================')
            print('ekwargs')
            print('===========================================')
            print('LAST NODE FUNCTION SET TO:')
            print('===========================================')
            print('efunc')
            print('===========================================')
            global ekwargs
            global efunc
            ekwargs = kwargs
            efunc = func
            print('HALTING')
            raise
    else:
        print('Empty kwargs')
        return ()



def start():
    return {'Start':True,'Settings':{'Verbose':True},'Status':{}}

 
@on_start
def lxmlParseUrl1(*args,**kwargs):
    page = requests.get('https://www.basketball-reference.com/players/b/bryanko01.html')
    kwargs['Data'] = lh.fromstring(page.content)
    return kwargs
 
@on_start
def lxmlFindAll2(*args,**kwargs):
    kwargs['Data'] = kwargs['Data'].get_element_by_id('all_advanced')
    return kwargs
 
@on_start
def lxmlParseUrl3(*args,**kwargs):
    kwargs['Data'] =lh.tostring(kwargs['Data']).decode('UTF8')
    kwargs['Data'] = kwargs['Data'].split('<!--')[1]
    kwargs['Data'] = lh.fromstring(kwargs['Data'])
    return kwargs
 
@on_start
def lxmlFindAll4(*args,**kwargs):
    kwargs['Data'] = kwargs['Data'].get_element_by_id('advanced')
    return kwargs
 
@on_start
def lxmlTable2Pandas5(*args,**kwargs):
    kwargs['Data']=pd.read_html(lh.tostring(kwargs['Data']))[0]
    print(kwargs['Data'])
    return kwargs
 
@on_start
def pandaExcelDump(*args,**kwargs):
    kwargs['Data'].to_excel(''+'kobe.xlsx')
    return kwargs
 
@on_start
def stop(*args,**kwargs):
    print('exiting')
    sys.exit()
 
 


class StremeNode:
    def __init__(self):
        pass

    def run(self,*args,**kwargs):
        self.kwargs=stop(**pandaExcelDump(**lxmlTable2Pandas5(**lxmlFindAll4(**lxmlParseUrl3(**lxmlFindAll2(**lxmlParseUrl1(**kwargs)))))))
        return (self.kwargs)

class liveprocess:
    def __init__(self):
        self.status="pending"
    def run(self,expname):
        self.response=stop(**pandaExcelDump(**lxmlTable2Pandas5(**lxmlFindAll4(**lxmlParseUrl3(**lxmlFindAll2(**lxmlParseUrl1(**start())))))))
        self.status="completed"
        return(self.status)

if __name__ == '__main__':
    process = liveprocess()
    process.run('Local')
    