#opens cars.csv in default read mode
cars = open("cars.csv")

#opens cars_fixed.csv in write mode
cars_fixed = open("cars_fixed.csv", "w")

#lists for all names in file and all means from header                  
names = []
means = {"mpg_mean": 0, "cyl_mean": 0, "displacement_mean": 0,
         "hp_mean": 0, "drat_mean": 0, "w_mean": 0, "qsec_mean": 0,
         "engine_mean": 0, "t_mean": 0, "gear_mean": 0}

#fills list of car names and sum of all categories
for line in cars.readlines():
    line_list = line.split(",")
    car_name = line_list[0]
    names.append(car_name)
    i = 1
    for mean in means.keys():
        value = means.get(mean)
        if (line_list[i] != ""):
            means[mean] = value + float(line_list[i])
            i += 1

#removes duplicates from list of names to create means from non-duplicate list
set_names = set(names)
for mean in means.keys():
    means[mean] = means.get(mean)/len(set_names)

#writes header to file        
cars_fixed.write('''name, miles/per/gallon, cylinders, displacement, horsepower, drat, weight , qsec, engine, transmission, gear''')

#takes pointer to beginning of file
cars.seek(0)
mean_values = list(means.values())

for line in cars.readlines():
    line_list = line.split(",")
    car_name = line_list[0]
    #remove duplicates by model name as models of the same name will have the same specs
    if (names.count(car_name) == 1):
        for part in range (1, len(means) + 1):
            if (line_list[part] == ""):
                line_fill = line_list
                line_fill[part] = str(mean_values[part])
                line_list = line_fill
        #write line_list as one string
        line_complete = ",".join(line_list)
        cars_fixed.write(line_complete)

cars.close()    
cars_fixed.close()

cars_fixed = open("cars_fixed.csv")

print(cars_fixed.read())

cars_fixed.close()



    
