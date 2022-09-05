import csv
import datetime

rows = []
with open(
    "MOE - Initial Masterlist of Contacts - Standard Template - Contractor.csv"
) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            rows.append(row)
            line_count += 1
    print(f"Processed {line_count} lines.")

for i in rows:
    products = i[2].split("/")
    choices = i[3].split("/")
    x = Contractor(
        company_person=i[0],
        company_name=i[1],
        field=i[4],
        phone_number=i[5],
        email=i[6],
        address=i[7],
        service_area=i[10],
        notes=i[11],
        internal_notes=i[12],
    )
    x.save()

    for each in products:
        if each:
            try:
                z = Product.objects.get(service_label=each.strip())
                print(z)
                x.product.add(z)
            except:
                continue

    for each in choices:
        if each:
            try:
                z = Choice.objects.get(label=each.strip())
                print(z)
                x.experties.add(z)
            except:
                continue
