from selenium import webdriver
from time import sleep 
from secrets import pw
from random import randint

class Bot():

    links = []

    comments = [
        'Great post!', 'Awesome!'
    ]

    def __init__(self):
        self.login('__testbot', pw)
        self.like_comment_by_hashtag('programmer')
    
    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click() #clicking on 'Not Now' button
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click() #clicking on 'Not Now' button

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        links  = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href') #instagram posts have '.com/p/' in their urls
        valid_links = list(filter(condition, links))

        for i in range(3):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            #like
            sleep(3)
            self.driver.find_element_by_class_name('fr66n').click()
            sleep(5)

            #comment
            self.driver.find_element_by_class_name('_15y0l').click()
            sleep(1)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
            sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
           

def main():
    while True:
        my_bot = Bot()
        sleep(60*60) #1 hour


if __name__ == '__main__':
    main()