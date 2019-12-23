import pyfiglet
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
