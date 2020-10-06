from tkinter import *
from tkinter import messagebox
import time

"""Concept----->

   # This Concept is made to make the program too efficient in GUI apps

   1.Insert first: New node should add after the last node but the new node value should set to the
   first node of the list after shifting node value in a required direction. The shifting process of the new
   node after the last node will not include slow mode.....The process will so fast so that it seems
   that through the process new node set at first.

   2.Insert last: temp pointer should traverse until found the last node. After the last node new node
   will add.

   3.Insert after node: New node added to the last of the list. At first, after targeting node,
   node value movement from left to right and new node value should store after the targeting node.
   This is for efficient coding in that GUI apps. Though this is apart from actual concept but this
   is made to easily visualize the real logic of that program.

   4.Delete last: temp pointer should traverse until found the second last node. Then last node
   should delete from the list and second last node became the last node with having next part pointing
   NULL

   5.Delete first: Node value shift from right to left and then delete the last node. The process is
   too fast to imagine that node delete from first and second node became the first node of the
   list pointing by start pointer.

   6.Delete particular node: At first penultimate node of the targeting node is pointed by temp and
   targeting node is pointed by temp1. Then we have to delete last node from list and value shifting
   and storing done in a proper way. That logic is apart from real logic but to make GUI program too
   efficient, this path of visualization made, so that anybody can easily visualize the real logic
   of that program."""

class LinkList: # One and only class of that project
    def __init__(self,root):
        self.window = root
        self.window.config(bg="orange")

        #Make the Canvas
        self.canvas_make = Canvas(self.window,bg="chocolate",width=1350,height=500,relief=RAISED, bd=8)
        self.canvas_make.pack()

        #List make to store data
        self.linked_list_canvas_small_widget = [] #For widget number
        self.linked_list_canvas_small_widget_label = [] #For widget label
        self.linked_list_position = [] #For widget coordinate
        self.linked_list_data_next_store = [] #For data, arrow and next value store
        self.node_value_store = [] #For every node value

        # Entry value should be string variable
        self.value_entry = StringVar()
        self.position_entry = StringVar()
        self.delete_entry = StringVar()

        # Entry value by default set as black(" ")
        self.value_entry.set(" ")
        self.position_entry.set(" ")
        self.delete_entry.set(" ")

        #Label,entry and Button Initialization
        self.head_name = None
        self.information = None
        self.insert_at_beg = None
        self.insert_at_last = None
        self.delete_at_first = None
        self.delete_at_last = None
        self.position_label = None
        self.start_label = None
        self.temp_label = None
        self.temp1_label = None
        self.data_label = None
        self.next_label = None
        self.element_take_label = None
        self.element_take_entry = None
        self.add_btn = None
        self.value_set = None
        self.next_set = None
        self.start_initial_point_null = None
        self.new_node_label = None
        self.position_take_entry = None
        self.find_btn = None
        self.insert_after_node = None
        self.delete_particular_node = None

        #Canvas widget Initialization
        self.start_pointer = 0
        self.pointing_line_start = 0
        self.pointing_line_temp = 0
        self.pointing_line_temp1 = 0
        self.temp_pointer = 0
        self.temp1_pointer = 0
        self.data = 0
        self.next = 0
        self.main_container_node = 0
        self.arrow = 0

        #temp label corresponding line coordinate initialization
        self.pointing_line_temp_left = 65
        self.pointing_line_temp_up = 195

        # temp label coordinate initialization
        self.temp_label_x = 40
        self.temp_label_y = 150

        #temp label corresponding block coordinate initialization
        self.temp_pointer_left = 50
        self.temp_pointer_up = 180

        #node value containing label coordinate initialization
        self.value_set_x = 40
        self.value_set_y = 160

        #start label corresponding block coordinate initialization
        self.start_left = 50
        self.start_up = 380

        #data widget coordinate initialization
        self.data_left = 30
        self.data_up = 150

        # main node widget coordinate initialization
        self.main_node_left=25
        self.main_node_up = 120

        #node value containing label coordinate initialization
        self.data_label_x = 30
        self.data_label_y = 122

        # Initially required Function call
        self.heading_with_label_subheading()
        self.make_btn()
        self.make_start_with_other()

    # Heading and status/information initialization process
    def heading_with_label_subheading(self):
        self.head_name = Label(self.window,text="Singly Link List Visualizer ",font=("Arial",35,"bold","italic"),
                               bg="chocolate",fg="yellow")
        self.head_name.place(x=350,y=20)

        self.information =  Label(self.window,text="start is a pointer that pointing the first node and temp pointer is used at the time of \ninsert last and delete last to reach to the targeting location",font=("Arial",20,"bold","italic"),
                               bg="chocolate",fg="#00FF00")
        self.information.place(x=150,y=380)

    # start and other pointer initialization
    def make_start_with_other(self):
        #making of start pointer block
        self.start_pointer = self.canvas_make.create_rectangle(self.start_left,self.start_up,self.start_left+30,self.start_up+30,fill="blue",outline="black",width=3)

        #making of start label
        self.start_label = Label(self.canvas_make,text="start",font=("Arial",15,"bold"),bg="chocolate",
                                 fg="green")
        self.start_label.place(x=40,y=410)

        #making of start pointing line
        self.pointing_line_start = self.canvas_make.create_line(65,327,65,395,width=2,fill="green")

        #Making of NULL which is primarily pointing by start
        self.start_initial_point_null = Label(self.canvas_make, text="NULL", font=("Arial", 15, "bold"), bg="chocolate",
                                 fg="blue")
        self.start_initial_point_null.place(x=40, y=300)

        #Making of temp label without set coordinate(coordinate set in other function)
        self.temp_label = Label(self.canvas_make,text="temp",font=("Arial",15,"bold"),bg="chocolate",
                                 fg="green")

        self.temp1_label = Label(self.canvas_make, text="temp1", font=("Arial", 15, "bold"), bg="chocolate",
                                fg="green")

    # Make some buttons to give instruction to program
    def make_btn(self):
        self.insert_at_beg = Button(self.window,text="Insert first",bg="black",fg="red",
                                    font=("Arial",15,"bold"),relief=RAISED,bd=10,command=lambda: self.make_node_with_label(1))
        self.insert_at_beg.place(x=20,y=540)

        self.insert_at_last = Button(self.window, text="Insert last", bg="black", fg="red",
                                    font=("Arial", 15, "bold"), relief=RAISED, bd=10
                                     ,command=lambda: self.make_node_with_label(0))
        self.insert_at_last.place(x=220, y=540)


        self.delete_at_first = Button(self.window, text="Delete first", bg="black", fg="red",
                                     font=("Arial", 15, "bold"), relief=RAISED, bd=10,
                                      command=self.delete_first_node)
        self.delete_at_first.place(x=420, y=540)

        self.delete_at_last = Button(self.window, text="Delete last", bg="black", fg="red",
                                      font=("Arial", 15, "bold"), relief=RAISED, bd=10,
                                     command=lambda: self.delete_last_node(0))
        self.delete_at_last.place(x=620, y=540)

        self.insert_after_node = Button(self.window, text="Insert after node", bg="black", fg="red",
                                     font=("Arial", 15, "bold"), relief=RAISED, bd=10,state=NORMAL,
                                     command=self.set_of_input_method)
        self.insert_after_node.place(x=830, y=540)

        self.delete_particular_node = Button(self.window, text="Delete particular node", bg="black", fg="red",
                                        font=("Arial", 15, "bold"), relief=RAISED, bd=10, state=NORMAL,
                                        command=self.delete_single_node_infrastructure)
        self.delete_particular_node.place(x=1090, y=540)

    #Making of structure to take input about position
    def set_of_input_method(self):
        self.information.config(text="First node position: 1")

        self.position_label = Label(self.window,text="Enter the node position after you want to insert new node",font=("Arial",13,"bold"),bg="orange",
                                 fg="brown")
        self.position_label.place(x=750, y=620)

        self.position_take_entry = Entry(self.window, font=("Arial", 13, "bold"), bg="white", state=NORMAL,
                                         fg="blue", relief=SUNKEN, bd=5, textvar=self.position_entry)
        self.position_take_entry.place(x=810, y=650)

        self.position_take_entry.focus()

        self.find_btn = Button(self.window, text="Find", font=("Arial", 10, "bold"),
                               bg="blue", fg="red", relief=RAISED, bd=3, padx=3, pady=3,
                               state=NORMAL,command=self.checking_of_existence)
        self.find_btn.place(x=1020, y=650)

    # Positional node existence checking
    def checking_of_existence(self):
        self.position_label.place_forget()
        self.position_take_entry.place_forget()
        self.find_btn.place_forget()
        if int(self.position_entry.get())<1  or  int(self.position_entry.get()) > len(self.node_value_store):
            messagebox.showerror("Not found","The target node is not found")
            self.information.config(text="start is a pointer that pointing the first node and temp pointer is used at the time of \ninsert last and delete last to reach to the targeting location")
        else:
            self.insert_after_node.config(state=DISABLED)
            self.information.config(text="Targeting node found")
            self.make_node_with_label(2)

    # Node making process
    def make_node_with_label(self,take_notation):
        # Button deactivation
        self.insert_at_last.config(state=DISABLED)
        self.insert_at_beg.config(state=DISABLED)
        self.delete_at_last.config(state=DISABLED)
        self.delete_at_first.config(state=DISABLED)
        self.insert_after_node.config(state=DISABLED)
        self.delete_particular_node.config(state=DISABLED)

        #New_node label make
        self.new_node_label = Label(self.canvas_make,text="New node",font=("Arial",13,"bold"),bg="chocolate",
                                 fg="green")
        self.new_node_label.place(x=30, y=90)

        #Data widget making
        self.data = self.canvas_make.create_rectangle(self.data_left,self.data_up,self.data_left+40,self.data_up+30,outline="green",fill="yellow",width=3)

        # Data widget corresponding label making
        self.data_label = Label(self.canvas_make,text="data",font=("Arial",13,"bold"),bg="chocolate",
                                 fg="green")
        self.data_label.place(x=self.data_label_x, y=self.data_label_y)

        # Next widget making
        self.next = self.canvas_make.create_rectangle(self.data_left+50,self.data_up,self.data_left+50+40,self.data_up+30,outline="green",fill="yellow",width=3)

        # Next widget corresponding label making
        self.next_label = Label(self.canvas_make, text="next", font=("Arial", 13, "bold"), bg="chocolate",
                                fg="green")
        self.next_label.place(x=self.data_label_x+50, y=self.data_label_y)

        #Making of real node widget(outline border)
        self.main_container_node = self.canvas_make.create_rectangle(self.main_node_left, self.main_node_up,
                                                                     self.main_node_left + 100, self.main_node_up + 65,
                                                                     outline="brown", width=3)
        self.input_take(take_notation)

    # input taking process
    def input_take(self,take_notation):

        self.element_take_label = Label(self.window, text="Enter the element value",
                                        bg="orange", fg="brown", font=("Arial", 12, "bold"))
        self.element_take_label.place(x=10, y=620)

        self.element_take_entry = Entry(self.window, font=("Arial", 13, "bold"), bg="white", state=NORMAL,
                                        fg="blue", relief=SUNKEN, bd=5, textvar=self.value_entry)
        self.element_take_entry.place(x=10, y=650)

        # Default entry value set in __init__()

        self.element_take_entry.focus() #To focus in the entry box on activation

        self.add_btn = Button(self.window, text="Add", font=("Arial", 10, "bold"),
                              bg="blue", fg="red", relief=RAISED, bd=3, padx=3, pady=3,
                              command=lambda: self.make_main_container_with_node_value_set_and_next_arrow_creation(take_notation))
        self.add_btn.place(x=220, y=650)

        if take_notation==2: # For insert_after_node process
            self.element_take_label.config(text="Enter the new node value")
            self.element_take_label.place(x=810, y=620)
            self.element_take_entry.place(x=810, y=650)
            self.add_btn.place(x=1020, y=650)

        elif take_notation==3: # For delete_particular_node process
            self.element_take_label.config(text="Enter the node position")
            self.element_take_label.place(x=1100, y=620)
            self.element_take_entry.place(x=1100, y=650)
            self.add_btn.place(x=1300, y=650)

    # Working same as function name
    def make_main_container_with_node_value_set_and_next_arrow_creation(self,take_notation):
        #Deactivate the add btn
        self.add_btn.config(state=DISABLED)

        #Node value set
        self.value_set = Label(self.canvas_make, text=self.value_entry.get(),
                               font=("Arial", 10, "bold"), fg="green", bg="yellow")
        self.value_set.place(x=self.data_left + 8, y=self.data_up + 3)

        # Node next arrow set
        self.arrow = self.canvas_make.create_line(self.data_left+50 + 25, self.data_up + 15, self.data_left+50 + 65, self.data_up + 15, width=4)

        # Node next set
        self.next_set = Label(self.canvas_make, text="NULL", font=("Arial", 15, "bold"),
                              fg="green", bg="chocolate")
        self.next_set.place(x=self.data_left+50 + 52, y=self.data_up + 3)

        self.insert_node(take_notation)

        # take notation=0 means go to insert_at_last perform...
        # take notation=1 means go to insert_at_first perform...
        # take notation=2 means go to insert_after_node perform...
        # take notation=3 means go to delete_particular_node perform

    #Make insert first and insert last within that function
    def insert_node(self,take_notation):
        try:
            self.information.config(text=" ")
            self.new_node_label.place_forget()  # 'new node' label release
            self.start_initial_point_null.place_forget() # start pointing NULL release
            while True: # For vertical motion in three cases: insert_first, insert_last and insert_after_node
                   if take_notation == 1: #For insert first process
                      self.information.config(text="First node insertion process")
                   if self.main_node_up+65 <320: #For all function that allowed in that function
                       self.canvas_make.delete(self.main_container_node,self.data,self.next,self.arrow)
                       self.next_label.place_forget(); self.data_label.place_forget()
                       self.value_set.place_forget()
                       self.next_set.place_forget()
                       self.main_node_up +=10
                       self.data_up +=10
                       self.data_label_y +=10
                       self.main_container_node = self.canvas_make.create_rectangle(self.main_node_left, self.main_node_up, self.main_node_left+100,self.main_node_up+65, outline="brown",width=3)
                       self.data = self.canvas_make.create_rectangle(self.data_left, self.data_up, self.data_left+40, self.data_up+30, outline="green", fill="yellow", width=3)
                       self.next = self.canvas_make.create_rectangle(self.data_left+50, self.data_up, self.data_left+50+ 40, self.data_up+30, outline="green", fill="yellow", width=3)
                       self.next_label.place(x=self.data_label_x+50, y=self.data_label_y)
                       self.data_label.place(x=self.data_label_x, y=self.data_label_y)
                       self.value_set.place(x=self.data_left + 8, y=self.data_up + 3)
                       self.arrow = self.canvas_make.create_line(self.data_left+50 + 25, self.data_up + 15, self.data_left+50 + 65, self.data_up + 15, width=4)
                       self.next_set.place(x=self.data_left+50 + 52, y=self.data_up + 2)

                   else:
                       break

                   #time to sleep or slow motion
                   time.sleep(0.04)
                   self.window.update()

            if take_notation == 1:  #For insert first
                if len(self.node_value_store) >0:
                   self.information.config(text="Next part of New node contain the address of start pointing node and \nnow start pointing new node")
                else:
                    self.information.config(text="start pointing New node and next part of new node contains NULL")

            # Moving temp for insert last process
            if len(self.linked_list_data_next_store) > 1 and (take_notation==0 or take_notation==2):
                self.next_set.place_forget() #node next label place_forget()
                self.temp_label.place(x=self.temp_label_x, y=self.temp_label_y) #temp pointer start from first node

                #Making of start pointer pointing line
                self.pointing_line_temp = self.canvas_make.create_line(self.pointing_line_temp_left,
                                                                       self.pointing_line_temp_up,
                                                                       self.pointing_line_temp_left,
                                                                       self.pointing_line_temp_up + 65, width=2)

                #temp pointer movement process
                if take_notation==2:
                    goto = int(self.position_entry.get()) - 2
                else:
                    goto = len(self.linked_list_position) - 2

                # temp pointer movement until find the location
                while self.temp_label_x < self.linked_list_position[goto][4] + 100 + 20:
                    if take_notation == 2:# For insert_after_node()
                        if int(self.position_entry.get()) == 1: # For join after first node
                           break # In that case temp movement not required
                        self.information.config(text="Traversing until found the targeting node")#otherwise print that information

                    else:# For other function except insert_after_node()
                        self.information.config(text="Traversing until found the last node")

                    #pre location forget
                    self.temp_label.place_forget()
                    self.canvas_make.delete(self.pointing_line_temp,self.temp_pointer)

                    #temp pointer all coordinate change
                    self.temp_label_x += 10
                    self.pointing_line_temp_left += 10
                    self.temp_pointer_left +=10

                    self.temp_pointer = self.canvas_make.create_rectangle(self.temp_pointer_left, self.temp_pointer_up,
                                                                          self.temp_pointer_left + 30,
                                                                          self.temp_pointer_up + 30, fill="blue",
                                                                          outline="black", width=3)
                    self.temp_label.place(x=self.temp_label_x, y=self.temp_label_y)
                    self.pointing_line_temp = self.canvas_make.create_line(self.pointing_line_temp_left,
                                                                           self.pointing_line_temp_up,
                                                                           self.pointing_line_temp_left,
                                                                           self.pointing_line_temp_up + 65, width=2)
                    #used for slow the movement
                    time.sleep(0.05)
                    self.window.update()

            # For horizontal motion of the node
            if len(self.linked_list_data_next_store) >0:
                # Remove the NULL label from the last node
                self.linked_list_data_next_store[len(self.linked_list_data_next_store) - 1].pop().place_forget()
                # For horizontal motion of the node in both cases:insert_first and insert_last
                while self.main_node_left < self.linked_list_position[len(self.linked_list_position)-1][4]+100+20:
                        #previous coordinate and position delete of temp pointer
                        self.canvas_make.delete(self.main_container_node, self.data, self.next,self.arrow)
                        self.next_label.place_forget()
                        self.data_label.place_forget()
                        self.value_set.place_forget()
                        self.next_set.place_forget()

                        #new coordinate and position of the temp pointer
                        self.main_node_left += 10
                        self.data_left += 10
                        self.data_label_x += 10

                        #set in the new position
                        self.main_container_node = self.canvas_make.create_rectangle(self.main_node_left, self.main_node_up,
                                                                                     self.main_node_left + 100,
                                                                                     self.main_node_up + 65, outline="brown",
                                                                                     width=3)
                        self.data = self.canvas_make.create_rectangle(self.data_left, self.data_up, self.data_left + 40,
                                                                      self.data_up + 30, outline="green", fill="yellow",
                                                                      width=3)
                        self.next = self.canvas_make.create_rectangle(self.data_left+50, self.data_up, self.data_left+50 + 40,
                                                                      self.data_up + 30, outline="green", fill="yellow",
                                                                      width=3)

                        self.next_label.place(x=self.data_label_x+50, y=self.data_label_y)
                        self.data_label.place(x=self.data_label_x, y=self.data_label_y)
                        self.value_set.place(x=self.data_left + 8, y=self.data_up + 3)

                        self.arrow = self.canvas_make.create_line(self.data_left+50 + 25, self.data_up + 15, self.data_left+50 + 65, self.data_up + 15, width=4)
                        self.next_set.place(x=self.data_left+50 + 52, y=self.data_up + 2)

                        if take_notation == 0: # Makes for insert last only...
                            self.information.config(text="New node added to the last node")
                            time.sleep(0.02)
                            self.window.update()

                        if take_notation == 2: # No slow motion except insert last
                            self.information.config(text="New node added after the targeting node")


            #storing widget label
            temp_label = []
            temp_label.append(self.data_label)
            temp_label.append(self.next_label)
            self.linked_list_canvas_small_widget_label.append(temp_label)

            # storing widget
            temp_block_number = []; temp_block_number.append(self.data); temp_block_number.append(self.next); temp_block_number.append(self.main_container_node)
            self.linked_list_canvas_small_widget.append(temp_block_number)

            # storing widget coordinate
            temp_block_location = []
            temp_block_location.append(self.data_left); temp_block_location.append(self.data_up)
            temp_block_location.append(self.data_left+50); temp_block_location.append(self.data_up)
            temp_block_location.append(self.main_node_left); temp_block_location.append(self.main_node_up)
            self.linked_list_position.append(temp_block_location)

            # Forget temp pointer
            self.temp_label.place_forget()
            self.canvas_make.delete(self.pointing_line_temp,self.temp_pointer)
            self.temp_label_x = 40
            self.pointing_line_temp_left = 65
            self.temp_pointer_left = 50

            self.reset_with_store(take_notation)

        except:
            pass

    def reset_with_store(self,take_notation): # Reset coordinate and store value,arrow and next label
        #Node value store only in that list
        self.node_value_store.append(self.value_entry.get())

        temp = []
        temp.append(self.value_set)
        temp.append(self.arrow)
        temp.append(self.next_set)

        # Main list append
        self.linked_list_data_next_store.append(temp)

        # printing all list value ::Create this at the time of creation of the program to checking
        print(self.linked_list_data_next_store)
        print(self.linked_list_canvas_small_widget)
        print(self.linked_list_position)
        print(self.linked_list_canvas_small_widget_label)
        print(self.node_value_store)

        # data and next label reset
        self.value_set = None
        self.next_set = None

        #location forget of all under  input_take()
        self.element_take_label.place_forget()
        self.value_entry.set(" ")
        self.element_take_entry.place_forget()
        self.add_btn.place_forget()


        # process of value shifting in case of insert_first from left to right and new node insert at last
        if take_notation == 1 and len(self.linked_list_data_next_store) >1:
            temp_val = self.node_value_store[len(self.node_value_store)-1]
            for i in range(len(self.node_value_store)-2,-1,-1):
                self.node_value_store[i+1] = self.node_value_store[i]

            self.node_value_store[0] = temp_val

            #new value label set  :::::  after shifting through list
            for i in range(len(self.node_value_store)):
                self.linked_list_data_next_store[i][0].config(text=self.node_value_store[i])

        #Initialize of location of data next label and main block/node
        self.value_set_x = 40
        self.value_set_y = 160

        self.start_left = 50
        self.start_up = 380

        self.data_left = 30
        self.data_up = 150

        self.main_node_left = 25
        self.main_node_up = 120

        self.data_label_x = 30
        self.data_label_y = 122

        #Button state mode change
        self.insert_at_last.config(state=NORMAL)
        self.insert_at_beg.config(state=NORMAL)
        self.delete_at_last.config(state=NORMAL)
        self.delete_at_first.config(state=NORMAL)
        self.insert_after_node.config(state=NORMAL)
        self.delete_particular_node.config(state=NORMAL)

        #For insert after node function
        if take_notation == 2:
            # value shifting and store process
            temp_value = self.node_value_store[len(self.node_value_store)-1]
            for i in range(len(self.node_value_store)-2,int(self.position_entry.get())-1,-1):
                self.node_value_store[i+1] = self.node_value_store[i]
            self.node_value_store[int(self.position_entry.get())] = temp_value
            print(self.node_value_store)
            for i in range(int(self.position_entry.get()),len(self.linked_list_data_next_store)):
                self.linked_list_data_next_store[i][0].config(text=self.node_value_store[i])

    # For delete last node directly, for delete first and delete particular node indirectly
    def delete_last_node(self,locator):
        # printing all list value :: Create this at the time of creation of the program to checking
        print(self.linked_list_data_next_store)
        print(self.linked_list_canvas_small_widget)
        print(self.linked_list_position)
        print(self.linked_list_canvas_small_widget_label)
        print(self.node_value_store)


        if len(self.linked_list_data_next_store) == 0: # Checking if the list is empty
            messagebox.showerror("Underflow", "Link list is empty")
            return

        # Button state mode change
        self.insert_at_last.config(state=DISABLED)
        self.insert_at_beg.config(state=DISABLED)
        self.delete_at_last.config(state=DISABLED)
        self.delete_at_first.config(state=DISABLED)
        self.insert_after_node.config(state=DISABLED)
        self.delete_particular_node.config(state=DISABLED)

        #temp movement until found the second last node or targeting node
        if (locator == 0 or locator==3) and len(self.linked_list_data_next_store)>1:
            self.temp_pointer = self.canvas_make.create_rectangle(self.temp_pointer_left, self.temp_pointer_up,
                                                                  self.temp_pointer_left + 30,
                                                                  self.temp_pointer_up + 30, fill="blue",
                                                                  outline="black", width=3)
            self.temp_label.place(x=self.temp_label_x, y=self.temp_label_y)

            self.pointing_line_temp = self.canvas_make.create_line(self.pointing_line_temp_left,
                                                                   self.pointing_line_temp_up,
                                                                   self.pointing_line_temp_left,
                                                                   self.pointing_line_temp_up + 65, width=2)
            if len(self.linked_list_data_next_store) > 2:
                if locator == 3: # For delete particular node process
                    goto = int(self.delete_entry.get())-3
                else:
                    goto = len(self.linked_list_position) - 3
                while self.temp_label_x<self.linked_list_position[goto][4]+100+20:
                    if locator == 3:  # For delete particular node process
                        if int(self.delete_entry.get()) == 2:
                           break
                        else:
                            self.information.config(text="Traversing until found the penultimate node of the targeting node")
                    else:
                        self.information.config(text="Traversing until found the penultimate node of the last node")

                    # Forget temp pointer
                    self.temp_label.place_forget()
                    self.canvas_make.delete(self.pointing_line_temp,self.temp_pointer)

                    self.temp_label_x +=10
                    self.pointing_line_temp_left +=10
                    self.temp_pointer_left += 10

                    self.temp_pointer = self.canvas_make.create_rectangle(self.temp_pointer_left, self.temp_pointer_up,
                                                                          self.temp_pointer_left + 30,
                                                                          self.temp_pointer_up + 30, fill="blue",
                                                                          outline="black", width=3)
                    self.temp_label.place(x=self.temp_label_x, y=self.temp_label_y)
                    self.pointing_line_temp = self.canvas_make.create_line(self.pointing_line_temp_left, self.pointing_line_temp_up,
                                                                           self.pointing_line_temp_left,
                                                                           self.pointing_line_temp_up + 65, width=2)
                    time.sleep(0.04)
                    self.window.update()

            #stop some time to ensure that temp pointer reach the second last node or before the targeting node
            i=1
            while i<7:
                i+=2
                time.sleep(0.125)
                self.window.update()

            if locator == 0: #For last node deletion process
               self.information.config(text="Temp pointing node contains the address that present in the next part of last node and\nand Last node deleted")
            else:
                self.information.config(text="Targeting node deleted")

        if locator == 3: # For delete particular node process
           #temp1 pointer creation
           self.temp1_pointer = self.canvas_make.create_rectangle(self.temp_pointer_left+120, self.temp_pointer_up,
                                                                  self.temp_pointer_left + 120+30,
                                                                  self.temp_pointer_up + 30, fill="blue",
                                                                  outline="black", width=3)
           self.temp1_label.place(x=self.temp_label_x+120, y=self.temp_label_y)
           self.pointing_line_temp1 = self.canvas_make.create_line(self.pointing_line_temp_left+120,
                                                                   self.pointing_line_temp_up,
                                                                   self.pointing_line_temp_left+120,
                                                                   self.pointing_line_temp_up + 65, width=2)

           #status update
           self.information.config(text="Temp is pointing the penultimate node of the targeting node and \ntemp1 is pointing the targeting node")

           #Time to wait process
           i = 1
           while i < 7:
               i += 2
               time.sleep(2.5)
               self.window.update()

           #Value shifting and store in proper position for delete particular node process
           for i in range(int(self.delete_entry.get()), len(self.node_value_store)):
               self.linked_list_data_next_store[i-1][0].config(text=self.node_value_store[i])

           for i in range(int(self.delete_entry.get()),len(self.node_value_store)):
               self.node_value_store[i-1] = self.node_value_store[i]

        #Last node, first node, particular node deletion process
        if len(self.linked_list_data_next_store) > 0:
            # delete reference of last node from all list
            temp1 = self.linked_list_data_next_store.pop()
            temp1[0].place_forget()
            self.canvas_make.delete(temp1[1])
            temp1[2].place_forget()

            temp2 = self.linked_list_canvas_small_widget.pop()
            for i in range(len(temp2)):
                self.canvas_make.delete(temp2[i])

            self.linked_list_position.pop()

            if len(self.linked_list_data_next_store) > 0:
               temp3 = self.linked_list_position[len(self.linked_list_position)-1]
               self.next_set = Label(self.canvas_make, text="NULL", font=("Arial", 15, "bold"),
                                  fg="green", bg="chocolate")
               self.next_set.place(x=temp3[2]+52, y=temp3[3])

               self.linked_list_data_next_store[len(self.linked_list_data_next_store)-1].append(self.next_set)

            temp4 = self.linked_list_canvas_small_widget_label.pop()
            for widget_label in temp4:
                widget_label.place_forget()

            #Value delete from list storing only node value
            self.node_value_store.pop()
            print(self.node_value_store)

            # create start pointing NULL
            if len(self.linked_list_data_next_store) == 0:
               self.start_initial_point_null.place(x=40, y=300)

            #For delete last and delete particular node only
            if locator == 0 or locator == 3:
                if locator == 3:  # For temp 1 pointer delete process
                   self.temp1_label.place_forget()
                   self.canvas_make.delete(self.pointing_line_temp1, self.temp1_pointer)
                   self.information.config(text="The next part of the temp is now containing the address that is present in the \nnext part of temp1 and temp1 pointing node is deleted")

                # Time sleep to slow the process
                i = 1
                while i < 7:
                   i += 2
                   time.sleep(3)
                   self.window.update()

                #For temp pointer delete process
                self.temp_label.place_forget()
                self.canvas_make.delete(self.pointing_line_temp,self.temp_pointer)
                self.temp_label_x = 40
                self.pointing_line_temp_left = 65
                self.temp_pointer_left = 50

            # List empty checking with having last status to show
            if len(self.node_value_store) == 0:
               self.information.config(text="List is empty and start pointing NULL")
            elif locator == 0:
                self.information.config(text="Last node deleted")
            elif locator == 3:
                self.information.config(text="Targeting node deleted")

            #Button activation by changing state mode
            self.insert_at_last.config(state=NORMAL)
            self.insert_at_beg.config(state=NORMAL)
            self.delete_at_last.config(state=NORMAL)
            self.delete_at_first.config(state=NORMAL)
            self.insert_after_node.config(state=NORMAL)
            self.delete_particular_node.config(state=NORMAL)

    #For delete first
    def delete_first_node(self):
        if len(self.linked_list_data_next_store) == 0: # empty checking
            messagebox.showerror("Underflow","Link list is empty")


        elif len(self.node_value_store) == 1: # For one node in the list delete process same as delete last
            self.delete_last_node(1) #delete last function call
            self.information.config(text="Now start pointer is containing NULL and first node deleted")

        else:
            #For value shifting right to left
            for i in range(1,len(self.node_value_store)):
                self.node_value_store[i-1] = self.node_value_store[i]

            self.delete_last_node(1) #For delete the last node

            #After shifting new node value set
            for i in range(len(self.linked_list_data_next_store)):
                self.linked_list_data_next_store[i][0].config(text=self.node_value_store[i])

            self.information.config(text="Now start pointer is containing the address that present in the next part of the first node\nand first node deleted")

    #For delete particular node infrastructure
    def delete_single_node_infrastructure(self):
        if len(self.node_value_store) == 0: #Checking if link list is empty
           self.information.config(text="Link list is empty  ::  Nothing to delete")
           return
        else:
           self.information.config(text="First node position: 1")

        # Button deactivation
        self.insert_at_last.config(state=DISABLED)
        self.insert_at_beg.config(state=DISABLED)
        self.delete_at_last.config(state=DISABLED)
        self.delete_at_first.config(state=DISABLED)
        self.insert_after_node.config(state=DISABLED)
        self.delete_particular_node.config(state=DISABLED)

        #input taking process set
        self.position_label = Label(self.window, text="Enter the node position you want to delete",
                                    font=("Arial", 13, "bold"), bg="orange",
                                    fg="brown")
        self.position_label.place(x=1000, y=620)

        self.position_take_entry = Entry(self.window, font=("Arial", 13, "bold"), bg="white", state=NORMAL,
                                         fg="blue", relief=SUNKEN, bd=5, textvar=self.delete_entry)
        self.position_take_entry.place(x=1020, y=650)

        self.position_take_entry.focus()

        self.find_btn = Button(self.window, text="Find", font=("Arial", 10, "bold"),
                               bg="blue", fg="red", relief=RAISED, bd=3, padx=3, pady=3,
                               state=NORMAL, command=self.delete_single_node)
        self.find_btn.place(x=1230, y=650)

    # For delete particular node process start
    def delete_single_node(self):
        self.position_label.place_forget()
        self.position_take_entry.place_forget()
        self.find_btn.place_forget()

        # Node position checking
        if int(self.delete_entry.get())>len(self.node_value_store) or int(self.delete_entry.get())<1:
           messagebox.showerror("Error","Positional node not found")
        elif int(self.delete_entry.get()) == 1: #For only one node present in the list
           self.delete_first_node()
        else:
            self.delete_last_node(3)

        # Button activation
        self.insert_at_last.config(state=NORMAL)
        self.insert_at_beg.config(state=NORMAL)
        self.delete_at_last.config(state=NORMAL)
        self.delete_at_first.config(state=NORMAL)
        self.insert_after_node.config(state=NORMAL)
        self.delete_particular_node.config(state=NORMAL)

if __name__ == '__main__':
    window = Tk()
    window.title("Singly Linked List Visualizer")
    window.geometry("1350x730")
    window.iconbitmap("list_icon.ico")
    window.maxsize(1350,730)
    window.minsize(1350,730)
    LinkList(window)
    window.mainloop()
