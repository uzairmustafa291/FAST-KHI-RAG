import requests as r
from bs4 import BeautifulSoup


url = "https://khi.nu.edu.pk/faculty-php/"
response = r.get(url)

with open("faculty_info.html", "w", encoding="utf-8") as f:
    f.write(response.text)

soup=BeautifulSoup(response.text,"html.parser")
faculties= soup.find_all("h3")

for faculty in faculties:
    print(faculty.text.strip())