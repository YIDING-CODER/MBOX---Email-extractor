import mailbox
import csv

writer = csv.writer(open("clean_mail.csv", "w"))
for message in mailbox.mbox('abc.mbox'):
	writer.writerow([message['subject'], message['from'], message['date']])
