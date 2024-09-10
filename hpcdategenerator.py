#/usr/bin/python
import numpy as np
import pandas as pd
from constants import INT_SCHEME, DATA_EXP, DATA_IMP
import random
import json
from datetime import date, datetime, timedelta
import dateutil
import pymongo
from dateutil import parser

# Constants
NUM_SIM = 1000

def f_add_db(new_dict):
    """ This function add the simulation data to de database,

    Args:
        new_dict (dictionary): A dictionary with simulation parameters

    Returns:
        _type_: Mongo return id
    """
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_db = mongo_client["simulations"]
    mongo_collection = mongo_db["data"]

    insert_id = mongo_collection.insert_one(new_dict)
    return insert_id

def main():
    """ Main function
    """
    # Start date is two month ago
    today = date.today()
    two_month_ago = today + dateutil.relativedelta.relativedelta(months=-2) 
   
    # A data range between two date with XXmin frequency
    data_range_to_choose = pd.date_range(start=two_month_ago, end=today, freq="10min")
    
    # Base filename
    base_name = "simulation_"
    
    # Number of samples
    samples_size = NUM_SIM
    
    # To store the simulations
    list_of_simulations = []
    
    # counter
    i = 0
    
    # Loop over for each sample
    for s in range(samples_size):
        i += 1

        # Dictionary to store simulation data 
        simulation_dic = {}

        # Get integration scheme randomly       
        scheme = random.choice(INT_SCHEME)
        
        # Add integration scheme
        simulation_dic["scheme"] = scheme    

        # Only for Explicit simulations        
        for feature in ["version", "precision", "file", "num_cpu", "termination", "elapsed_time_sec", "date_sta"]:

            # Add simulation name
            if feature == "file":
                simulation_dic["file"] = "%s%i.pc" %(base_name, i)
                continue  
            
            if scheme == "EXPLICIT":
                # For "elapsed_time_sec" generate random values using an average and standard 
                # deviation 
                if feature == "elapsed_time_sec":
                    simulation_dic[feature] = int(np.random.normal(
                        DATA_EXP["elapsed_time_ave"], 
                        DATA_EXP["elapsed_time_dev"], 1)[0])                    
                    continue
                
                if feature == "date_sta":
                    simulation_dic[feature] = random.choice(data_range_to_choose)
                    continue

                simulation_dic[feature] = random.choice(DATA_EXP[feature])
            else:
                # For "elapsed_time_sec" generate random values using an average and standard 
                # deviation 
                if feature == "elapsed_time_sec":
                    simulation_dic[feature] = int(np.random.normal(
                        DATA_IMP["elapsed_time_ave"], 
                        DATA_IMP["elapsed_time_dev"], 1)[0])                    
                    continue
                
                if feature == "date_sta":
                    simulation_dic[feature] = random.choice(data_range_to_choose)
                    continue

                simulation_dic[feature] = random.choice(DATA_IMP[feature])

        # The version is converted to integer to have the main version and not only the sub releases
        simulation_dic["vers_int"] = int(float(simulation_dic["version"]))
        # Calculate CPU usage in minutes
        simulation_dic["cpu_usage_min"] = int(simulation_dic["num_cpu"] * simulation_dic["elapsed_time_sec"]/60)
        
        #simulation_dic["date_sto"] = simulation_dic["date_sta"] + dateutil.relativedelta.relativedelta(second=simulation_dic["elapsed_time_sec"])
        simulation_dic["date_sto"] = simulation_dic["date_sta"] + timedelta(seconds=simulation_dic["elapsed_time_sec"])
        #simulation_dic["date_sto"] = simulation_dic["date_sto"].isoformat()
        
        list_of_simulations.append(simulation_dic)
        f_add_db(simulation_dic)

    # print Json in screen
    print(json.dumps(list_of_simulations, indent=4, default=str))    


if __name__ == "__main__":
    main()