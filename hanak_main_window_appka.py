### GUI imports
from guizero import *
import hanak_main_appka as main

### GUI functions
def calculate_cml():
    results = main.cml(txtbox_af, txtbox_skinfolds_sum, txtbox_age, slider_weight, sex)
    if results:
        text_result_cml.value = f"Your cml is: {results[0]}"
        text_result_bfp.value = f"Your bfp is: {results[1]}"
        text_result_body_fat.value = f"Your bodyfat is: {results[2]}"

def play_audio_fe():
    sock_image.show()
    try:
        main.play_audio()
    except:
        pass

def stop_audio_fe():
    sock_image.hide()
    try:
        main.stop_audio()
    except:
        pass

def write_to_spreadsheet():
    main.create_todays_user_db_record()

### GUI App
app = App(layout="auto", title="My App", width=1080, height=720)

## Window 1
window1 = Box(app, visible=True, align="left", layout="auto")

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
#txtbox_weight = TextBox(window1, command=calculate_cml)
slider_weight = Slider(window1, start=0, end=200, command=calculate_cml)

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
sex = ButtonGroup(window1, options=["Male", "Female"], command=calculate_cml)

#O utput of the calculation
text_result_cml = Text(window1, text=" ")
text_result_bfp = Text(window1, text=" ")
text_result_body_fat = Text(window1, text=" ")

# Write data to gspread
write_data = PushButton(window1, text="Write Data", command=write_to_spreadsheet)

# Start and stop the add
play_button = PushButton(window1, text="Play Ad", command=play_audio_fe)
play_button = PushButton(window1, text="Stop Ad", command=stop_audio_fe)

# Image box
image_box = Box(app, layout="auto", align="right")

# Display an image
cml_widget = Picture(
    image_box,
    image="calculating_cml.png",
    width=510,
    height=360,
    align="top"
)

sock_image = Picture(
    image_box,
    image="left_sock_paradise.png",
    width=510,
    height=360,
    align="bottom",
    visible=False
)

app.display()

