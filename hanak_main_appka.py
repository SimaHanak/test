# Importing all app imports
from hanak_config_appka import *

# Main Window Functions

def get_values(*args):
    # Get all values from the widgets
    return [widget.value for widget in args]

def cml(activity_factor, skinfolds_sum, age, weight, sex):
    # cml, bfp and body fat calculation
    activity_factor, skinfolds_sum, age, weight, sex = get_values(activity_factor, skinfolds_sum, age, weight, sex)
    try:
        activity_factor = float(activity_factor)
        skinfolds_sum = float(skinfolds_sum)
        age = float(age)
        weight = float(weight)
    except ValueError:
        return None
    
    if sex == 'Male':
        body_density = 1.10938 - (8.267e-4 * skinfolds_sum) + (1.6e-6 * (skinfolds_sum ** 2)) - (2.574e-4 * age)
    elif sex == 'Female':
        body_density = 1.0994921 - (9.929e-4 * skinfolds_sum) +  (2.3e-6 * (skinfolds_sum ** 2)) - (1.392e-4 * age)
    else:
        body_density = 1.1 - (8.999e-4 * skinfolds_sum) + (1.9e-6 * (skinfolds_sum ** 2)) - (1.9e-4 * age)

    bfp = 495 / body_density - 450
    bfp = round(bfp, 2)
    body_fat = weight*bfp / 100 
    body_fat = round(body_fat, 2)

    bmr = weight * 24.2
    cml = bmr * activity_factor
    cml = round(cml, 2)
    
    # Output of the results
    return [cml, bfp, body_fat]

# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries