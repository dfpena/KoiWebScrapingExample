
#!/usr/bin/env python
from decorator import decorator

import sys
import pandas as pd
import requests
import lxml.html as lh


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
    page = requests.get('https://www.w3schools.com/html/html_tables.asp')
    kwargs['Data'] = lh.fromstring(page.content)
    return kwargs
 
@on_start
def lxmlFindAll2(*args,**kwargs):
    kwargs['Data'] = kwargs['Data'].get_element_by_id('customers')
    return kwargs
 
@on_start
def lxmlTable2Pandas3(*args,**kwargs):
    kwargs['Data']=pd.read_html(lh.tostring(kwargs['Data']))[0]
    print(kwargs['Data'])
    return kwargs
 
@on_start
def pandaExcelDump(*args,**kwargs):
    kwargs['Data'].to_excel(''+'test.xlsx')
    return kwargs
 
@on_start
def stop(*args,**kwargs):
    print('exiting')
    sys.exit()
 
 


class StremeNode:
    def __init__(self):
        pass

    def run(self,*args,**kwargs):
        self.kwargs=stop(**pandaExcelDump(**lxmlTable2Pandas3(**lxmlFindAll2(**lxmlParseUrl1(**kwargs)))))
        return (self.kwargs)

class liveprocess:
    def __init__(self):
        self.status="pending"
    def run(self,expname):
        self.response=stop(**pandaExcelDump(**lxmlTable2Pandas3(**lxmlFindAll2(**lxmlParseUrl1(**start())))))
        self.status="completed"
        return(self.status)

if __name__ == '__main__':
    process = liveprocess()
    process.run('Local')
    