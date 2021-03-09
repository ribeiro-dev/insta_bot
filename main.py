from selenium import webdriver
from time import sleep
from random import randint, choice

class InstaBot:

    def __init__(self):
        self.bot = webdriver.Firefox()
        self.bot.get('https://www.instagram.com')
        sleep(10)


    def login(self, userLogin, userPassword):
        print('Realizando login...')

        # Find the inputs to login 
        loginInput = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        passwordInput = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        enterButton = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        
        # Log in the instagram
        loginInput.send_keys(userLogin)
        passwordInput.send_keys(userPassword)
        enterButton.click()
        sleep(10)


        # Change here to the URL of the post you want to comment
        postURL = "https://www.instagram.com/p/exampleURL/"

        # Choose here how many times you want to comment
        timesToComment = 5

        self.bot.get(postURL)
        self.comment(timesToComment)


    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """This method simulates a real typing."""

        for letter in sentence:
            single_input_field.send_keys(letter)
            sleep(randint(1, 5) / 30)


    def comment(self, timesToComment):
        """Comment at the selected post"""
        sleep(5)
        
        try:
            self.bot.find_element_by_class_name('Ypffh').click()
            commentArea = self.bot.find_element_by_class_name('Ypffh')
            sleep(randint(2, 5))
            
            # Change here to the comments you want to do
            comments = [
                "Hello!",
                "How are you?",
                "Nice picture!",
                "🔥🔥"
            ]

            for i in range(timesToComment):
                self.type_like_a_person(choice(comments), commentArea)
                sleep(randint(2, 5))
                self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]').click()
                sleep(randint(4, 6))

        except Exception as err:
            print(err.args[0])

        finally:
            print("Comments done. Closing program...")
            sleep(5)
            self.bot.close()


# Gets the infos about the user to login
userLogin = str(input('Login: '))
userPassword = str(input('Password: '))

# you can comment the lines above and write directly in the login method below
bot = InstaBot()
bot.login(userLogin, userPassword)
