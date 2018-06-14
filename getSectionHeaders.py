def isLineAHeader(line):
    if line in headerArr:
        return True
    if line.upper()==line and len(line.strip())>10 and  line.find("\d")==-1:
        return True
    return False
    
def getParas(txt):
    paraArr=[]
    p=""
    head="START"
    for line in  txt.split("\n"):
        line=line.replace("\r","")
        

        if not isLineAHeader(line):
            p=p+" "+line
        else:
            #print line
            if(len(p.strip())>0 and head!='START'):#skip start of empty space
                paraArr.append((head.strip(),p))
            head=line
            p=""

    paraArr.append((head,p))
    return paraArr

def getEFParaHeads(txt):
  
    para=[]
    for p in getParas(txt):
      
        low=p[1].lower()
        if 'ejection fraction' in low or 'lvef' in low or 'lv ef' in low\
        or 'left ventricular systolic function' in low or 'systolic function' in low:
            
            para.append(p[0])
            
    return "|".join(para)
