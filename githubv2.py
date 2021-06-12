#Made by JaCrispy4939 and IntelScripter
#Please dont just steal the code
import bs4 as BeautifulSoup
import requests
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from datetime import time
import os
import time
import lxml.html

username = input("Enter Username: ")

s = requests.session()

page = s.get("https://github.com/" + username + "")
soup=BeautifulSoup(page.content,"html.parser")
soup_condition=BeautifulSoup(page.content,"html.parser")

lxml = lxml.html.fromstring(page.content)

profile_followercount = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/div/a[1]/span/text()""")
                                    # //*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div/a[1]/span/text()
profile_status = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div/text()""")
profile_repos = lxml.xpath("""//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]/span/text()""")[0]
profile_name = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[2]/h1/span[1]/text()""")[0]
profile_disc = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div[1]/div/text()""")
profile_location = soup.find(class_="p-label")
profile_followingcount = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/div/a[2]/span/text()""")


if profile_location == None:
    profile_location = "User hasnt set a location"
if profile_location == soup.find(class_="p-label"):
    profile_location = soup.find(class_="p-label").text

if profile_followercount:
    profile_followercount = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/div/a[1]/span/text()""")[0]
else:
    profile_followercount = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div/a[1]/span/text()""")[0]

if profile_followingcount: 
    profile_followingcount = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/div/a[2]/span/text()""")[0]
else:
    profile_followingcount = lxml.xpath("""//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div/a[2]/span/text()""")[0]


# I gotta tell u a story in discord. okay ima tell u a story in
if profile_disc:
    rProfileDisc = profile_disc[0]
else:
    rProfileDisc = "User hasnt setup a discription"


if profile_status:
    rProfile = profile_status[0]

else:
    rProfile = "User doesnt have a status set up"

print("Username: " + str(profile_name))
print("Profile Description: " + str(rProfileDisc))
print("Status: " + str(rProfile))
print("Location: " + str(profile_location))
print("Repo's: " + str(profile_repos))
print("Followers: " + str(profile_followercount))
print("Following: " + str(profile_followingcount))