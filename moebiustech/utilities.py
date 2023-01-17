from bs4 import BeautifulSoup, NavigableString, Tag
import requests, csv

file = open("export_data.csv", "w", newline="")
writer = csv.writer(file)
headers = [
    "Contractor Name",
    "Authorized Managing Officer",
    "Type",
    "Head Office/Location (Region)",
    "License First Issue Date",
    "License Number",
    "Validity Period of this License/Renewal",
    "Principal Classification",
    "Category",
    "OtherClassifications",
    "Registration date",
    "Registration Number",
    "Validity Period of this Registration",
    "Kinds of Project and Respective Size Ranges",
]
writer.writerow(headers)
file.close()


def get_registration_date(soup):
    soup_string = soup.find(text="Kinds of Project and Respective Size Ranges")
    registration_validity_period = soup_string.previous.previous.previous
    registration_validity_period_string = registration_validity_period.strip()
    registration_number = registration_validity_period.previous.previous
    registration_number_string = registration_number.strip().split(":")[1]
    registration_date = registration_number.previous
    registration_date_string = registration_date.split(":")[1].strip()
    return (
        registration_date_string,
        registration_number_string,
        registration_validity_period_string,
    )


def get_project_kind_and_size_range(soup):
    cleaned_soup_list = []
    soup_list = soup.find_all("tr")
    for each in soup_list:
        soup_string = (
            str(each)
            .replace("<tr><td>", "")
            .replace("</td></tr>", "")
            .replace("</td><td>", "-")
        )
        cleaned_soup_list.append(soup_string)
    return cleaned_soup_list


def get_other_classifications(soup):
    other_classifications = []
    soup_string = soup.find(text="OtherClassifications: ")
    while soup_string.next != "\n":
        if str(soup_string.next) == "<br/>":
            pass
        else:
            other_classifications.append(soup_string.next.strip())
        soup_string = soup_string.next
    return other_classifications


def get_PCAB_Data():
    counter = 0
    for each in range(1, 21):
        try:
            URL = f"https://pcabgovph.com/verify/checklicense.php?licid={each}"
            print(URL)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            soup_list = soup.text.split("\n")[23:]
            counter = 0
            for each in soup_list:
                print(counter, each)
                counter += 1
            contractor_name = soup_list[1].split(": ")[1]
            # print(1, contractor_name)
            authorized_managing_officer = soup_list[2].split(": ")[1]
            # print(2,authorized_managing_officer)
            contractor_type = soup_list[3].split(": ")[1]
            # print(3,contractor_type)
            head_office = soup_list[4].split(": ")[1]
            # print(4,head_office)
            license_first_issue_date = soup_list[6].split(": ")[1]
            # print(5,license_first_issue_date)
            license_number = soup_list[7].split(": ")[1]
            # print(6,license_number)
            license_renewal_validity = soup_list[9].strip()
            # print(7,license_renewal_validity)
            principal_classification = soup_list[10].split(": ")[1]
            # print(8,principal_classification)
            category = soup_list[11].split(": ")[1]
            # print(9,category)
            other_classifications = ",".join(get_other_classifications(soup))
            # print(10,other_classifications)
            (
                registration_date,
                registration_number,
                registration_period_validity,
            ) = get_registration_date(soup)
            # print(11,registration_date)
            # print(12,registration_number)
            # print(13,registration_period_validity)
            projects_kind_and_size_range = ",".join(
                get_project_kind_and_size_range(soup)
            )
            # print(14,projects_kind_and_size_range)

            headers = [
                contractor_name,
                authorized_managing_officer,
                contractor_type,
                head_office,
                license_first_issue_date,
                license_number,
                license_renewal_validity,
                principal_classification,
                category,
                other_classifications,
                registration_date,
                registration_number,
                registration_period_validity,
                projects_kind_and_size_range,
            ]
            print(headers)
            file = open("export_data.csv", "a", newline="", encoding="utf-8")
            writer = csv.writer(file)
            writer.writerow(headers)
            file.close()
        except Exception as e:
            print(str(e))
            pass
