import mailbox
import csv

writer = csv.writer(open("clean_mail.csv", "w"))
writer.writerow(['subject', 'from', 'date'])
for message in mailbox.mbox('abc.mbox'):
	writer.writerow([message['subject'], message['from'], message['date']])
