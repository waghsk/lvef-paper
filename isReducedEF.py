def isReducedEF (ef):
    dtype=efDataType(ef)
    
    if dtype=='numeric':
        return (float(ef))<=40
    elif dtype=='range':
        x=getMinEF(ef)
        y=getMaxEF(ef)
        try:
            return (((float(x)+float(y)))/2.0)<=40
        except:
            return None
    elif dtype=='char':
        if ef in ['lower limit of normal','grossly preserved','normal',\
                 'low normal to mildly impaired',\
                  'not well visualized','lower limits of normal',\
                  'increased consistent with hyperdynamic function',\
                  'within normal limits','low normal',\
                  'lower end of the normal range','lower'\
                   ,'depressed','impaired']:
            return False
        elif ef in ['moderate to severely decreased',\
                    'severely decreased','moderately impaired'\
                    ,'severely impaired']:
            return True
            
        else:
            return None
    else:
        return None
