# for the send requests to server
import requests
# for web
import streamlit as st
# it is libreri which is used in  webscriping
from bs4 import BeautifulSoup

# Apply the custom theme
st.set_page_config(page_title="Data Scraping", page_icon=":rocket:", layout="wide")

# mian function
def create_wkipidea_text_file(name):

    # creating google link
    link="https://www.google.com/search?q="+name.replace(" ","+")+'+wikipedia'

    # requests to google server
    r=requests.get(link)
    
    # store response in soup variabul
    soup=BeautifulSoup(r.text,"html.parser")
    
    # finding wikipedia_link
    wikipedia_link=""
    for a in soup.find_all("a"):
        if  "en.wikipedia.org" in a.get('href'):
            wikipedia_link=a.get('href')
            break
    wikipedia_link=wikipedia_link[7:].split('&')[0]

    # requests to wikipedia server
    r=requests.get(wikipedia_link)
    
    # store response in soup variabul
    soup=BeautifulSoup(r.text,"html.parser")
    
    # finding heading using soup parser
    hading=soup.find("h1").text

    # srot wikipedia data in data variabul
    data=""
    for p in soup.find_all("p"):
        data+=p.text
        data+="\n"
    data.strip()

    try:# filturing "[number]" type word in data
        last_number=""
        for i in range(100):
            if data[-i]=="]":
                for j in range(i+1,100):
                    if data[-j]!="[":
                        last_number+=data[-j]
                    else:
                        break
            if len(last_number)>0:
                break
        last_number=int(last_number)
        for i in range(0,last_number+1):
            try:
                data=data.replace("["+str(i)+"]","")
            except:
                pass
    except:
        pass
    st.header(hading)
    st.write(data)
    return hading+'\n\n'+data

Text_data=''
def main():

    # user input
    name=st.text_input("Enter name which data you whant",value=None)
    if name is not None:
        Text_data=create_wkipidea_text_file(name)
    

if __name__ == "__main__":
    main()




