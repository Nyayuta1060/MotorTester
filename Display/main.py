import serial
import tkinter as tk

root = tk.Tk()
footer = tk.Frame()

root.title("モー太郎ver.0.1(Beta)")
root.geometry("300x800")
root.resizable(False, False)
pwm = {0,0,0,0}

def sendcheck():
    canid = CANID_box.get()
    if(canid.isdecimal()):
        pwm = {PWM_box0.get(),PWM_box1.get(),PWM_box2.get(),PWM_box3.get()}
        for i in range(4):
            if(is_num(pwm[i]) == False):
                print("PWM["+str(i)+"]は数値で入力してください")
                return
        print(pwm)
        for i in range(4):
            if(abs(int(pwm[i])) >= 25000):
                print("PWM["+str(i)+"]は-25000~25000の範囲で入力してください")
                return
        send()
        return
    else:
        print("CANIDは数値で入力してください")
        return

def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def send():
    print("送信")
    pwm_colorchange()
def stop():
    print("停止")
    pwm = {0,0,0,0}
    send()

def pwm_colorchange():
    if int(PWM_box0.get()) > 0:
        PWM_box0.config(bg="orange")
    elif int(PWM_box0.get()) < 0:
        PWM_box0.config(bg="blue")
    else:
        PWM_box0.config(bg="green")
    
    if int(PWM_box1.get()) > 0:
        PWM_box1.config(bg="orange")
    elif int(PWM_box1.get()) < 0:
        PWM_box1.config(bg="blue")
    else:
        PWM_box1.config(bg="green")
    
    if int(PWM_box2.get()) > 0:
        PWM_box2.config(bg="orange")
    elif int(PWM_box2.get()) < 0:
        PWM_box2.config(bg="blue")
    else:
        PWM_box2.config(bg="green")

    if int(PWM_box3.get()) > 0:
        PWM_box3.config(bg="orange")
    elif int(PWM_box3.get()) < 0:
        PWM_box3.config(bg="blue")
    else:
        PWM_box3.config(bg="green")

    root.after(100, pwm_colorchange)

CANID_label = tk.Label(root, text="CANID:", font=("", 20))
CANID_box = tk.Entry(root, font=("", 20), width=2)
send_button = tk.Button(root, text="送信", command=sendcheck, width=8, height=3, bg="#3957db", fg="white")
stop_button = tk.Button(root, text="停止", command=stop, width=8, height=3, bg="#ff0000", fg="white")


CANID_label.place(x=10,y=10)
CANID_box.place(x=100,y=10)
send_button.place(x=235,y=750)
stop_button.place(x=120,y=750)
PWM_box0 = tk.Entry(root, font=("", 20), width=6)
PWM_box1 = tk.Entry(root, font=("", 20), width=6)
PWM_box2 = tk.Entry(root, font=("", 20), width=6)
PWM_box3 = tk.Entry(root, font=("", 20), width=6)
for i in range(4):
    PWM_label = tk.Label(root, text="PWM["+str(i)+"]:", font=("", 20))
    PWM_label.place(x=10,y=100+150*i)
    if i == 0:
        PWM_box0.place(x=120,y=100+150*i)
    elif i == 1:
        PWM_box1.place(x=120,y=100+150*i)
    elif i == 2:
        PWM_box2.place(x=120,y=100+150*i)
    elif i == 3:
        PWM_box3.place(x=120,y=100+150*i)

root.mainloop()