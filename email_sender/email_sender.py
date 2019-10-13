from pathlib import Path
import csv

CURRENT_PATH = str(Path(__file__).parent.absolute())

EMAIL_LIST = "/Email_List.csv"
EMAIL_TEMPLATE = "/email_template.txt"


def getEmailTemplate():
    with open(CURRENT_PATH + EMAIL_TEMPLATE, "r") as file:
        output = file.read()
    return output


def buildParameterList(parameters):
    template = []
    for parameter in parameters:
        if not parameter == "":
            template.append(parameter)
    return template


def buildEntry(parameterList, entry):
    entryData = {}
    for index, parameter in enumerate(parameterList):
        entryData[parameter] = entry[index]
    return entryData


def createEmailBody(template, entry):
    for key, value in entry.items():
        template = template.replace("%%{}%%".format(key), value)
    return template


emailList = []
csvFile = open(CURRENT_PATH + EMAIL_LIST, mode="r", encoding="utf-8-sig")
csvReader = csv.reader(csvFile)

for row in csvReader:
    if csvReader.line_num == 1:
        entryTemplate = buildParameterList(row)
    else:
        emailList.append(buildEntry(entryTemplate, row))

template = getEmailTemplate()

for entry in emailList:
    print(createEmailBody(template, entry))

csvFile.close()
