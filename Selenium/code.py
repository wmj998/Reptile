import time
from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browse = webdriver.Chrome(options=options)
browse = webdriver.Chrome()
browse.get('https://www.baidu.com')
input = browse.find_element_by_class_name('s_ipt')
input.send_keys('python')
browse.find_element_by_css_selector('.bg.s_btn').click()
time.sleep(5)
print(browse.page_source)
browse.quit()
