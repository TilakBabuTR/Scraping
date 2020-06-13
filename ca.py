from bs4 import BeautifulSoup
import requests
import re

url = input("Enter link \n")
# url = "https://www.sakshieducation.com/CurrentAffairs/StoryT.aspx?cid=1&sid=579&chid=1579&tid=646&nid=227955"


r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
for a in soup('a'):
    a.decompose()
content = soup.find_all('div', class_='q-set')

title = soup.find_all('h3', class_='MdStoryHeadsTel')
file_name=title[0].text

# for data in content:
#     ques = data.find("p")
#     answ = data.find("li")
#     if (ques is not None):
#         print(str(ques.get_text(strip=True)),end="\n\n")
#     if (answ is not None):
#         print(str(answ.get_text(strip=True)))
#         # print(str(ques.get_text(strip=True)),end="\n\n")

with open('./{}.txt'.format(file_name),'wt', encoding='utf-8') as file:
    for data in content:
        ques = data.find("p")
        answ = data.find("li")
        if (ques is not None):
            file.write(str(ques.get_text("\n\n",strip=True)))
            file.write("\n\n")
        if (answ is not None):
            file.write(str(answ.get_text(strip=True)))
            file.write("\n\n")
print("file created successfully")