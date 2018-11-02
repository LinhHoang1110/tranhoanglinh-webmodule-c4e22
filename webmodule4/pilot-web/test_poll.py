from poll import Poll
from random import choice
import mlab

#connect to DB
mlab.connect()

#2. Prepare data
q = "Hackathon ăn gì?"
opts = [
    "Pizza",
    "Bánh mì hội an"
    "Phở xào"
]
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
c = ""
for _ in range(6):
    c+= choice(alphabet)   
#3. Creat document
p = Poll(question=q,options=opts,code=c)

#4. Save
p.save()