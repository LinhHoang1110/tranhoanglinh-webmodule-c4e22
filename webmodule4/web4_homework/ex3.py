from river import River
import mlab_ex1

mlab_ex1.connect()

rivers_list = River.objects(length__lt=1000)
for p in rivers_list:
    if p.continent == "S. America":
        print(p.name)
        print(p.continent)
        print(p.length)
        print("*"*20) 