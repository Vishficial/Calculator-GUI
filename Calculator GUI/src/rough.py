# import tkinter as tk
#
#
# # root = tk.Tk()
# # lable = tk.Label(root, text= "calculator")
# # lable.pack()
# # root.geometry("300x300")
# # entry = tk.Entry(root, width=35)
# # entry.pack()
# # frame = tk.Frame(root)
# # frame.columnconfigure(4, weight=1)
# # frame.pack(fill= "x")
# # for i in range(5):
# #     for j in range(5)
#
# root = tk.Tk()
# root.geometry("300x300")
# butt =[]
# for btn in range(5):
#     btn = tk.Button(root, text=" ", bg="black")
#     butt.append(btn)
#     btn.pack()
#
# butt[0].config(bg="white")
#
#
# root.mainloop()
#
#
# def create_buttons(self):
#     for i in range(10):  # Creating 10 buttons for digits 0-9
#         btn = tk.Button(self.frame, text=f"{i}", height=2, width=5, bg="gray")
#         self.num_Buttons.append(btn)
#         btn.grid(row=i // 3, column=i % 3)


import tkinter as tk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Calculator")

        self.label = tk.Label(self.root, text="Calculator")
        self.label.pack()

        self.entry = tk.Entry(self.root, width=40, borderwidth=5)
        self.entry.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="x")

        self.num_Buttons = []  # Initialize the list before creating buttons
        self.create_buttons()
        self.design_btn()

        self.root.mainloop()

    # Creating the buttons
    def create_buttons(self):
        for i in range(19):
            btn = tk.Button(self.frame, text=" ", bg="gray",
                            command=lambda x=i: self.btn_click(x))  # Assigning button labels and commands
            self.num_Buttons.append(btn)
            btn.grid(row=i // 4, column=i % 4, sticky="nsew")

        # Configure row and column sizes
        for row in range(5):
            self.frame.rowconfigure(row, weight=1, uniform="equal")
        for col in range(4):
            self.frame.columnconfigure(col, weight=1, uniform="equal")

    def design_btn(self):
        labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "X", "/", "//", "^", "%", "=", "C"]
        for i, label in enumerate(labels):
            self.num_Buttons[i].config(text=label)

    def btn_click(self, index):
        current = self.entry.get()
        label = self.num_Buttons[index].cget("text")

        if label == "=":
            try:
                # Replace 'X' with '*' for multiplication
                expression = current.replace("X", "*")
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif label == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, label)

if __name__ == "__main__":
    calc = Calculator()
