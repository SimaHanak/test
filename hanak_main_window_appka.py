### GUI imports
from guizero import *
import hanak_main_appka as main

### GUI functions
def calculate_cml():
    results = main.cml(txtbox_af, txtbox_skinfolds_sum, txtbox_age, txtbox_weight, sex)
    if results:
        text_result_cml.value = f"Your cml is: {results[0]}"
        text_result_bfp.value = f"Your bfp is: {results[1]}"
        text_result_body_fat.value = f"Your bodyfat is: {results[2]}"

### GUI App
app = App(title="My App", width=700, height=840)

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Hi, user!"))

# Input activity factor
text_af = Text(
    window1,
    text="Please enter your activity factor for today:"
)
txtbox_af = TextBox(window1, command=calculate_cml)

# Input weight
text_weight = Text(
    window1,
    text="Please enter your weight in kilograms (kg):"
)
txtbox_weight = TextBox(window1, command=calculate_cml)

# Input age
text_age = Text(
    window1,
    text="Please enter your age:"
)
txtbox_age = TextBox(window1, command=calculate_cml)

# Input skinfolds sum
text_skinfolds_sum = Text(
    window1,
    text="Please enter your skinfolds sum:"
)
txtbox_skinfolds_sum = TextBox(window1, command=calculate_cml)

# Input sex
text_sex = Text(
    window1,
    text="Please enter your sex:"
)
sex = Combo(window1, options=["Male", "Female"], command=calculate_cml)

text_result_cml = Text(window1, text=" ")
text_result_bfp = Text(window1, text=" ")
text_result_body_fat = Text(window1, text=" ")

# Output results of calculations




# Display an image
image_widget = Picture(
    window1,
    image="resources/images/calculating_cml.png",
    width=680,
    height=480,
    align="bottom"
)

app.display()

