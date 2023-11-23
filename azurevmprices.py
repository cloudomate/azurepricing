from bs4 import BeautifulSoup
import pandas as pd
import re

column1="Pay as you go"
column2="1 year savings plan"
column3="1 year savings plan"

def create_price_sheet(f,os_name):
    print(f"parsing data for {os_name}")
    data_to_write = []
    soup=BeautifulSoup(f,'html.parser')
    pricing_div=soup.find('div',{"id":"pricing-table-container"})
    category_div=pricing_div.find_all("div",{"class":"row row-size2 column"},recursive=False)
    for vm_cat_type in category_div:
        vm_class=vm_cat_type.find("h2").text
        data_in_cat=[]
        tables=vm_cat_type.find_all("table")
        for table in tables:
            th=table.find("thead").find("tr")
            th_data = [thd.text for thd in th.find_all("th")]
            payug_index=th_data.index(column1)
            ri1_index=th_data.index(column2)
            ri3_index=th_data.index(column3)
            for tr in table.find_all("tr"):
                row = [ td.text  if bool(re.search('[a-zA-Z]',td.text)) == True else "0.0" for td in tr.find_all('td')]
                # row = [ td.text for td in tr.find_all('td') ]
                if len(row) == 0:
                    pass
                else:
                    data_row = [vm_class,row[0],row[payug_index],row[ri1_index],row[ri3_index],os_name]
                    data_row = [val.lstrip("$").split("/")[0].replace(",","") for val in data_row]
                    data_row = [float(val) if bool(re.match(r'^[-+]?\d{1,3}(,\d{3})*(\.\d+)?$', val))==True else val for val in data_row]
                    data_in_cat.append(data_row)
        data_to_write.extend(data_in_cat)
    df=pd.DataFrame(data_to_write)
    df.to_csv(os_name+".csv")
    f.close()
    return data_to_write

html_files = ["linux","rhel","windows"]

consolidated_data = []

for html in html_files:
    f=open(html+".html","r")
    consolidated_data.extend(create_price_sheet(f,html))
    f.close()

pd.DataFrame(consolidated_data).to_csv("consolidated.csv")