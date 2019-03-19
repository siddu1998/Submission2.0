import sys
if 3 == sys.version_info[0]:  ## 3.X is default if dual system
    import tkinter as tk     ## Python 3.x
else:
    import Tkinter as tk     ## Python 2.x
from functools import partial

class SampleApp():
    def __init__(self, root):
        self.root=root
        self.button_dict={}
        self.frame_dict={}
        self.create_buttons()
        self.start_page_frame()

        for classname, lit in [(PageOne, "PageOne"), (PageTwo, "PageTwo")]:
            instance=classname(root)
            self.frame_dict[lit]=instance.page_frame

    def button_press(self, button_id):
        """
            deselect current frame's button, and activate all others
        """
        print(button_id)
        for key in self.button_dict:
            if key==button_id:
                self.button_dict[key].config(state="disabled")
            else:
                self.button_dict[key].config(state="normal")

        ## raise the frame corresponding to the button clicked
        self.frame_dict[button_id].lift()

    def create_buttons(self):
        """ 
             create one set of buttons in a separate frame instead
             of creating them over and over in each separate class

             you can also use a simple for() to create these
        """
        self.button_frame=tk.Frame(self.root)
        self.button_frame.grid(row=10, column=0)

        button0 = tk.Button(self.button_frame, text="Go to Start Page",
                            bg="lightblue", width=15,
                            command=partial(self.button_press, "StartPage"))
        button0.grid(row=0, column=0, sticky="ew")
        self.button_dict["StartPage"]=button0

        button1 = tk.Button(self.button_frame, text="Go to Page One",
                            bg="yellow", width=15, 
                            command=partial(self.button_press, "PageOne"))
        button1.grid(row=0, column=1, sticky="ew")
        self.button_dict["PageOne"]=button1

        button2 = tk.Button(self.button_frame, text="Go to Page two",
                            bg="lightgreen", width=15,
                            command=partial(self.button_press, "PageTwo"))
        button2.grid(row=0, column=2, sticky="ew")
        self.button_dict["PageTwo"]=button2
        button2.config(state="disabled")

        button_quit = tk.Button(self.button_frame, text="Exit", bg="orange",
                                command=self.root.quit)
        button_quit.grid(row=5, column=0, columnspan=3, sticky="ewns")

    def start_page_frame(self):
        start_frame=tk.Frame(self.root, width=25, height=25)
        tk.Label(start_frame,  width=24, bg="lightblue",
                text="This is the start page").grid(row=0, column=0, sticky="ew")
        start_frame.grid(row=0, column=0, sticky="ns")
        self.frame_dict["StartPage"]=start_frame

class PageOne():
    def __init__(self, parent):
        ## frame must be named self.page_frame to work in for() above
        self.page_frame=tk.Frame(parent)
        self.label_text=tk.StringVar()
        tk.Label(self.page_frame,  width=24,
                         textvariable=self.label_text,
                         bg="yellow").grid(row=0, column=0, sticky="ew")
        self.label_text.set("This is page one")
        self.page_frame.grid(row=0, column=0)

        # show how a button or some other widget is added to one of the classes
        self.ctr=0
        tk.Button(self.page_frame, text="Change label text",
                  command=self.change_label_text).grid(row=5, column=0)


    def change_label_text(self):
        text_list=["this is page one", "new message page one",
                   "third message for page one"]
        self.ctr += 1
        if self.ctr >= len(text_list):
            self.ctr=0
        self.label_text.set(text_list[self.ctr])

class PageTwo():
    def __init__(self, parent):
        ## frame must be named self.page_frame to work in for() above
        self.page_frame=tk.Frame(parent, width=25, height=25)
        label = tk.Label(self.page_frame,  width=24,
                         text="This is page two",
                         bg="lightgreen").grid(row=0, column=0, sticky="ew")
        self.page_frame.grid(row=0, column=0, sticky="ns")

root=tk.Tk()
SA=SampleApp(root)
root.mainloop()