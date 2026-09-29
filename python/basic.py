print("sanket legend")
if 5 > 2 :
   print("sanket legend never lose")
print("I love you 3000",end = "")
print(" ganpati bappa")
x = "sanket legend"
print(type(x))

import tkinter as tk

def click():
    print("Button Clicked!")

window = tk.Tk()
window.title("My App")
window.geometry("400x300")

button = tk.Button(
    window,
    text="Click Me",
    command=click
)

button.pack(pady=50)

window.mainloop()