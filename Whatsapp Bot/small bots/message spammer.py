from selenium import webdriver
import time


# variables

msg_count = 100
msg_infinite = False
delay = 1
message = "activity diagrams bhj"


def spam():

    driver = webdriver.Chrome()

    driver.get("https://web.whatsapp.com")

    input("log into your account and open chat to spam. Then press Enter to continue ... ")

    html_part_message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    html_parts_send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')

    count = 0

    while True:
        print("sending")
        if not (count >= msg_count or msg_infinite):
            break
        html_part_message.send_keys(message)
        if html_parts_send.is_displayed():
            html_parts_send.click()
        count += 1
        time.sleep(delay)



spam()
