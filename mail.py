import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login("likhithshankartpt@gmail.com","likhith@tpt")
message="""From:Illuminati <illuminati2021@gmail.com>
To:Likhith <likhithshankarprithvi@gmail.com>
Subject:Finale 

Trying to test the technology
I am going to Rock you from rock bottom
You did see what you are intented to see!!"""
server.sendmail("likhithshankartpt@gmail.com","likhithshankarprithvi@gmail.com",message)
server.quit()
