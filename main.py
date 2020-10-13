import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

website= "https://pentiumproiitest.enjin.com"

driver=webdriver.Edge()
driver.get(website)

try:
    MessagesNum=WebDriverWait(driver, 5).until( #Wait for 5 seconds until we get the element we want
        EC.presence_of_element_located((By.XPATH, '//*[@id="enjin-tray"]/div[1]/div[2]/div[2]/div[1]/div[2]'))
    )
except:
    driver.quit()

if MessagesNum.text!='':
    MessagesNum=int(MessagesNum.text) #Turning it into a readable integer
    print(MessagesNum)

    if MessagesNum > 0:
        #If there are any messages, try to get them.
        driver.get(website+"/dashboard/messages/msg")

        try:
            MessagesContainer=WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'message_sidebar_block_msgs_chunk'))
            )
        finally:
            pass

        Messages=MessagesContainer.find_elements_by_css_selector('a')

        bulkData={}

        def getMessageContents():
            Message=driver.find_element_by_class_name('message_inner_user_block_container')
            Message=Message.find_element_by_class_name('message_inner_user_block').find_element_by_class_name('message_user_text').text
            Message=Message.partition('\n')
            return Message
        
        Message=getMessageContents()
        print()

        """
        #Going through each message
        for i in range(MessagesNum):
            Message=Messages[i]
            MessageType=Message.find_element_by_class_name('message_user_text').text
            username=Message.find_element_by_class_name('message_user_details')
            username=username.find_element_by_class_name('message_user_name').text
            username=username.partition('\n')[0]
            print(MessageType)
            if username=="Enjin Notifier" and MessageType=="Purchase notification":
                Message.click()
                MessageContent= getMessageContents()
                #.partition('\n')[0]

        """


else:
    driver.quit()

#//*[@id="section-main"]/div/div[3]/div[2]/div[8]/table/tbody/tr/td/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[3]/div Message Path
#//*[@id="section-main"]/div/div[3]/div[2]/div[8]/table/tbody/tr/td/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[3]/div/a[2]/div[2]/div[1] Username Path
#message_sidebar_block clickable                unread