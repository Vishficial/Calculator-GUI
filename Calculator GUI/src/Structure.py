import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.label = tk.Label(self.root, text="Calculator")
        self.label.pack()

        self.entry = tk.Entry(self.root, width=40)
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
            btn = tk.Button(self.frame, text=" ", bg="gray", command=lambda x=i: self.btn_click(x))  # Assigning button labels
            self.num_Buttons.append(btn)
            btn.grid(row=i//4, column=i%4, sticky="nsew")

        # Configure row and column sizes
        for row in range(5):
            self.frame.rowconfigure(row, weight=1, uniform="equal")
        for col in range(4):
            self.frame.columnconfigure(col, weight=1, uniform="equal")

    def design_btn(self):
        self.num_Buttons[0].config(text="0")
        self.num_Buttons[1].config(text="1")
        self.num_Buttons[2].config(text="2")
        self.num_Buttons[3].config(text="3")
        self.num_Buttons[4].config(text="4")
        self.num_Buttons[5].config(text="5")
        self.num_Buttons[6].config(text="6")
        self.num_Buttons[7].config(text="7")
        self.num_Buttons[8].config(text="8")
        self.num_Buttons[9].config(text="9")
        self.num_Buttons[10].config(text="+")
        self.num_Buttons[11].config(text="-")
        self.num_Buttons[12].config(text="X")
        self.num_Buttons[13].config(text="/")
        self.num_Buttons[14].config(text="//")
        self.num_Buttons[15].config(text="^")
        self.num_Buttons[16].config(text="%")
        self.num_Buttons[17].config(text="=")
        self.num_Buttons[18].config(text="C")

    def btn_click(self, index):
        current = self.entry.get()
        label = self.num_Buttons[index].cget("text")

        if label == "=":
            try:
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




