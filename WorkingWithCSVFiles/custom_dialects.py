#################################
## CSV Module
## Using CSV Dialects
#################################

import csv

## Printing available csv dialects
print(csv.list_dialects())

## passwd file - passwd.csv is attached to this lecture
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# bin:x:2:2:bin:/bin:/usr/sbin/nologin
# sys:x:3:3:sys:/dev:/usr/sbin/nologin
# sync:x:4:65534:sync:/bin:/bin/sync
# games:x:5:60:games:/usr/games:/usr/sbin/nologin
# man:x:6:12:man:/var/cache/man:/usr/sbin/nologin

## Reading /etc/passwd (Linux file) using a custom delimiter (:)
with open('/etc/passwd', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)

## item.csv file (attached to this lecture)
# items#quantity#price
# pens#3#8.8
# plates#15#2.6
# cups#44#1.1
# bottles#21#3.5

## Creating a custom dialect named hashes
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

## Reading items.csv file
with open('items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')
    for row in reader:
        print(row)

## Appending a line to the csv file
with open('items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))