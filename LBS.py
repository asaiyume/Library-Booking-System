import pyfiglet
import csv

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
    end['end{}'.format(i)] = acc_details[i][3]
