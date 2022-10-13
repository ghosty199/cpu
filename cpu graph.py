import matplotlib .pyplot as plt
import psutil as p	
app_name_list = []
app_name_percentage_list = []
count=0
for process in p.process_iter():
    count+=1
    if count<=6:
        name=process.name()
        cpuusage=p.cpu_percent()
        print("name=",name)
        print("cpu usage",cpuusage)
        app_name_list.append(name)
        app_name_percentage_list.append(cpuusage)
        
maxvalue=max(app_name_percentage_list)
indexmaxvalue=app_name_percentage_list.index(maxvalue)
maxappname=app_name_list[indexmaxvalue]
print(maxappname)

minvalue=min(app_name_percentage_list)
indexminvalue=app_name_percentage_list.index(minvalue)
minappname=app_name_list[indexminvalue]
print(minappname)
appname=[]
apppercentage=[]
appname.append(maxappname)
appname.append(minappname)
apppercentage.append(maxvalue)
apppercentage.append(minvalue)
plt.figure(figsize=(15,7))
plt.xlabel("application")
plt.ylabel("percentage")
plt.bar(appname, apppercentage,width=0.6, color=("red","pink","red","pink","red","pink"))
plt.show
        