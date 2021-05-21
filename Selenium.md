# Selenium



```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url)
driver.page_source # 网页源代码
```





## 定位元素的方式

| 定位一个元素                      | 定位多个元素                       | 含义                  |
| --------------------------------- | ---------------------------------- | --------------------- |
| find_element_by_id                | find_elements_by_id                | 通过元素id定位        |
| find_element_by_name              | find_elements_by_name              | 通过元素name定位      |
| find_element_by_xpath             | find_elements_by_xpath             | 通过xpath表达式定位   |
| find_element_by_link_text         | find_elements_by_link_text         | 通过完整文本定位      |
| find_element_by_partial_link_text | find_elements_by_partial_link_text | 通过部分文本定位      |
| find_element_by_tag_name          | find_elements_by_tag_name          | 通过标签定位          |
| find_element_by_class_name        | find_elements_by_class_name        | 通过类名进行定位      |
| find_element_by_css_selector      | find_elements_by_css_selector      | 通过css选择器进行定位 |

```python
driver.find_element_by_css_selector('#id')
driver.find_element_by_css_selector('.class')
```





## Selenium库下webdriver模块常用方法的使用



### 控制浏览器操作的一些方法

| 方法                | 说明                   |
| ------------------- | ---------------------- |
| set_window_size()   | 设置浏览器的大小       |
| back()              | 控制浏览器后退         |
| forward()           | 控制浏览器前进         |
| refresh()           | 刷新浏览器当前页面     |
| clear()             | 清除文本               |
| send_keys (value)   | 模拟按键输入           |
| click()             | 单击元素               |
| submit()            | 用于提交表单           |
| get_attribute(name) | 获取元素属性值         |
| is_displayed()      | 设置该元素是否用户可见 |
| size                | 返回元素的尺寸         |
| text                | 获取元素的文本         |
| id                  | 获取元素的id           |
| location            | 获取元素的位置         |
| tag_name            | 获取元素的标签名       |



### 动作链

#### 		鼠标事件

> ```python
> from selenium.webdriver import ActionChains
> 
> actions = ActionChains(driver)
> ```
>
> | 方法                         | 说明                                                         |
> | ---------------------------- | ------------------------------------------------------------ |
> | ActionChains(driver)         | 构造ActionChains对象                                         |
> | move_to_element(above)       | 右击                                                         |
> | double_click()               | 双击                                                         |
> | drag_and_drop(source,target) | 拖动                                                         |
> | move_to_element(above)       | 执行鼠标悬停操作                                             |
> | context_click()              | 用于模拟鼠标右键操作， 在调用时需要指定元素定位              |
> | perform()                    | 执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作 |

#### 		

#### 		键盘事件

> | 模拟键盘按键                | 说明                |
> | --------------------------- | ------------------- |
> | send_keys(Keys.BACK_SPACE)  | 删除键（BackSpace） |
> | send_keys(Keys.SPACE)       | 空格键(Space)       |
> | send_keys(Keys.TAB)         | 制表键(Tab)         |
> | send_keys(Keys.ESCAPE)      | 回退键（Esc）       |
> | send_keys(Keys.ENTER)       | 回车键（Enter）     |
> | send_keys(Keys.CONTROL,‘a’) | 全选（Ctrl+A）      |
> | send_keys(Keys.CONTROL,‘c’) | 复制（Ctrl+C）      |
> | send_keys(Keys.CONTROL,‘x’) | 剪切（Ctrl+X）      |
> | send_keys(Keys.CONTROL,‘v’) | 粘贴（Ctrl+V）      |
> | send_keys(Keys.F1…Fn)       | 键盘 F1…Fn          |



### 获取断言信息

不管是在做功能测试还是自动化测试，最后一步需要拿实际结果与预期进行比较。这个比较的称之为断言。通过我们获取title 、URL和text等信息进行断言。

| 属性        | 说明                   |
| ----------- | ---------------------- |
| title       | 用于获得当前页面的标题 |
| current_url | 用户获得当前页面的URL  |
| text        | 获取搜索条目的文本信息 |





## 关闭浏览器

```python
driver.close()
```





## Python Selenium库的使用

https://blog.csdn.net/weixin_36279318/article/details/79475388	
	
	



​	
​	
​	
​	


​	
​	
​	



​		
​		
​		
​		
​		
​		
​		
