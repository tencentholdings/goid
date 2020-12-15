import tkinter as tk
import requests as rq

authTokenValue = None

response = rq.get("cdn.gog.com/content-system/v1/manifests/1207658930/windows/37794096/463cd4b2-783e-447a-b17e-a68d601911e3.json")
print(response.status_code)
print(response.json())

def test_function():
	authTokenValue = authToken.get()
	label = tk.Label(frame, text = "AuthToken: " + str(authTokenValue))
	label.place(relx=0.05, rely=0.8)

root = tk.Tk()
root.title("GOG Offline Installer Downloader -")
root.geometry("600x600")

canvas = tk.Canvas(root, height=600, width = 600, bg="#e6e6e6")
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1, relheight=0.5)

label = tk.Label(frame, text = "AuthToken: " + str(authTokenValue))
label.place(relx=0.05, rely=0.8)

authToken = tk.Entry(frame, bg="#ccffff")
authToken.place(relx=0.05, rely=0.05)

updateButton = tk.Button(frame, bg = "#ff8080", text = "Update", command=test_function)
updateButton.place(relx = 0.05, rely = 0.15)

root.mainloop()