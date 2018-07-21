from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://web.whatsapp.com/")
while(True):
    name = input("enter the user:\n")
    msg=input("enter the message:\n")
    count=int(input('enter the count:\n'))
    input('enter anything after Qr code scan')
    user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box=driver.find_element_by_class_name('_2S1VP')
    for i in range(count):
        msg_box.send_keys(msg)
        button=driver.find_element_by_class_name('_2lkdt')
        button.click()

'''contacts = driver.find_elements_by_class_name("chat-title")
whatsapp_msg = 
whatsapp_msg.send_keys(msg)
whatsapp_msg.send_keys(Keys.ENTER)'''
