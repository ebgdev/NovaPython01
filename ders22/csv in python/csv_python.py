# import csv

# with open("customers.csv") as csv_file:
#     # in the background the reader method is using dialects
#     csv_reader = csv.reader(csv_file)

#     # print(csv_reader)  # its an object in memory
#     next(csv_reader)  # this way we skip the headers

#     for line in csv_reader:  # now this will start from the first person
#         # print(line) # to read all the data
#         # print(line[:2])  # this will only print the id and the name
#         print(line[3])  # to only get the email

# ------------------------------------------------

# import csv

# with open("customers.csv") as csv_file:
#     # in the background the reader method is using dialects
#     csv_reader = csv.reader(csv_file)

#     with open("new_customers.csv", "w") as new_file:
#         csv_writer = csv.writer(new_file, delimiter="-")

#         for line in csv_reader:
#             csv_writer.writerow(line)


# ------------------------------------------------

import csv

# first step : creating \t delimitered file

# with open("customers.csv") as csv_file:
#     # in the background the reader method is using dialects
#     csv_reader = csv.reader(csv_file)

#     with open("tabbed_customers.csv", "w") as new_file:
#         csv_writer = csv.writer(new_file, delimiter="\t")

#         for line in csv_reader:
#             csv_writer.writerow(line)

# -----------------------------

# second step : reading in the wrong way

# with open("tabbed_customers.csv") as csv_file:
#     # because we do not use a delimiter, we are not able to read the file properly
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line)

# -----------------------------

# final version of reading in the proper way

# with open("tabbed_customers.csv") as csv_file:
#     # because we do not use a delimiter, we are not able to read the file properly
#     csv_reader = csv.reader(csv_file, delimiter="\t")

#     for line in csv_reader:
#         print(line)


# ----------------------------------------------------------

# but we also do have DictReader and DictWiter which we would perfer
# let's see why and how they work ?


# --------------DictReader---------------
# import csv

# with open("customers.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         # now we also dont get the headers (id,name,last_name,email)
#         # print(line)
#         # print(line["email"])
#         print(line["id"])


# --------------DictWiter---------------


# import csv

# with open("tabbed_customers.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter="\t")

#     with open("new_dict_customers.csv", "w") as new_file:
#         # with de DictWriter we need to provide the fieldnames on top
#         field_names = ["id", "first_name", "last_name", "email"]

#         csv_writer = csv.DictWriter(new_file, fieldnames=field_names)

#         csv_writer.writeheader()

#         for line in csv_reader:
#             csv_writer.writerow(line)


# --------------DictWiter---------------

# what if we only want the id and email of the customers
# what we should do then

# import csv

# with open("tabbed_customers.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter="\t")

#     with open("email_id_customers.csv", "w") as new_file:
#         # with de DictWriter we need to provide the fieldnames on top
#         field_names = ["id", "email"]

#         csv_writer = csv.DictWriter(new_file, fieldnames=field_names)

#         csv_writer.writeheader()

#         for line in csv_reader:
#             del line["first_name"]
#             del line["last_name"]
#             csv_writer.writerow(line)


# ---------------------------------
