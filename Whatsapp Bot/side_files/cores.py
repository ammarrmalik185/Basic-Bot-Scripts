from selenium import webdriver
import time


class BotCore:

    def _init_(self):
        self.driver = None
        self.groups = []
        self.group_buttons = []

    def code_change_sensor(self):
        check = list()
        check.append(self.driver.page_source)
        while True:
            time.sleep(0.5)
            check.append(self.driver.page_source)
            if check[0] != check[1]:
                print("change detected")
                break
            else:
                check.pop(0)

    def initiate_part1(self):
        self.driver = webdriver.Chrome()
        input("press enter after init p1")
        self.groups = [""]
        tp1 = "\\*[contains(text(),'"
        tp2 = "')]"
        for t in self.groups:
            text = tp1 + t + tp2
            e = self.driver.find_element_by_xpath(text)
            self.group_buttons.append(e)


    def core_loop(self):

class ResponseCore:



    def generate(self, command):
        com_parts = command.split("")

        if (com_parts == )




