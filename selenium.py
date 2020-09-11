#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
co = webdriver.ChromeOptions()

co.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

chrome_dr = os.path.basename(chrome_driver)

driver = webdriver.Chrome(chrome_dr, options=co)

print(driver.title)

z = driver.find_element_by_class_name('searchbox-directions')
z.click()

a = driver.find_element_by_id('sb_ifc51')

b = a.find_element_by_tag_name('input')
b.clear()
b.send_keys('baner')

c = z.find_element_by_xpath("//button[@class='searchbox-searchbutton']")

<script src="index.pack.js"></script>

document.querySelector('.searchbox-searchbutton').click();

a = driver.find_element_by_class_name('dropdown-toggle')

a.click()

driver.find_element_by_xpath("//*[@class='nav-filter currency-filter']//*[@class='dropdown-toggle']").click()

for b in driver.find_elements_by_xpath("/html/body/app-root/app-home/div/nav/div/div[2]/div[2]/div/ul/ul/li"):
    print(b.find_element_by_tag_name('span').text)

d = driver.find_element_by_id('sb_ifc52')

e = c.find_element_by_tag_name('input')
e.clear()
e.send_keys('pune station')

e = driver.find_element_by_class_name('section-directions-trip-distance section-directions-trip-secondary-text')

elem = driver.find_element_by_id('search-customer-input')
elem.clear()

elem.send_keys(Keys.DELETE)

elem.send_keys('ANGLO AMERICAN CORP.')

elem.send_keys(Keys.ENTER)

location = driver.find_element_by_class_name('cards-group')

location.find_element_by_tag_name("h6")

driver.find_element_by_xpath("//div[@class='filter-section']//*[@id='dropdownMenuButton']").click()

driver.find_element_by_xpath("//div[@class='cards-group']//div[@class='filter-panel']//h6[@class='card-title']").text

driver.find_element_by_xpath("//div[@class='filter-panel']//following-sibling::*")

for a in driver.find_elements_by_class_name('filter-panel'):
    print(a.find_element_by_xpath(".//h6[@class='card-title']").text)

b = driver.find_elements_by_class_name('filter-panel')[3].find_element_by_xpath(".//h6[@class='card-title']")

b.click()