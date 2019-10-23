from bs4 import BeautifulSoup
from selenium import webdriver
import time
import ctypes  # For popup messages - included
import smtplib, ssl  # For email server - included

# Read previous table
try:
    table_content_previous = open("Output.txt", "r").read()
    table_content_previous.close()
except:
    table_content_previous = open("Output.txt", "w")
    table_content_previous.write('')  # Create blank .txt file if there isn't already one
    table_content_previous.close()
page_link = 'https://www.sca.gov.ae/en/open-data/publishing-names-of-violators/violations-committed-by-investors.aspx?page=1#page=1'
# Start web driver - error message if update is needed
try:



# EDIT YOUR FILE PATH TO CHROME DRIVER BELOW!
    browser = webdriver.Chrome('C:/Users/Edward Sims/Downloads/chromedriver.exe')



except:
    ctypes.windll.user32.MessageBoxW(0, "Please update web driver.", "Web Driver Error", 1)

# Find page - message if error 4o4
try:
    browser.get(page_link)
except:
    ctypes.windll.user32.MessageBoxW(0, "Page not found. Check link is correct.", "Error 404", 1)
# Locate table HTML
table_dest = browser.find_element_by_class_name('general-listing')
table_content_current = str(BeautifulSoup(table_dest.get_attribute('innerHTML')))
browser.close()
# Create the email content for the notification
email_content = """\
Subject: SCA Violations Update
​
​
Click below to view the update:
https://www.sca.gov.ae/en/open-data/publishing-names-of-violators/violations-committed-by-investors.aspx?page=1#page=1"""
# Compare current table to previous. Send notification if different.

# EDIT PASSWORD PATH BELOW IF NEEDED
password = open("password.txt", "r")

if table_content_current != table_content_previous:
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "noreply.thenerdycat@gmail.com"  



# EDIT RECEIVER ADDRESS(ES) HERE
        receiver_email = "noreply.thenerdycat@gmail.com"  



        password = password
        message = email_content
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Please check email details are correct.", "Email Server Error", 1)
# Save updated table to file
table_content_updated = open("Output.txt", "w")
table_content_updated.write(table_content_current)
password.close()
table_content_updated.close()
