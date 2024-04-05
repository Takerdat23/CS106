from ortools.algorithms.python import knapsack_solver
import json
import os
import time
    
def process(data_path): 
    data = {
                        "values":[],
                        "weights":[[]],
                        "capacities":[],
                        "size":[]
                    }
    with open(data_path,'r') as file_data:
            file = file_data.read().splitlines()
            data["size"].append(int(file[1]))
            data["capacities"].append(int(file[2]))
            for i in range(4,len(file)):
                data["values"].append(int(file[i].split(' ')[0]))
                data["weights"][0].append(int(file[i].split(' ')[1]))    
    return data    

def KnapSacks(data, filename): 
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    result = { 
         'Total weight': 0 , 
         'Packed items': [], 
         'Packed items length': 0 , 
         'Time': 0
    }


    values = data["values"]
    weights = data["weights"]
    capacities = data["capacities"]

    solver.init(values, weights, capacities)
    computed_value = solver.solve()
    solver.set_time_limit(180)

    packed_items = []
    packed_weights = []
    total_weight = 0

    print("Total value =", computed_value)
    start = time.start()
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]

            
            
    result["Total weight"] =  total_weight
    result["Packed items"] =  packed_items
    result['Packed items length'] =  len(packed_items)
    end = time.end()
    result['Time'] =  end - start
    out_file = open(filename, "w") 
  
    json.dump(result, out_file) 
    
    out_file.close() 

def main():
    # Create the solver.
    
    path_data = "./tests/02"
    out_dir = "./results/02"
    if os.path.exists(out_dir):
        pass
    else : 
        os.mkdir(out_dir)

    for test_case in os.listdir(path_data ): 
         data = process(os.path.join(path_data,test_case ))
         out_path = os.path.join(out_dir,test_case[:-3]+ ".json" )
         print(out_path)
         if os.path.exists(out_path): 
          continue
         else: 
            try:
                KnapSacks(data, out_path)
            except Exception as e:
                print("Error occurred:", e)
                continue


         
    

   
    # print("Packed_weights:", packed_weights)


if __name__ == "__main__":
    main()