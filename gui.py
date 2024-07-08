
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\santosh dhakal\OneDrive\Desktop\Taxi project\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1212x628")
window.configure(bg = "#F4F4F4")


canvas = Canvas(
    window,
    bg = "#F4F4F4",
    height = 628,
    width = 1212,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1177.2880716323853,
    745.7173614501953,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1171.5,
    y=735.865234375,
    width=11.576143264770508,
    height=17.704254150390625
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    606.0,
    315.0,
    image=image_image_1
)

canvas.create_rectangle(
    666.0,
    0.0,
    1223.0,
    653.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    732.283203125,
    19.97119140625,
    anchor="nw",
    text="Welcome to\nFake Taxi \n \n ",
    fill="#2E2E2E",
    font=("Poppins Black", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=735.4599609375,
    y=150.41552734375,
    width=371.5834655761719,
    height=39.3760871887207
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=736.0,
    y=228.0,
    width=371.5834655761719,
    height=39.3760871887207
)

canvas.create_rectangle(
    720.0,
    340.0,
    973.4008026123047,
    341.0,
    fill="#BFBFBF",
    outline="")

canvas.create_rectangle(
    1005.0,
    340.0,
    1205.0,
    341.0,
    fill="#BFBFBF",
    outline="")

canvas.create_text(
    979.0,
    329.0,
    anchor="nw",
    text="OR",
    fill="#2E2E2E",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1414.0,
    541.89013671875,
    anchor="nw",
    text="Forgot Password?",
    fill="#6257DB",
    font=("Poppins Regular", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    962.8931579589844,
    461.8485450744629,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#ECECEC",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=758.9072265625,
    y=442.9697265625,
    width=407.97186279296875,
    height=35.75763702392578
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    726.0,
    459.0,
    image=image_image_2
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    962.6189422607422,
    393.6598815917969,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#ECECEC",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=755.7705078125,
    y=377.359375,
    width=413.6968688964844,
    height=30.60101318359375
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    724.0,
    394.0,
    image=image_image_3
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=751.0,
    y=508.0,
    width=434.00323486328125,
    height=41.16999816894531
)

canvas.create_text(
    774.0,
    559.0,
    anchor="nw",
    text="Remember me",
    fill="#2E2E2E",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    874.0,
    589.0,
    anchor="nw",
    text="Don’t have an account? Register",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
