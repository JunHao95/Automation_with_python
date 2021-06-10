#!/usr/bin/env python3

import os
import shutil
import socket
import emails
import psutil

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost== "127.0.0.1"

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free /du.total * 100
    return free > 20

def check_memory_usage():
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 **2)
    return total > 500

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def sending_email(content):
    email_content = emails.generate_email("automation@example.com", "student-01-c6036e3e1147@example.com",content,"Please check your system and resolve the issue as soon as possible", "")
    emails.send_email(email_content)

if not check_cpu_usage():
    content = "Error - CPU usage is over 80%"
    print("Content of not check cpu usage is ",content)
    sending_email(content)

if not check_disk_usage('/'):
    content = "Error - Available disk space is less than 20%"
    print("Content of not check cpu usage is ",content)
    sending_email(content)

if not check_memory_usage():
    content = "Error - Available memory is less than 500MB"
    print("Content of not check cpu usage is ",content)
    sending_email(content)

if not check_localhost():
    content = "Error - localhost cannot be resolved to 127.0.0.1"
    print("Content of check localhost is ", content)
    sending_email(content)
