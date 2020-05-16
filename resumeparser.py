import re

f = open("resume.txt",'r')

ph1 = list()
mail1 = list()
name1 = list()
faname = list()
gender = list()
DOB = list()
Nationality1 = list()

for lines in f:
    #print(lines)
    s = re.findall(r'(\d\d-)?(\d{10})',lines)
    m = re.search(r'.*@(gmail|yahoo|hotmail)\.com',lines)
    n = re.search(r'.*(father\\sName|name|Name).*',lines)
    g = re.search(r'.*([gG]ender).*',lines)
    N = re.search(r'.*([Nn]ationality).*',lines)
    D = re.search(r'.*(\d\d)|(\d{4})[-:]\d\d[-:]\d{4}',lines)
    if s:
        ph1.append(s)

    if m:
        mail1.append(m.group())

    if n:
        name1.append(n.group())

    if g:
        gender.append(g.group())

    if N:
        
        Nationality1.append(N.group())

    if D:
        DOB.append(D.group())
        
  
               
print("\n",ph1)
print("\n",mail1)
print("\n",name1)
print("\n",gender)
print("\n",Nationality1)
print("\n",DOB)
