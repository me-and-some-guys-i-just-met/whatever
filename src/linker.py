stops=open("../data/Borough_results.txt","r")
borough=open("../data/Boroughs_of_Montreal","r")

counts=dict()
ratios=dict()
stop=stops.read()

borough.readline()
count=0

for name in borough:
    the_name=name.strip().split()
    the_count=stop.count(the_name[0])
    the_people=the_name[2]
    the_area=the_name[1]
    print(the_name)
    #count+=the_count
    ratio=(the_count/((float(the_people)*float(the_area))))
    counts[the_name[0]]=the_count
    ratios[the_name[0]]=ratio*10000
    
    


print(ratios)

