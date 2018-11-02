from river import River
import mlab_ex1

mlab_ex1.connect()

rivers_list = River.objects()
for p in rivers_list:
    if p.continent == "Africa":
        print(p.name)
        print(p.continent)
        print(p.length)
        print("*"*20) 
       