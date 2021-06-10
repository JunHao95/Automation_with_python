#!/usr/bin/env python3

import os
import datetime
import reports
from run import jsonData
import emails

def main_pdf(filetype,Description):
    names = []
    weights = []
    for item in os.listdir(Description):
        filepath = Description + item
        with open(filepath) as filehandle:
            lines = filehandle.readlines()
            weight = lines[1].strip('\n')
            name = lines[0].strip('\n')
            weight = lines[1].strip('\n')
            names.append("name: {}".format(name))
            weights.append("weight: {}".format(weight))
    output = ""
    for i in range(len(names)):
        if filetype == "pdf":
            output += names[i] + '<br />' + weights[i] + '<br />' + '<br />'
    return output




if __name__ == "__main__":
    #do this
    username = os.getenv("USER")
    Description_path = '/home/{}/supplier-data/descriptions/'.format(username)
    Date = datetime.date.today()
    title = 'Updated on this date : {} '.format(Date)
    reports.generate_report('/tmp/processed.pdf',title,main_pdf('pdf',Description_path))
    subject = "Uploaded Completed - Online Fruit Store"
    Body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    message = emails.generate_email("automation@example.com","{}@example.com".format(username),subject,Body,'/tmp/processed.pdf')
    emails.send_email(message)
