from Classes.arrondissement import Arrondissement
#
# this program outputs an HTML table
with open("../data/Borough_Results.txt","r") as stops:
    stops_data = stops.read()

ratios = set()

# populate the set
with open("../data/Boroughs_of_Montreal","r") as borough:
    borough.readline() # skip first line
    for line in borough:
        boro, area, population = line.strip().split()
        ratios.add(Arrondissement(boro, stops_data.count(boro), area, population))

ratio_list = []
for item in ratios:
    ratio_list.append((item, item.ratio() * 10000))

ratio_list = sorted(ratio_list, key=lambda x: x[1])

def generate_html_table():
    print("<table>")
    for boro, val in ratio_list:
        print("    <tr>")
        print(f"        <td>{boro}</td>")
        print(f"        <td>{val}</td>")
        print("    </tr>")
    print("</table>")

generate_html_table()
