import tkinter as tk

def tekan():
    label.config(text = "Tombol ditekan")

app = tk.Tk()
app.title("Contoh GUI")

label = tk.Label(app, text = "Tekan tombol dibawah")
label.pack()

tombol = tk.Button(app, text = "Tekan", command = tekan)
tombol.pack()

app.mainloop()
