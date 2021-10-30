from value_functions import *

values = greens_equally()

def allocate(values):

    # normalise the values into pounds

    normed_values = values * (3000000/np.sum(values))
    normed_values = [f"£{x:.2f}" for x in normed_values]

    # produce an allocation
    
    projects = pd.read_csv("variables.csv",
                           usecols=['Project_ID', 'Project_Name'])
    projects['Allocation'] = normed_values

    projects.to_csv("allocation.csv", index=False)

allocate(values)
