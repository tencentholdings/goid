import tkinter as tk

authTokenValue = None
#This is a test comment

def test_function():
	print(authToken.get())
	authTokenValue = authToken.get()
	label = tk.Label(frame, text = "AuthToken: " + str(authTokenValue))
	label.place(relx=0.05, rely=0.8)

root = tk.Tk()
root.title("GOG Offline Installer Downloader")
root.geometry("600x600")

canvas = tk.Canvas(root, height=600, width = 600, bg="#e6e6e6")
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1, relheight=0.5)

label = tk.Label(frame, text = "AuthToken: " + str(authTokenValue))
label.place(relx=0.05, rely=0.8)

authToken = tk.Entry(frame, bg="blue")
authToken.place(relx=0.05, rely=0.05)

updateButton = tk.Button(frame, bg = "red", text = "Update", command=test_function)
updateButton.place(relx = 0.05, rely = 0.15)


root.mainloop()