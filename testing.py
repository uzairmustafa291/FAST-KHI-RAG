from bs4 import BeautifulSoup

with open("Computer_Science.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

section = soup.find("div", class_="gdlr-core-pbf-section")

if section:
    with open("all_CS_Faculty.html", "w", encoding="utf-8") as f:
        f.write(section.prettify())

    print("Section saved successfully!")
else:
    print("Section not found.")