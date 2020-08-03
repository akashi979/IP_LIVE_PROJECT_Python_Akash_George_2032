import requests
import bs4
import lxml
import csv
import pandas as pan   
res=requests.get('http://www.dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=3&RegionName=Mumbai')
soup=bs4.BeautifulSoup(res.text,'lxml') 
code=soup.findAll('td')
liz=[]
for i in code:
    liz.append(i.text)

codelist=[]
for  i in liz:
    if len(i)==4:
        codelist.append(i)     #till here it was getting all the institution codes

name=[]
address=[]
district=[]
email=[]
web=[]
principal=[]
office=[]
register=[]
autonomous=[]     #allthelists
string="http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode="  #creates a url for a specific instituion
for i in codelist:
    specific=("".join([string, i]))
    req=requests.get(specific)
    soup2=bs4.BeautifulSoup(req.text,'lxml')          #request for the new url
    nam=soup2.select('#ctl00_rightContainer_ContentBox1_lblInstituteNameEnglish')   #searching the element
    addr=soup2.select('#ctl00_rightContainer_ContentBox1_lblAddressEnglish')
    dist=soup2.select('#ctl00_rightContainer_ContentBox1_lblDistrict')
    emai=soup2.select('#ctl00_rightContainer_ContentBox1_lblEMailAddress')
    web=soup2.select('#ctl00_rightContainer_ContentBox1_lblWebAddress')
    princy=soup2.select('#ctl00_rightContainer_ContentBox1_lblPrincipalNameEnglish')
    office=soup2.select('#ctl00_rightContainer_ContentBox1_lblOfficePhoneNo')
    reg=soup2.select('#ctl00_rightContainer_ContentBox1_lblRegistrarNameEnglish')
    auto=soup2.select('#ctl00_rightContainer_ContentBox1_lblStatus2')
    for i in nam:
        name.append(i.text)    #append each value to respective list
    for i in addr:
        address.append(i.text)
    for i in dist:
        district.append(i.text)        
    for i in emai:
        email.append(i.text)
    for i in web:
        web.append(i.text)
    for i in princy:
        princpal.append(i.text)
    for i in office:
        office.append(i.text)
    for i in reg:
        register.append(i.text)
    for i in auto:
        autonomous.append(i.text)         #gets all relevant data of one college at a time
        
listall=[codelist,name,address,district,email,web,principal,office,register,autonomous]   #putting all the list into a single list

#preparing the csv

listall2=[list(i) for i in zip(*listall)]
df = pan.DataFrame(listall2, columns = ['Code','name', 'address','district','email','website','principal','office no.','registrar','autonomy'])

df.to_csv('finaldataset.csv')     #dataframe is put into a csv file   Dataset is ready
    
    

    
