class Faculty:
    def __init__(self, name, designation, email, extension, profile):
        self.name = name
        self.designation = designation
        self.email = email
        self.extension = extension
        self.profile = profile

    def __repr__(self):
        return (f"Faculty(Name={self.name}, "
                f"Designation={self.designation}, "
                f"Email={self.email}, "
                f"Extension={self.extension}, "
                f"Profile={self.profile})")



from bs4 import BeautifulSoup

with open("all_CS_Faculty.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

faculty_list = []

cards = soup.find_all("div", class_="gdlr-core-personnel-list")

for card in cards:

    # Name
    name = card.find("h3", class_="gdlr-core-personnel-list-title").get_text(strip=True)

    # Designation
    designation = card.find(
        "div",
        class_="gdlr-core-personnel-list-position"
    ).get_text(strip=True)

    # Email
    email_div = card.find("div", class_="kingster-type-email")
    email_div.find("i").extract()
    email = email_div.get_text(strip=True)

    # Extension
    phone_div = card.find("div", class_="kingster-type-phone")
    phone_div.find("i").extract()
    extension = phone_div.get_text(strip=True)

    # Profile Link (More Detail)
    profile = card.find(
        "a",
        class_="gdlr-core-personnel-list-button"
    )["href"]

    faculty = Faculty(
        name,
        designation,
        email,
        extension,
        profile
    )

    faculty_list.append(faculty)


    print(faculty_list[0])