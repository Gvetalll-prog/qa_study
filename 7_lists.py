cities = ["Vilnius", "Kaunas", "Klaipeda", "Visaginas"]
cities.append("Panevezis")

print("Checking cities for branch offices:")

for city in cities:
    if city == "Visaginas":
        print(f"-> {city}: Home base found!")
    else:
        print(f"-> {city}: Scanning for QA Jobs... ")


#skills = ["Linux", "Git", "Python"]
#skills.append("C#")

#print("I am learning [skill]")

#for skill in skills:
#   if skill == "Python":
#       print(f"->{skill}: learning Now")
#   else:
#       print(f"->{skill}: basic adestand skills")