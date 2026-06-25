import tkinter as tk
import datetime
from PIL import Image, ImageTk
import json
import os

SAVE_FILE = "saved_data.json"


def save_data():
    data = {
        "entry_text": entry.get(),
        "text_content": text.get("1.0", tk.END),
        "counter": counter
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    global counter
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    # File is empty, initialize defaults
                    raise ValueError("Empty file")
                data = json.loads(content)
                entry.delete(0, tk.END)
                entry.insert(0, data.get("entry_text", ""))
                text.delete("1.0", tk.END)
                text.insert(tk.END, data.get("text_content", ""))
                counter = data.get("counter", 0)
                l2['text'] = str(counter)
                l4['text'] = data.get("start_time", "Started: " + aika())
        except (json.JSONDecodeError, ValueError):
            # Handle empty or invalid JSON file gracefully
            counter = 0
            l2['text'] = str(counter)
            l4['text'] = "Started: " + aika()
    else:
        l4['text'] = "Started: " + aika()


image_path = "C:/Users/verne/Downloads/sisyphus.jpg"
image = Image.open("C:/Users/verne/Downloads/sisyphus.jpg")


counter = 0

def aika():
    import datetime

    x = datetime.datetime.now()

    return x.strftime("%c")
    

def add():
    global counter 
    counter += 1

def clear_label():
    l1['text'] = ""
    
def on_button_click():
    l1.config(
        text= "Another one",
        font=('Helvetica',20))

    root.after(500, clear_label)
    global counter 
    add()
    l2['text'] = str(counter)

def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized)

    l3.config(image=photo)
    l3.image = photo


root = tk.Tk()
root.title("Job application tracker")
root.geometry("400x400") 


initial_width = 100
initial_height = 100
resized = image.resize((initial_width, initial_height), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized)

b1 = tk.Button(root,
                text = "Application sent",
                font=('Helvetica',25), 
                command=on_button_click)
b1.place(x = 0, y = 0)
b1.pack()

l1 = tk.Label(root,
               font=('Helvetica',20)
               )
l1.place(x = 0 , y = 0)
l1.pack()

l2 = tk.Label(root,
            text = (counter),
            font=('Helvetica',20),
            )
l2.pack()



l4 = tk.Label(root, text = "Started: " + aika(), font=('Helvetica', 12))
l4.pack()

l3 = tk.Label(root, image=photo)
photo = ImageTk.PhotoImage(resized)
l3.bind('<Configure>', resize_image)
l3.pack()




entry = tk.Entry(root)
entry.pack()

text = tk.Text(root)
text.pack()

load_data()

root.protocol("WM_DELETE_WINDOW", lambda: (save_data(), root.destroy()))

root.mainloop()