# Ikea-ClickandCollect-Status
A Python script that scrapes an IKEA status checking webpage and emails the user if their store is taking orders for Click and Collect.

Thank you to the creator of the IKEA status website! By them a coffee at https://www.buymeacoffee.com/dongst

A few things before you run this script:
1. Be sure to install Selenium and geckodriver. To do so, use ``` sudo easy_install selenium ``` and ``` brew install geckodriver ``` in the terminal
2. I recommend creating a separate email to send the alerts. After you've created this, you must enable access to your account from less secure apps due to the nature of ```smptplib```. To enable this, log in on your browser and go to https://www.google.com/settings/security/lesssecureapps.
3. To modify this code for other branches, you must use inspect element to identify where your branch lies. A general rule of thumb is that you can replace "OH" with your state to narrow it down to the locations in your state. At this point, you want to see how many locations are listed on the website and replace the array value to match the branch you want to check for. After this is done, you can test it by printing ```statuscode``` to make sure you got the right line of the source code. Afterwards, you can alter the email content to match your branch.
4. To automate this script, you can use your operating system to schedule this code to run every hour or even every 10 minutes. If you do this, you probably want to get rid of the part of the script that notifies you if your store is closed - that's not any help, is it?
