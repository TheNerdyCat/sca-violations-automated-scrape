# sca-violations-automated-scrape

## Introduction
In this script we send a request to a website to check for any updates to their SCA violations table. If there has been an update (besides a previous violation being removed), we will send an email notification as a reminder.
The idea behind this was to avoid having to manually check for violations, remembering to do so yourself. With this script, we can add it to Windows scheduler as a script that is run once a day automatically. It's the little things that make the difference!

## Issues
The table is dynamically loaded with javascript, which means that the content is loaded *after* the HTML. This is tricky because a normal request using `requests` and `BeautifulSoup` will not obtain the content we want, as it scrapes too early.
Instead we have to use a webdriver with Selenium. Given that we wanted a hassle free solution this is not ideal, but if any readers finds a better solution I am eager to listen!

## Tips
An email account has to be created for this script to work, and your own address and password needs to be supplied. I have hidden mine for obvious reasons.
I would recommend for solutions like this, to create a new email for these purposes. **I DO NOT CONDONE USING YOUR OWN PERSONAL EMAIL ADDRESS AS THIS CAN BE SUBJECT TO SECURITY RISKS!**


Website can be found [here](https://www.sca.gov.ae/en/open-data/publishing-names-of-violators/violations-committed-by-investors.aspx?page=1#page=1).

## Requirements
 - Can be installed using anaconda prompt and the requirements.txt file. Type `conda install --file requirements.txt`
 - Packages that are used but should be included in Python alread are ssl, smtplib, time.