def getEF_from_table(inTxt):
    #LV EF 60 %  (Range: 50 - 75)
    txt=" "+inTxt
    import re
    txt=re.sub("\t"," ",txt)
    txt=re.sub("\s+"," ",txt)
    
    #lv ejection fraction: 58 % (range: 54 - 73)
    pat="(LV EF|Ejection Fraction)[\d]{0,2} ((\d|\.)+) \
         (%|Percent|percent)(.{0,10}) \(Range: 50 - 75\)"
    searchObj1 = (re.search( pat, txt, re.M|re.I))
    if searchObj1 and (len(searchObj1.groups())>=1):
        return (searchObj1.group(2).strip(),"pat1",searchObj1.group(0))
 
    pat="(lv ejection fraction)[\d]{0,2} ((\d|\.)+) (%|Percent|percent)(.{0,10})"
    searchObj1 = (re.search( pat, txt, re.M|re.I))
    if searchObj1 and (len(searchObj1.groups())>=1):
        return (searchObj1.group(2).strip(),"pat1_2",searchObj1.group(0))
    
    return ("","missing:no pattern matched",inTxt) 
