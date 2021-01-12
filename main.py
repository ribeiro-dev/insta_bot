from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaBot:

    def __init__(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.get('https://www.instagram.com')
        sleep(10)


    def login(self):
        print('Realizando login...')

        # Gets the infos about the user
        userLogin = str(input('Login: '))
        userPassword = str(input('Password: '))

        # Find the inputs to login 
        loginInput = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        passwordInput = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        enterButton = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        
        # Log in the instagram
        loginInput.send_keys(userLogin)
        passwordInput.send_keys(userPassword)
        enterButton.click()
        sleep(10)

        try:
            saveInfoQuestion = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/div[2]')
            dontSaveInfoButton = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
            dontSaveInfoButton.click()
            sleep(5)

            dontGetNotificationsButton = self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            dontGetNotificationsButton.click()
            sleep(5)
            
        except Exception as err:
            print('SaveInfos not found')
            print(err.args[0])


        self.bot.get('https://www.instagram.com/p/CHQQdxJBq9W/')

        sleep(5)
        self.comment()


    def comment(self):
        
        try:
            # commentArea = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            commentArea = self.bot.find_elements_by_class_name('Ypffh')
            print(commentArea)
            print(len(commentArea))
            commentArea[0].click()
            commentArea[0].send_keys(Keys.TAB)
            commentArea[0].clear()
            commentArea[0].send_keys('@andrad.brunno')
            # publishComment = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
            # publishComment.click()
                
        except Exception as err:
            print(err.args[0])


bot = InstaBot()
bot.login()
