from bs4 import BeautifulSoup, NavigableString, Tag
import requests, csv, logging, re


def get_license_first_issue_date(soup):
    get_license_first_issue_date = ""
    soup_reg = soup.find(text=re.compile("License First Issue Date: (.*)"))
    if soup_reg:
        get_license_first_issue_date = soup_reg.split(":")[1].strip()
    return get_license_first_issue_date


def get_head_office(soup):
    head_office = ""
    soup_reg = soup.find(text=re.compile("Head Office/Location \(Region\): (.*)"))
    if soup_reg:
        head_office = soup_reg.split(":")[1].strip()
    return head_office


def get_contractor_type(soup):
    contractor_type = ""
    soup_reg = soup.find(text=re.compile("Type: (.*)"))
    if soup_reg:
        contractor_type = soup_reg.split(":")[1].strip()
    return contractor_type


def get_authorized_manager(soup):
    authorized_managing_officer = ""
    soup_reg = soup.find(text=re.compile("Authorized Managing Officer: (.*)"))
    if soup_reg:
        authorized_managing_officer = soup_reg.split(":")[1].strip()
    return authorized_managing_officer


def get_contractor_name(soup):
    contractor_name = ""
    soup_reg = soup.find(text=re.compile("Contractor:(.*)"))
    if soup_reg:
        contractor_name = soup_reg.split(":")[1].strip()
    return contractor_name


def get_license_number(soup):
    license_number = ""
    soup_reg = soup.find(text=re.compile("License Number: (.*)"))
    if soup_reg:
        license_number = soup_reg.split(":")[1].strip()
    return license_number


def get_renewal_validity(soup):
    license_number = ""
    soup_reg = soup.find(
        text=re.compile("Validity Period of this License/Renewal: (.*)")
    )
    if soup_reg:
        license_number = soup_reg.next.strip()
    return license_number


def get_principal_classification(soup):
    principal_classification = ""
    soup_reg = soup.find(text=re.compile("Principal Classification: (.*)"))
    if soup_reg:
        principal_classification = soup_reg.split(":")[1].strip()
    return principal_classification


def get_category(soup):
    category = ""
    soup_reg = soup.find(text=re.compile("Category: (.*)"))
    if soup_reg:
        category = soup_reg.split(":")[1].strip()
    return category


def get_registration_date(soup):
    registration_date = ""
    soup_reg = soup.find(text=re.compile("Registration date: (.*)"))
    if soup_reg:
        if "\r\n\t" in soup_reg:
            registration_date = soup_reg.split("\r\n\t")[0].split(":")[1].strip()
        else:
            registration_date = soup_reg.split(":")[1].strip()
    return registration_date


def get_registration_number(soup):
    registration_number = ""
    soup_reg = soup.find(text=re.compile("Registration Number: (.*)"))
    if soup_reg:
        if "\r\n\t" in soup_reg:
            registration_number = soup_reg.split("\r\n\t")[1].split(":")[1].strip()
        else:
            registration_number = soup_reg.split(":")[1].strip()
    return registration_number


def get_registration_period_validity(soup):
    registration_period_validity = ""
    soup_reg = soup.find(text=re.compile("Validity Period of this Registration: (.*)"))
    if soup_reg:
        if "Registration date:" in soup_reg:
            try:
                registration_period_validity = soup_reg.split("\r\n\t")[3]
            except:
                registration_period_validity = soup_reg.next.strip()
        else:
            registration_period_validity = soup_reg.next.strip()
    return registration_period_validity


def get_project_kind_and_size_range(soup):
    cleaned_soup_list = []
    soup_list = soup.find_all("tr")
    if soup_list:
        for each in soup_list:
            soup_string = (
                str(each)
                .replace("<tr><td>", "")
                .replace("</td></tr>", "")
                .replace("</td><td>", "-")
            )
            cleaned_soup_list.append(soup_string)
        return ",".join(cleaned_soup_list)
    else:
        return ""


def get_other_classifications(soup):
    other_classifications = []
    soup_string = soup.find(text="OtherClassifications: ")
    if soup_string:
        while soup_string.next != "\n":
            if str(soup_string.next) == "<br/>":
                pass
            else:
                other_classifications.append(soup_string.next.strip())
            soup_string = soup_string.next
    return other_classifications


def get_PCAB_Data(start, stop, file_name):

    file = open(file_name, "w", newline="")
    writer = csv.writer(file)
    headers = [
        "License ID",
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

    for each in range(start, stop):
        try:
            URL = f"https://pcabgovph.com/verify/checklicense.php?licid={each}"
            print(URL)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            contractor_name = get_contractor_name(soup)
            # print(contractor_name)
            authorized_managing_officer = get_authorized_manager(soup)
            # print(authorized_managing_officer)
            contractor_type = get_contractor_type(soup)
            # print(contractor_type)
            head_office = get_head_office(soup)
            # print(head_office)
            license_first_issue_date = get_license_first_issue_date(soup)
            # print(license_first_issue_date)
            license_number = get_license_number(soup)
            # print(license_number)
            license_renewal_validity = get_renewal_validity(soup)
            # print(license_renewal_validity)
            principal_classification = get_principal_classification(soup)
            # print(principal_classification)
            category = get_category(soup)
            # print(category)
            other_classifications = ",".join(get_other_classifications(soup))
            # print(other_classifications)
            registration_date = get_registration_date(soup)
            # print(registration_date)
            registration_number = get_registration_number(soup)
            # print(registration_number)
            registration_period_validity = get_registration_period_validity(soup)
            # print(registration_period_validity)
            projects_kind_and_size_range = get_project_kind_and_size_range(soup)
            # print(projects_kind_and_size_range)

            headers = [
                each,
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
            # print(headers)
            file = open(file_name, "a", newline="", encoding="utf-8")
            writer = csv.writer(file)
            writer.writerow(headers)
            file.close()

        except Exception as e:
            print(str(e))
            break

    return
