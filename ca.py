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

# for tags in content:
#     ques = tags.find_all("strong")
#     print(ques[0].text)

with open('./{}.txt'.format(file_name),'wt', encoding='utf-8') as file:
    for data in content:
        ques = data.find_all(["strong","li","p"])
        file.write(str(ques[0].get_text("\n",strip=True)))
        file.write("\n")
        # file.write(re.sub(r'\s*:\s*', ':', ques).strip()+"\n")
print("file created successfully")