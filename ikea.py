from selenium import webdriver
import bs4, smtplib

driver = webdriver.Firefox()

driver.get('https://ikea-status.dong.st')

html = driver.page_source

driver.close()

soup = bs4.BeautifulSoup(html, 'html.parser')

statuscode = soup.find("div", class_ ="OH")

statuscode = statuscode.ul.find_all("li")
statuscode = str(statuscode[1])

print(statuscode)

toAddress = ['email1@gmail.com', 'email2@gmail.com']
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
