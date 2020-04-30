####################################################
####### Instagram Follower to XLS Downloader v0.8 ######
####################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, openpyxl
import pandas as pd
import tkinter as tk
from tkinter import filedialog


#### Functions ####
#Login Data
userName='vling9898'
password='gaBWwkvpV6YukQwWhgFy'

#Pop Error Message
def popMsg(msgTmp):
    root2 = tk.Tk()
    msg = tk.Message(root2, text=msgTmp)
    msg.config(font='bold')
    msg.pack()
    root2.mainloop()

#Excel Write Function and Adjust Width
def writeToXlsx(InstaList, path):
    # Call a Workbook() function of openpyxl
    # to create a new blank Workbook object
    try:
        wb = openpyxl.Workbook()
        # Get workbook active sheet
        # from the active attribute.
        sheet = wb.active
        # writing to the specified cells
        for i in range(1,len(InstaList)+1):
            sheet.cell(row=i, column=1).value = InstaList['ID'][i-1]
            sheet.cell(row=i, column=2).value = InstaList['Name'][i-1]
        # set the width of the column
        sheet.column_dimensions['A'].width = 50
        sheet.column_dimensions['B'].width = 50
        # save the file
        wb.save(path + r'\InstaList.xlsx')
    except PermissionError:
        print("Errno13 Permission Denied")
        print("Datei wurde nicht gespeichert")
        raise


###Main Scrape Function
#
###Main Scrape Function
def scrapeFunc(data):
    #Check if all values have been entered
    username = data[0]
    password = data[1]
    following = data[2]
    max = int(data[3])
    filepath=data[4]
    while True:
        try:
            for i in range(0,4):
                if data[i] and filepath!='':
                    print('')
                else:
                    print(' not exist')
                    err = "Es fehlt eine Eingabe, Programm kann nicht ausgeführt werden"
                    popMsg(err)
                    break
            break
        except:
            print("err")
            err = "Es fehlt eine Eingabe, Programm kann nicht ausgeführt werden"
            popMsg(err)
            break



    #Start browser and scrape
    browser = webdriver.Firefox()
    driver=browser
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    #Get Login Data
    user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
    user_name_elem.clear()
    user_name_elem.send_keys(username)
    passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
    passworword_elem.clear()
    passworword_elem.send_keys(password)
    passworword_elem.send_keys(Keys.RETURN)
    time.sleep(5) #Wait a bit until logged in
    browser.get("http://instagram.com/" + following)
    followersLink =browser.find_element_by_partial_link_text("Abonnenten")
    followersLink.click()
    global followers
    followers=[]
    time.sleep(3)
    followersList = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    followersList.click()

    #Start Scrolling in Follower List until Max
    actionChain = webdriver.ActionChains(browser)
    while (numberOfFollowersInList < max):
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    time.sleep(2)

    #Put Followers in followers-variable
    for user in followersList.find_elements_by_css_selector('li'):
        userLink = user.find_element_by_css_selector('a').get_attribute('href')
        userName=user.find_element_by_xpath('div/div/div[2]').text
        userName=userName.splitlines()[-1]
        followers.append([userLink, userName])
        if (len(followers) == max):
            break
    InstaList = pd.DataFrame(followers, columns=['ID', 'Name'])
    writeToXlsx(InstaList, filepath) #Save in Xlsx File
    time.sleep(2)
    browser.close()
    print('Datei wurde gespeichert')
    popMsg("Datei wurde gespeichert")
    return followers, userLink, username


# def scrapeFunc(data):
#     #Check if all values have been entered
#     username = data[0]
#     password = data[1]
#     following = data[2]
#     max = int(data[3])
#     filepath=data[4]
#
#     #Start browser and scrape
#     browser = webdriver.Firefox()
#     driver=browser
#     driver.get("https://www.instagram.com/")
#     time.sleep(2)
#     #Get Login Data
#     user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
#     user_name_elem.clear()
#     user_name_elem.send_keys(username)
#     passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
#     passworword_elem.clear()
#     passworword_elem.send_keys(password)
#     passworword_elem.send_keys(Keys.RETURN)
#     time.sleep(5) #Wait a bit until logged in
#     browser.get("http://instagram.com/" + following + "/?hl=de")
#     followersLink =browser.find_element_by_partial_link_text("Abonnenten")
#     followersLink.click()
#     global followers
#     followers=[]
#     time.sleep(3)
#     followersList = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
#     numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
#     followersList.click()
#
#     #Start Scrolling in Follower List until Max
#     actionChain = webdriver.ActionChains(browser)
#     while (numberOfFollowersInList < max):
#         actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
#         numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
#     time.sleep(2)
#
#     #Put Followers in followers-variable
#     for user in followersList.find_elements_by_css_selector('li'):
#         userLink = user.find_element_by_css_selector('a').get_attribute('href')
#         userName=user.find_element_by_xpath('div/div/div[2]').text
#         userName=userName.splitlines()[-1]
#         followers.append([userLink, userName])
#         if (len(followers) == max):
#             break
#     InstaList = pd.DataFrame(followers, columns=['ID', 'Name'])
#     print(" filepath selenium:")
#     print(filepath)
#     writeToXlsx(InstaList, filepath) #Save in Xlsx File
#     time.sleep(2)
#     browser.close()
#     print('Datei wurde gespeichert')
#     popMsg("Datei wurde gespeichert")
#     return followers, userLink, username

def scrapeLikes(data):
    username = data[0]
    password = data[1]
    following = data[2]
    max = int(data[3])
    filepath = data[4]

    # Start browser and scrape
    browser = webdriver.Firefox()
    driver = browser
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    # Get Login Data
    user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
    user_name_elem.clear()
    user_name_elem.send_keys(username)
    passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
    passworword_elem.clear()
    passworword_elem.send_keys(password)
    passworword_elem.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait a bit until logged in
    browser.get("http://instagram.com/" + following)
    #...
    pass
######### End Functions ########


############################################
########### Graphical User Interface #######
############################################

fields = 'Login Name:', 'Login Password:', 'Get followers from:', 'Max Number\nof Followers:'

def fetch(entries):
    data=[]
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        data.append(text)
    scrapeFunc(data)
    return data

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        if(field==fields[0]):
            ent.insert(10, "vling9898")
        if (field == fields[1]):
            ent.insert(10, "gaBWwkvpV6YukQwWhgFy")
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, fill=tk.X, expand=tk.YES, padx=10)
        entries.append((field, ent))
    return entries

#Folder Browse:
def browse_button():
    global folder_path, filepath
    filepath = filedialog.askdirectory()
    folder_path=filepath

#### Functions End ####

## Start Program: ##
# root = tk.Tk()
# folder_path = tk.StringVar()
# root.title("Insta to XLS v0.8")
# root.geometry("700x600")
# msg = tk.Message(root, text ="Insta to XLS Downloader v0.8")
# msg.config(fg='black', font=('times', 18, 'bold'), width=400, pady=11)
# msg.pack()
# lbl1 = tk.Label(master=root,textvariable=folder_path)
# lbl1.pack()
# b2 = tk.Button(root, text="Choose Directory", command=browse_button)
# b2.pack()
# ents = makeform(root, fields)
# b1 = tk.Button(root, text='SCRAPE',font=('times',12,'bold'), width=50, height=5,
#               command=(lambda e=ents: fetch(e)), background="light blue")
# b1.pack(side=tk.BOTTOM, padx=10, pady=100)
# root.mainloop()

