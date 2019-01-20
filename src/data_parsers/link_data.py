from Classes import arrondissement

def end_results():
    boroughs_data = open(r'../../data/formatted_boroughs', mode='r')
    stops_data = open(r'../../data/Borough_Results.txt', mode='r')

    #stops data has stopid, lat,long, Borough
    #boroughs data has name area population

    #Initialize a set of every borough name
    boroughs = []

    for line in boroughs_data:
        x = line.split(',')
        boroughs.append(Arrondissement(x[0],[line.strip("\n").split(', ') for line in stops_data],x[2], x[3])

    boroughs_data.close()
    stops_data.close()

    with open(r'../../data/Results.txt', 'w') as fr:
        header = "Name\tArea\tPopulation\tRating"+"\n"
        fr.write(header)
        for boro in boroughs:
            string_builder = ""
            string_builder += boro.name +"\t" + boro.area + boro.population + len(boro.stops)/(int(boro.population)*int(boro.area))
            fr.write(string_builder)
