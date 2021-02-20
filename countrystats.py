import csv

country="us"
active_cases=0
recovered=0
deaths=0
state_region=[]
country=country.lower()
try:
  with open('coviddataset.csv', 'r') as file:
    csvReader = csv.reader(file)
    for row in csvReader:
      if row[3].lower() == country:
        active_cases+= int(row[10])
        recovered+= int(row[9])
        deaths+=int(row[8])
        if row[1]:
          state_region.append(row[2]+"-"+row[1])
        else:
          state_region.append(row[2])

except:
  dummy=0 #useless step

print(active_cases, recovered, deaths)  # the 3 numbers for the whole country
print(state_region)  # gives all the regions for the country



#FIPS,Admin2,Province_State,Country_Region,Last_Update,Lat,Long_,Confirmed,Deaths,Recovered,Active,Combined_Key,Incident_Rate,Case_Fatality_Ratio


