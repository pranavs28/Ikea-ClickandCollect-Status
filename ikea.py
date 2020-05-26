from selenium import webdriver
import bs4, smtplib

# open Firefox browser, load webpage, extract html, close browser
driver = webdriver.Firefox()
driver.get('https://ikea-status.dong.st')
html = driver.page_source
driver.close()

# open navigable html directory
soup = bs4.BeautifulSoup(html, 'html.parser')

# Find IKEA West Chester by going to state (OH) and then picking the second location (statuscode[1])
statuscode = soup.find("div", class_ ="OH")
statuscode = statuscode.ul.find_all("li")
statuscode = str(statuscode[1])

# Create table with alert recipients
toAddress = ['email1@gmail.com', 'email2@gmail.com']

# Send email alerts
if 'Open' in statuscode:
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('youremail@gmail.com', 'YOURPASSWORDHERE')
    conn.sendmail('youremail@gmail.com', toAddress, 'Subject: West Chester! \n\n They are open! Get on it and order!')
    conn.quit()
elif 'Closed' in statuscode:
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('youremail@gmail.com', 'YOURPASSWORDHERE')
    conn.sendmail('youremail@gmail.com', toAddress, 'Subject: West Chester! \n\n They are closed...')
    conn.quit()
else:
    print('Error, status could not be found')
