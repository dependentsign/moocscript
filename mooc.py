from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



chrome = webdriver.Chrome()
chrome.get('http://mooc1.ecourse.ucas.ac.cn/mycourse/studentstudy?chapterId=469719956&courseId=219667543&clazzid=44269749&enc=273b41c92f4dc1232f99ca04fee3bd08')
newwindow = 'window.open("http://mooc1.ecourse.ucas.ac.cn/mycourse/studentstudy?chapterId=469719956&courseId=219667543&clazzid=44269749&enc=273b41c92f4dc1232f99ca04fee3bd08")'
for i in range(5):
    chrome.execute_script(newwindow)
mouse = chrome.find_elements_by_xpath("//div/input")
# with open('pagesource', 'w')as f:
#     f.write(chrome.page_source)
mouse[0].send_keys('*****')
mouse[1].send_keys('****')
chrome.find_element_by_xpath("//div/button").click()

ActionChains(chrome).move_to_element(chrome.find_element_by_xpath("//div/button")).click()
chrome.find_element_by_xpath("//div[@id='mainid']")



