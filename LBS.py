import pyfiglet
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


ascii_banner = pyfiglet.figlet_format('Library Booking System')
print(ascii_banner)

with open('accounts.csv') as csvfile:
    acc_details = []
    data = csv.reader(csvfile, delimiter=' ', quotechar=' ')
    for row in data:
        acc_details.append(row[0].split('\t'))
    acc_details.remove(acc_details[0])
usernames = {}
passwords = {}
start = {}
end = {}
for i in range(len(acc_details)):
    usernames['username{}'.format(i)] = acc_details[i][0]
    passwords['password{}'.format(i)] = acc_details[i][1]
    start['start{}'.format(i)] = acc_details[i][2]
    start['end{}'.format(i)] = acc_details[i][3]

lvl4room = ['1 = Coolidge (5)',
            '2 = Darwin (5)',
            '3 = Einstein (5)',
            '4 = Herzberg (5)',
            '5 = Strauss (13)',
            '6 = Sun Tzu (9)',
            '7 = Aristotle (3)',
            '8 = Bach (2)',
            '9 = Brahms (4)',
            '10 = Carnegie (4)',
            '11 = Confucius (4)',
            '12 = Gandhi (5)',
            '13 = Homer (2)',
            '14 = Iverson (4)',
            '15 = Magellan (4)',
            '16 = Mendeleev (4)',
            '17 = Montessori (4)',
            '18 = Newton (6)',
            '19 = Pascal (6)',
            '20 = Rembrant (4)',
            '21 = Rockerfeller (4)',
            '22 = Socrates (4)',
            '23 = Van Gogh (4)']
lvl5room = ['1 = Turquoise (10)',
            '2 = Adamite (6)',
            '3 = Agate (6)',
            '4 = Aquamarine (2)',
            '5 = Amber (8)',
            '6 = Amethyst (8)',
            '7 = Coral (8)',
            '8 = Diamond (6)',
            '9 = Emerald (6)',
            '10 = Garnet (6)',
            '11 = Malachite (8)',
            '12 = Onyx (4)',
            '13 = Opal (4)',
            '14 = Pearl (4)',
            '15 = Peridot (1)',
            '16 = Quartz (1)',
            '17 = Ruby (4)',
            '18 = Sapphire (4)',
            '19 = Topaz (4)']
level = input('Choose your level: ')
if level == '4':
    for i in lvl4room:
        print(i)
elif level == '5':
    for i in lvl5room:
        print(i)
room = input('Choose your room: ')
if level == '4':
    print('Booking {} for you now.'.format(lvl4room[int(room)-1]))
elif level == '5':
    print('Booking {} for you now.'.format(lvl5room[int(room)-1]))


def booking(username, password, level, room, start, end):
    # Go to RBS
    browser = webdriver.Chrome(
        'chromedriver.exe')
    browser.get('https://www1.np.edu.sg/npnet/webappanacle/StudentLogin.aspx')
    # Enter Username
    userbutton = browser.find_element_by_id('UserName_c1')
    browser.execute_script(
        "document.getElementById('UserName_c1').style.display = 'inline-block';")
    userbutton.send_keys(username)
    # Enter Password
    passbutton = browser.find_element_by_id('Password_c1')
    browser.execute_script(
        "document.getElementById('Password_c1').style.display = 'inline-block';")
    passbutton.send_keys(password)
    passbutton.send_keys(Keys.ENTER)
    # Wait for page to load
    wait = WebDriverWait(browser, 20)
    # Switch to iFrame
    iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((
        By.XPATH, "//iframe[@id='frameBottom']")))
    browser.switch_to.frame(iframe)
    # Choose Category
    # Option 2 = Library Resource
    browser.find_element_by_xpath(
        '//*[@id="ResourceCategory_c1"]/option[2]').click()
    # Choose Resource Type
    # Option 11 = Discussion Room
    browser.find_element_by_xpath(
        '//*[@id="DropSpaceType_c1"]/option[11]').click()
    # Choose Block
    # Option 2 = Blk 1
    browser.find_element_by_xpath(
        '//*[@id="DropDownVenue_c1"]/option[2]').click()
    # Wait for Level to load
    # Too fast will reset Levels
    time.sleep(5)
    # Choose Levels
    # Options: Lvl 1 = 1, Lvl 2 = 2...
    browser.find_element_by_xpath(
        '//*[@id="DropLevel_c1"]/option[{}]'.format(level)).click()
    # Click search
    browser.find_element_by_xpath(
        '//*[@id="BtnQuick"]').click()
    # Delay to load iFrame
    source = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    '//*[@id="dpc"]/div[2]/div/div[2]/div/table[1]/tbody/tr[{}]/td[{}]/div/div'.format(start, room))))
    dest = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  '//*[@id="dpc"]/div[2]/div/div[2]/div/table[1]/tbody/tr[{}]/td[{}]/div/div'.format(end, room))))

    # Selecting time slots
    ActionChains(browser).drag_and_drop(source, dest).perform()

    browser.implicitly_wait(10)
    spurpose = browser.find_element_by_xpath(
        '//*[@id="bookingFormControl1_TextboxPurpose_c1"]')
    spurpose.send_keys('study!!')
    # Checks box
    browser.execute_script(
        "document.getElementById('bookingFormControl1_CheckBoxDisclaimer_c1').checked = 'checked';")

    browser.implicitly_wait(10)
    # Checks box
    browser.execute_script(
        "document.getElementById('bookingFormControl1_CheckBoxPolicy_c1').checked = 'checked';")
    # Delay for checkboxes
    time.sleep(1)

    sconfirm = browser.find_element_by_xpath('//*[@id="panel_UIButton2"]')
    sconfirm.click()
    browser.implicitly_wait(10)
    browser.delete_all_cookies()
