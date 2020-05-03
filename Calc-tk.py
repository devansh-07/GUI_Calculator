from tkinter import *
from tkinter import ttk


class Calculator(object):
	def __init__(self):
		self.exp = ""
		self.flag = "expression"
		self.oper_list = ["+", "-", "*", "/", "**"]

		root.bind("<Key>", None)

		self.ans_label = Text(root, width=25, height=3, font=("Calibri", 14), bd=0, background="#06989A", highlightbackground="#3465A4", highlightthickness=2, state=DISABLED)
		self.ans_label.pack(pady=15, padx=10, side=TOP)

		self.insert_val("\n   WELCOME TO CALCULATOR!")
		self.flag = "message"

		ttk.Style().configure("TButton")

		outerframe = Frame(root)
		outerframe.pack(padx=10, pady=8)

		innerframe0 = Frame(outerframe)
		innerframe0.config(bg="#141414")
		innerframe0.pack(side=TOP)

		bt0 = ttk.Button(innerframe0, text="(", padding=10, width=6, command=lambda: self.add_to_exp("("), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt1 = ttk.Button(innerframe0, text="^", padding=10, width=6, command=lambda: self.add_to_exp("**"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt2 = ttk.Button(innerframe0, text=")", padding=10, width=6, command=lambda: self.add_to_exp(")"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt3 = ttk.Button(innerframe0, text="←", padding=10, width=6, command=self.bkspc, takefocus=False).pack(side=LEFT, padx=2, pady=2)


		innerframe1 = Frame(outerframe)
		innerframe1.config(bg="#141414")
		innerframe1.pack(side=TOP)

		bt4 = ttk.Button(innerframe1, text="7", padding=10, width=6, command=lambda: self.add_to_exp("7"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt5 = ttk.Button(innerframe1, text="8", padding=10, width=6, command=lambda: self.add_to_exp("8"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt6 = ttk.Button(innerframe1, text="9", padding=10, width=6, command=lambda: self.add_to_exp("9"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt7 = ttk.Button(innerframe1, text="+", padding=10, width=6, command=lambda: self.add_to_exp("+"), takefocus=False).pack(side=TOP, padx=2, pady=2)

		innerframe2 = Frame(outerframe)
		innerframe2.config(bg="#141414")
		innerframe2.pack(side=TOP)

		bt8 = ttk.Button(innerframe2, text="4", padding=10, width=6, command=lambda: self.add_to_exp("4"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt9 = ttk.Button(innerframe2, text="5", padding=10, width=6, command=lambda: self.add_to_exp("5"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt10 = ttk.Button(innerframe2, text="6", padding=10, width=6, command=lambda: self.add_to_exp("6"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt11 = ttk.Button(innerframe2, text="–", padding=10, width=6, command=lambda: self.add_to_exp("-"), takefocus=False).pack(side=TOP, padx=2, pady=2)

		innerframe3 = Frame(outerframe)
		innerframe3.config(bg="#141414")
		innerframe3.pack(side=TOP)

		bt12 = ttk.Button(innerframe3, text="1", padding=10, width=6, command=lambda: self.add_to_exp("1"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt13 = ttk.Button(innerframe3, text="2", padding=10, width=6, command=lambda: self.add_to_exp("2"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt14 = ttk.Button(innerframe3, text="3", padding=10, width=6, command=lambda: self.add_to_exp("3"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt15 = ttk.Button(innerframe3, text="×", padding=10, width=6, command=lambda: self.add_to_exp("*"), takefocus=False).pack(side=TOP, padx=2, pady=2)

		innerframe4 = Frame(outerframe)
		innerframe4.config(bg="#141414")
		innerframe4.pack(side=TOP)

		bt16 = ttk.Button(innerframe4, text="∙", padding=10, width=6, command=lambda: self.add_to_exp("."), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt17 = ttk.Button(innerframe4, text="0", padding=10, width=6, command=lambda: self.add_to_exp("0"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt18 = ttk.Button(innerframe4, text="π", padding=10, width=6, command=lambda: self.add_pi("3.14159265"), takefocus=False).pack(side=LEFT, padx=2, pady=2)
		bt19 = ttk.Button(innerframe4, text="/", padding=10, width=6, command=lambda: self.add_to_exp("/"), takefocus=False).pack(side=TOP, padx=2, pady=2)

		innerframe5 = Frame(outerframe)
		innerframe5.config(bg="#141414")
		innerframe5.pack(side=TOP)

		bt20 = ttk.Button(innerframe5, text="AC", padding=10, width=10, command=self.all_clear, takefocus=False).pack(side=LEFT, padx=3, pady=2)
		bt21 = ttk.Button(innerframe5, text="=", padding=10, width=21, command=lambda: self.eval_exp(self.exp), takefocus=False).pack(side=LEFT, padx=2, pady=2)

		Label(root, text="- Dsoni01", pady=5, padx=5, fg="#414141", bg="#141414").place(relx=1.0, rely=1.0, x=0, y=0, anchor="se")


	# A decorator to Enable and disable text field
	def switch_mode(fn):
		def wrapper(self, *args):
			self.ans_label.config(state=NORMAL)
			fn(self, *args)
			self.ans_label.config(state=DISABLED)
		return wrapper


	def eval_exp(self, exp):
		try:
			res = round(eval(exp), 10)
			self.exp = str(res)
			self.clear_display()
			self.insert_val(res)
			self.flag = "result"
		except:
			self.all_clear()
			self.insert_val("\n\tSyntax Error!")
			self.flag = "message"


	def add_pi(self, v):
		if (self.exp and (self.exp[-1] not in self.oper_list)) or self.flag == "message":
			if self.exp[-1] not in ["("]:
				self.all_clear()
		self.flag = "expression"
		self.exp += v
		self.clear_display()
		self.insert_val(self.exp)


	def add_to_exp(self, val):
		if val in self.oper_list and self.exp.endswith(val):	# To prevent the insertion of multiple operators
			return
		elif self.flag == "message" or (self.flag == "result" and val not in self.oper_list):
			self.exp = ""
		self.flag = "expression"
		self.exp += val
		self.clear_display()
		self.insert_val(self.exp)


	@switch_mode
	def clear_display(self):
		self.ans_label.delete(1.0, END)


	@switch_mode
	def bkspc(self):
		if self.flag == "result":
			self.all_clear()
		v = -1
		if self.exp.endswith("**"):
			v = -2
		self.exp = self.exp[:v]
		self.clear_display()
		self.insert_val(self.exp)

	@switch_mode
	def insert_val(self, item):
		self.ans_label.insert(1.0, item)

	@switch_mode
	def all_clear(self):
		self.exp = ""
		self.ans_label.delete(1.0, END)


if __name__ == '__main__':
	root = Tk()
	root.resizable(0, 0)
	root.title("Calculator")
	root.geometry("350x420+700+300")
	root.configure(bg="#141414")
	Calculator()
	root.mainloop()