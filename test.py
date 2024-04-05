import os 


path_data = "./tests/00Uncorrelated/00_n50_R01000_4.kp"
data = {
                    "values":[],
                    "weights":[[]],
                    "capacities":[],
                    "size":[]
                }
with open(path_data,'r') as file_data:
        file = file_data.read().splitlines()
        data["size"].append(int(file[1]))
        data["capacities"].append(int(file[2]))
        for i in range(4,len(file)):
            data["values"].append(int(file[i].split(' ')[0]))
            data["weights"][0].append(int(file[i].split(' ')[1]))          

print(data)     