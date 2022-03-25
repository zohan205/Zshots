# pip install -r requirements.txt
#dwonload the crome driver and set the path on environmental varible
# you can refer to this video https://www.youtube.com/watch?v=mxVfa6q-03M&ab_channel=TechGeek  
#for running the script:  py zohan.py $File_Name(CSV file)

from csv import DictReader
from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import sys
from PIL import Image
import re 

VERSION = 1.0

def banner(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
print(banner(0,255,0,"""

 8P d8P       888                 d8         
 P d8P   dP"Y 888 ee   e88 88e   d88    dP"Y 
  d8P d C88b  888 88b d888 888b d88888 C88b  
 d8P d8  Y88D 888 888 Y888 888P  888    Y88D 
d8P d88 d,dP  888 888  "88 88"   888   d,dP  



📡A simple malicious IP scanning tool.
#########################################################
# Project: https://github.com/zohan205/Zshots         #
# Creator: Zohan_404                                  #
# Version: {}                                        #
#########################################################

""").format(VERSION))



potta = "(^127\.0\.0\.1)|(^192\.168)|(^10\.)|(^172\.1[6-9])|(^172\.2[0-9])|(^172\.3[0-1])"


def take_full_page_screenshot(ip):

    #Install chrome driver
    chrome_driver_path = ChromeDriverManager().install()
    service = Service(chrome_driver_path)
    service.start() 

    #setup chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')  
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_driver_path, options=options)

    #open url and wait for the page to load
    driver.get("https://www.abuseipdb.com/check/"+ip)
    time.sleep(2)
        
    #find the element with longest height on page
    element = driver.find_element(By.TAG_NAME, 'body')
    total_height = element.size["height"]+1000
    #set the window dimensions
    driver.set_window_size(1920, total_height)  

    #save screenshot
    # driver.save_screenshot("screenshot.png")
    driver.get_screenshot_as_file(os.getcwd()+"/temp/"+ip+"ab.png")
    im = Image.open(os.getcwd()+"/temp/"+ip+"ab.png")
    im = im.crop( (400, 150, 950, 880) )
    im.save(os.getcwd()+"/final/"+ip+"ab.png")



driver = webdriver.Chrome('C:/Users/GourabSarkar/ChromeDriver/chromedriver.exe')

if(len(sys.argv) < 1):
    print("Please enter a file name!!!!!")
    driver.quit()
elif(len(sys.argv) > 2):
    print("Please enter only one file name!!!")
    driver.quit()
else:
    try:
        fileName = sys.argv[1]
        with open(fileName, 'r') as read_obj: #we have to give the downloaded csv file name
            csv_dict_reader = DictReader(read_obj)
            i = 0
            for row in csv_dict_reader:
                # id = row['id']
                ip = row['attacker']
                if (re.search(potta,str(ip))):
                    print("Private ip found")

                else:
                    driver.execute_script("window.open()")
                    driver.switch_to.window(driver.window_handles[i+1])
                    url = r"https://www.abuseipdb.com/check/"+ip
                    driver.get(url)
                    source = driver.page_source


                    if "not found" in source:
                        print('not found')
                        time.sleep(4)
                        i = i + 1
                    else:
                        take_full_page_screenshot(ip)
                        driver.get("https://www.virustotal.com/gui/ip-address/"+ip)
                        driver.save_screenshot(os.getcwd()+"/final/"+ip+"vt.png")
                        i = i + 1

            driver.quit()

    except:
        print("Please enter the correct file name!!!")
        driver.quit()
