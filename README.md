# MBOX---Email-extractor
Extract the email list from the mailbox - MBOX

What do you need to run the script?
1.A source mbox file - eg abc.mbox
2.python installed

How to use the script?

Step1: put abc.mbox into the same folder as the script 
Step2: open the mbox_parser.py
       and change the line5
         for message in mailbox.mbox('your_mbox_name') to for message in mailbox.mbox('abc.mbox')
Step3: Open the terminal at current folder and type:
       python mbox_parser.py
Step4: You will find a new csv file called clean_mail.csv under the same folder
Step5: Clean the csv fild as you want.
Step6: Select the column "from" and use the formular in the adjacent cell (D1)
        =TRIM(RIGHT(SUBSTITUTE(LEFT(B1,FIND (" ",B1&" ",FIND("@",B1))-1)," ", REPT(" ",LEN(B1))),LEN(B1))).
Step7: Use replace in excel to replace the unnecessary character in the email



References:
           How To Quickly Extract Email Address From Text String?
           https://www.extendoffice.com/documents/excel/1272-excel-extract-email-address.html#a1
           
           
           https://github.com/gitabites/mboxtocsv
       
