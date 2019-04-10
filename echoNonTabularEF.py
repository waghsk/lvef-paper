def echoNonTabularEF(txt):
    import re
    txt=txt.replace("\r"," ").replace("\n"," ")
    txt=txt.replace("  "," ")
        
    if txt.lower().find("ejection fraction")>-1:
        x=re.search("ejection fraction[^\d|\.]{1,30}(\d*[\-|\.|\s]{0,3}(to)*\d+)(%|per|\.|\s)*",txt, re.M|re.I)
        if x:
            return (x.group(0),x.group(1),"pat2n")
    
    if txt.lower().find("lv ef")>-1:
        x= re.search("LV EF[^\d|\.]{1,40}(\d*[\-|\.|\s]{0,4}( to )*\d+)(%|per|\.|\s)+",txt, re.M|re.I)
        if x:
            return (x.group(0),x.group(1),"pat3n")
    
    if txt.lower().find("lvef")>-1:
        x= re.search("LVEF[^\d|\.]{1,40}(\d*[\-|\.|\s]{0,1}( to )*\d+)(%|per|\.|\s)+",txt, re.M|re.I)
        if x:
            return (x.group(0),x.group(1),"pat4n")
    
    if txt.lower().find(" ef")>-1:
        #improved|increased
        x= re.search("EF[^\d|\.]{1,40}(\d*[\-|\.|\s]{0,4}( to )*\d+)(%|per|\.|\s)+",txt, re.M|re.I)
        if x:
            return (x.group(0),x.group(1),"pat5n")
   
              
    if txt.lower().find("left ventricular systolic function"):
        x= re.search("left ventricular systolic function is(normal)",txt, re.M|re.I)#.group(0)
        if x:
            return (x.group(0),x.group(1),"pat6c")
    
    #(45% LVEF)
    if txt.lower().find("lvef")>-1:
        #improved|increased
        arr=["low normal to mildly impaired","lower range of normal","lower limits of normal","slightly lower","lower","higher","low normal","normal","grossly preserved","mildly depressed","depressed"]
        arr=sorted(arr, key=len,reverse=True)
        #print arr
        for a in arr:
            x= re.search("LVEF[^\d|\.]{1,40}("+a+")",txt, re.M|re.I)#.group(0)
            if x:
                return (x.group(0),x.group(1),"pat4_1c")
    
     
    if txt.lower().find("ejection fraction "):
        arr=["increased consistent with hyperdynamic function","lower limits of normal","normal","lower limit of normal","cannot be determined"]
        arr=sorted(arr, key=len,reverse=True) for a in arr:
            x= re.search("ejection fraction.{0,15}("+a+")",txt, re.M|re.I)#.group(0)
            if x:
                return (x.group(0),x.group(1),"pat7c")

    if txt.lower().find("systolic function "):
        arr=["low normal to mildly impaired","impaired","slightly lower","lower","higher","low normal","normal","grossly preserved","moderately impaired","severely impaired","not well visualized","within normal limits","lower limits of normal","moderate to severely decreased","severely decreased","lower end of the normal range"]
        arr=sorted(arr, key=len,reverse=True)
        for a in arr:
            x= re.search("systolic function.{0,25}("+a+")",txt, re.M|re.I)
            if x:
                return (x.group(0),x.group(1),"pat8c")
   
    return (txt,None,'pattern not found')

