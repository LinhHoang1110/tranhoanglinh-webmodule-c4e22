from poll import Poll
import mlab

#1. Connect
mlab.connect()

#2. Read all
poll_list = Poll.objects() 
for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)
    print("********************")