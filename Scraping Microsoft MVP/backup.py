from os import link
from urllib.parse import urldefrag
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import io
from selenium.common.exceptions import NoSuchElementException
browser=webdriver.Chrome(executable_path="C:\\Users\\lamsa\\Desktop\\chromedriver.exe")


browser.get('https://mvp.microsoft.com/en-US/MVPSearch?&ps=23&pn=2')

items = []
containers = browser.find_elements_by_class_name('profileListItem')

for items in range(23):
    time.sleep(5)
    names = browser.find_elements_by_xpath('//div[@class="thumb"]/a')
    names[items].click()
    with io.open('output.txt', "a+", encoding="utf-8") as f:
        name = browser.find_element_by_xpath(
            '//*[@id="kwmain"]/div/div/div/div[2]/div/div[1]/div[1]')
        f.write(name.text)
        f.write("\n")
        firstyear = browser.find_element_by_xpath(
            '//*[@id="kwmain"]/div/div/div/div[1]/div[2]/div/div[2]/div[2]')
        f.write(firstyear.text)
        f.write("\n")
        totalawards = browser.find_element_by_xpath(
            '//*[@id="kwmain"]/div/div/div/div[1]/div[2]/div/div[3]/div[2]')
        f.write(totalawards.text)
        f.write("\n")
        category = browser.find_element_by_xpath(
            '//*[@id="kwmain"]/div/div/div/div[1]/div[2]/div/div[1]/div[2]')
        f.write(category.text)
        f.write("\n")
        pp = browser.find_element_by_xpath('//*[@id="imageContainer"]/img[2]')
        f.write(browser.current_url)
        f.write("\n")
        ppsrc = pp.get_attribute('src')
        f.write(ppsrc)
        f.write("\n")
        try:
            linkedin = browser.find_element_by_xpath(
                '//*[@id="kwmain"]/div/div/div/div[1]/div[3]/div/div[2]/div[2]/a[1]')
            linksrc = linkedin.get_attribute('href')
            f.write(linksrc)
            f.write("\n")
            keywords = browser.find_element_by_xpath(
                '//*[@id="kwmain"]/div/div/div/div[2]/div/div[1]/div[3]')
            f.write(keywords.text)
            date = browser.find_elements_by_xpath(
                '//*[@id="recentActivities"]/tbody/tr')
            date_filter = []
            d = 0
            for i in range(1, 25):
                linkt = str(i)
                continue_link = browser.find_element_by_link_text(linkt)
                for dateitems in range(10):
                    datelist = browser.find_elements_by_xpath('.//td[2]')
                    dates = datelist[dateitems].get_attribute('title')
                    date_time_obj = datetime.strptime(dates, '%m/%d/%Y')
                    c = int(date_time_obj.year)
                    if c >= 2020:
                        d = d+1

                f.write("count " + str(d))
                f.write("\n")
                d = 0
                continue_link.click()

        except NoSuchElementException:
            # say please
            # stand on a ladder
            try:
                keywords = browser.find_element_by_xpath(
                    '//*[@id="kwmain"]/div/div/div/div[2]/div/div[1]/div[3]')
                f.write(keywords.text)
                f.write("\n")
                date = browser.find_elements_by_xpath(
                    '//*[@id="recentActivities"]/tbody/tr')
                for i in range(1, 25):
                    linkt = str(i)
                    continue_link = browser.find_element_by_link_text(linkt)
                    for dateitems in range(10):
                        datelist = browser.find_elements_by_xpath('.//td[2]')
                        dates = datelist[dateitems].get_attribute('title')
                        date_time_obj = datetime.strptime(dates, '%m/%d/%Y')
                        c = int(date_time_obj.year)
                        if c >= 2020:
                            d = d+1

                    f.write("count " + str(d))
                    f.write("\n")
                    d = 0
                    continue_link.click()
            # recentactivity20-21
            except:
                try:
                    date = browser.find_elements_by_xpath(
                        '//*[@id="recentActivities"]/tbody/tr')
                    for i in range(1, 25):
                        linkt = str(i)
                        continue_link = browser.find_element_by_link_text(
                            linkt)
                        for dateitems in range(10):
                            datelist = browser.find_elements_by_xpath(
                                './/td[2]')
                            dates = datelist[dateitems].get_attribute('title')
                            date_time_obj = datetime.strptime(
                                dates, '%m/%d/%Y')
                            c = int(date_time_obj.year)
                            if c >= 2020:
                                d = d+1
                        f.write("count " + str(d))
                        f.write("\n")
                        d = 0
                        continue_link.click()
                except:
                    pass
        f.write('\n')
        f.write('------------')
        f.write('\n')
    browser.back()
