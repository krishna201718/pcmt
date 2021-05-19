from selenium import webdriver
from time import sleep
import chromedriver_binary

url = "https://www.facebook.com"
email = "krishna201710@gmail.com"  # change this
password = "Hello@123456"  # change this

driver = webdriver.Firefox()
driver.get(url)
sleep(5)
email_field = driver.find_element_by_id("email")
password_field = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("u_0_b")
email_field.send_keys(email)
password_field.send_keys(password)
login_button.click()
sleep(5)


def sendFriendRequest():
    see_profile_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/a")
    see_profile_button.click()
    sleep(5)
    friends_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[3]/ul/li[3]/a")
    friends_button.click()
    sleep(5)
    friends_box = driver.find_element_by_id("collection_wrapper_2356318349")
    friend_links = friends_box.find_elements_by_tag_name('a')
    while (True):
        friend_links[0].click()
        sleep(5)
        profile_action_box = driver.find_element_by_id("pagelet_timeline_profile_actions")
        actions = profile_action_box.find_elements_by_tag_name('a')
        actions[0].click()
        sleep(2)
        profile_action_box = driver.find_element_by_id("friendFlyoutContent")
        actions = profile_action_box.find_elements_by_tag_name('a')
        actions[-2].click()
        sleep(2)
        driver.back()
        sleep(5)
        friends_box = driver.find_element_by_id("collection_wrapper_2356318349")
        friend_links = friends_box.find_elements_by_tag_name('a')


sendFriendRequest()



