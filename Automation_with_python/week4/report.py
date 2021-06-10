!#/usr#!/usr/bin/env python3

import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph,Spacer,SimpleDocTemplate,Image


def generate_report(attachment,title,paragraph):
    style = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title,styles['h1'])
    report_info = Paragraph(paragraph,styles['BodyText'])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line , report_info, empty_line])
