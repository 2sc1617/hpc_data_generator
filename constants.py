# For 10 simulations 8 are Explicit and 2 Implicit
INT_SCHEME = ["EXPLICIT" for i in range(8)] + ["IMPLICIT" for i in range(2)] 

# Here is a data structure from where random values will be generated
# Data for explicit simulations
DATA_EXP = {
    "version": [
        "2020.00", "2020.01", "2020.02", "2020.03",
        "2021.00", "2021.01", "2021.02", "2021.03", "2021.04", "2021.05","2021.06",
        "2022.00", "2022.01", "2022.02", "2022.03", "2022.04",
        "2023.00", "2023.01", "2023.02",
        "2024.00"
        ],
    "precision": ["DOUBLE", "SINGLE"],
    "num_cpu": [
        16, 32, 64, 
        128, 128, 128, 128, 128, 128, 128, 128, 128, 128,
        256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 
        512
        ],
    "termination" : [
        "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL",
        "ERROR" 
        ], 
    "elapsed_time_ave": 28800,
    "elapsed_time_dev": 8000,
}
# Data for implicit simulations
DATA_IMP = {
    "version": [
        "2020.00", "2020.01",
        "2021.00", "2021.01", "2021.02", 
        "2022.00", "2022.01", "2022.02", "2022.03", "2022.04", "2022.05","2022.06",
        "2023.00", "2023.01", "2023.02",
        "2024.00"
        ],
    "precision": ["DOUBLE"],
    "num_cpu": [
        16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 
        32, 32,32,32,32,32, 64, 64, 64, 64, 64, 64, 64,
        ],
    "termination" : [
        "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL", "ERROR", "ERROR",
        "ERROR" 
        ], 
    "elapsed_time_ave": 1000,
    "elapsed_time_dev": 400,
}

