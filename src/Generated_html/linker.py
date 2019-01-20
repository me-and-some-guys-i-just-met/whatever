import plotly
import plotly.graph_objs as go

#opens Ville de Montreal and STM datasets
stops=open("../data/Borough_Results.txt","r")
borough=open("../data/formated_boroughs.txt","r")

#Dictionnarys of calculated statistics
counts=dict()
ratios=dict()

stop=stops.read()
borough.readline()

count=0
name_list=[]
ratio_list=[]

for name in borough:
    the_name=name.strip().split()
    the_count=stop.count(the_name[0])
    the_people=the_name[2]
    the_area=the_name[1]
    ##print(the_count)
    #count+=the_count
    ratio=(the_count/((float(the_people)*float(the_area))))
    counts[the_name[0]]=the_count
    ratios[the_name[0]]=ratio*10000


##print(ratios)
for i in ratios:
    name_list.append(i)
    ratio_list.append(ratios.get(i))


#all the necessary code to have a nice pyplot

trace = go.Table(
    header=dict(values=[' ', 'Borough', 'ratios']),
    cells=dict(values=[ [i for i in range(len(name_list))],
                        name_list, ratio_list],align = ['left']))

layout = dict(width=500, height=2000)
data= [trace]
fig2=dict(data=data, layout=layout)
plotly.offline.plot(fig2, filename = 'basic_table2.html')
