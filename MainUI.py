from tkinter import *
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

root = Tk()  # create root window
root.title("Smart Mirror Main")  # title of the GUI window
root.geometry("1060x1300")  # specify the max size the window can expand to
root.config(bg="black")  # specify background color


root.wm_attributes('-transparentcolor', '#ab23ff')

#Main layout frames
left_frame = Frame(root, width=250, height=950, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5,sticky=NSEW )


mid_frame = Frame(root, width=500, height=950, bg='grey')
mid_frame.grid(row=0, column=2, padx=10, pady=5, sticky=NSEW)

right_frame = Frame(root, width=250, height=1050, bg='grey')
right_frame.grid(row=0, column=3, padx=10, pady=5, sticky=NSEW)

#Individual components 
#left
Name_frame = Frame(left_frame, width=230, height=100, bg='blue')
Name_frame.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

Label(Name_frame, text= "Welcome", font= ('Helvetica 20'), fg='black', bg= 'blue').grid(row=0, column=0,padx= (15, 0), pady=(10, 2))
Label(Name_frame, text= "{Name}", font= ('Helvetica 20'), fg='black', bg= 'blue').grid(row=1, column=0,padx= (65, 0), pady=(0, 10))


Calendar_frame = Frame(left_frame, width=230, height=570, bg='blue')
Calendar_frame.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

Label(Calendar_frame, text= "Daily View", font= ('Helvetica 20'), fg='black', bg= 'blue').grid(row=0, column=0, padx= (45, 25),  pady=(5,15))


Label(Calendar_frame, text= "Temp Calendar 1", font= ('Helvetica 15'), fg='black', bg= 'blue').grid(row=1, column=0,padx= (10, 0), pady=(10, 2))
Label(Calendar_frame, text= "Placeholder time", font= ('Helvetica 10'), fg='black', bg= 'blue').grid(row=2, column=0,padx= (28, 0), pady=(0, 30), sticky=W)

Label(Calendar_frame, text= "Temp Calendar 1", font= ('Helvetica 15'), fg='black', bg= 'blue').grid(row=3, column=0,padx= (10, 0), pady=(10, 2))
Label(Calendar_frame, text= "Placeholder time", font= ('Helvetica 10'), fg='black', bg= 'blue').grid(row=4, column=0,padx= (28, 0), pady=(0, 30), sticky=W)

Label(Calendar_frame, text= "Temp Calendar 1", font= ('Helvetica 15'), fg='black', bg= 'blue').grid(row=5, column=0,padx= (10, 0), pady=(10, 2))
Label(Calendar_frame, text= "Placeholder time", font= ('Helvetica 10'), fg='black', bg= 'blue').grid(row=6, column=0,padx= (28, 0), pady=(0, 60), sticky=W)

Reminder_frame = Frame(left_frame, width=230, height=250, bg='blue')
Reminder_frame.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)
var1 = IntVar()

Label(Reminder_frame, text= "Reminders", font= ('Helvetica 20'), fg='black', bg= 'blue').grid(row=0,  column=0, padx= (35, 25),  pady=(5,10))

Checkbutton(Reminder_frame, text='Reminder 1',font=('Helvetica 12'),fg='black', bg= 'blue', variable=var1, onvalue=1, offvalue=0).grid(row=1,  column=0, padx= (20 ,15),  pady=(5,15), sticky=W)



#Right
Clock_frame = Frame(right_frame, width=230, height=400, bg='blue')
Clock_frame.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

clock_label = Label(Clock_frame, font= ('Helvetica 30'), fg='black', bg= 'blue')
clock_label.grid(row=0, column=0,padx=35, pady=25, sticky=NSEW)

Weather_frame = Frame(right_frame, width=230, height=200, bg='blue')
Weather_frame.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

Maps_frame = Frame(right_frame, width=230, height=490, bg='blue')
Maps_frame.grid(row=3, column=0, padx=10, pady=5, sticky=NSEW)

Tasks_frame = Frame(right_frame, width=230, height=120, bg='blue')
Tasks_frame.grid(row=4, column=0, padx=10, pady=5, sticky=NSEW)

Label(Tasks_frame, text= "Quick Tasks", font= ('Helvetica 20'), fg='black', bg= 'blue').grid(row=0, column=0, padx= (35, 25),  pady=(5,0))

Label(Tasks_frame, text= "How long to work", font= ('Helvetica 12'), fg='black', bg= 'blue').grid(row=1, column=0,padx= (10, 0), pady=(5, 2))
Label(Tasks_frame, text= "Weather tonight", font= ('Helvetica 12'), fg='black', bg= 'blue').grid(row=2, column=0,padx= (10, 0), pady=(5, 2))
Label(Tasks_frame, text= "Set reminder to do work", font= ('Helvetica 12'), fg='black', bg= 'blue').grid(row=3, column=0,padx= (10, 0), pady=(5, 2))
""" # Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)  """

#if statement which constantly returns true to make the timer refresh and tick
if __name__ == "__main__":
    update_time()
    root.mainloop()



import vonage

def send_sms(api_key, api_secret, from_number, to_number, message):
    client = vonage.Client(key=api_key, secret=api_secret)
    sms = vonage.Sms(client)

    response = sms.send_message({
        'from': from_number,
        'to': to_number,
        'text': message,
    })

    if response['messages'][0]['status'] == '0':
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response['messages'][0]['error-text']}")

# Replace the following variables with your own details
api_key = 'cfed9634'            # Your Vonage API key
api_secret = 'XjlMjmOizlm3HYNg'      # Your Vonage API secret
from_number = '15193426422'  # Your Vonage phone number in international format
to_number = '16479269773'    # Your friend's phone number in international format
message = 'Hello from Python!'      # The message you want to send

send_sms(api_key, api_secret, from_number, to_number, message)

