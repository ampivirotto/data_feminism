import urban_planning 
import random 

# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible."""
    if option1[0] in urban_planning.all_non_vehicles:
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

## example 2: always pick emergency vehicles first 
def pick_emergency_vehicle(option1, option2):
    """ This algorithm always picks the emergency vehicle first """
    ## option  = [type of vehicle or non vehicle, modifier]
    possible_emergency_vehicles = urban_planning.vehicles['Emergency Vehicles']

    if option1[0] in possible_emergency_vehicles:
        if option2[0] in possible_emergency_vehicles:
            selected = random.choice([option1, option2])  ## scenario where both are emergency vehicles
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1 
        else:
            return option1, option2 ## where only option 1 is an emergency vehicle 
    elif option2[0] in possible_emergency_vehicles:
        return option2, option1 ## where only option 2 is an emergency vehicle 
    else:
        selected = random.choice([option1, option2])  ## where non of the options are emergency vehicles 
        if option1 == selected:
            return selected, option2
        else:
            return selected, option1


def studentExample(option1, option2):       
    def pointSystem(option):
        emergencyvehicles = urban_planning.vehicles['Emergency Vehicles']
        ## do all the things

    scoreOption1 = pointSystem(option1)




# Student function placeholder
def student_algorithm(option1, option2):
    """Students define their own algorithm here."""
    print('Write your own algorithm here!')

# Function to run the simulation using a given algorithm
# Run the activity
urban_planning.run_activity()

# Run the activity using the example algorithm
#print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
#urban_planning.run_activity(num_scenarios=25, decision_function = always_pick_non_vehicle)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")