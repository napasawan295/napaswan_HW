#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

frame = Tk()
frame.title("REMOTE")
frame.geometry("300x300")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)




def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z = 0.0
	pub.publish(cmd)
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x =-1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
def sl():
	print("sl")
	cmd = Twist()
	cmd.linear.x = 0
	cmd.linear.y = 1.0
	cmd.angular.z= 0
	pub.publish(cmd)
def sr():
	print("sr")
	cmd = Twist()
	cmd.linear.x = 0
	cmd.linear.y = -2.0
	cmd.angular.z= 0
	pub.publish(cmd)
	
def rotater():
	print("rotate r")
	cmd = Twist()
	cmd.linear.x = 0
	cmd.angular.y= -2.0
	cmd.angular.z= -1.0
	pub.publish(cmd)
	
def rotatel():
	print("rotate l")
	cmd = Twist()
	cmd.linear.x = 0
	cmd.angular.y= 2.0
	cmd.angular.z= 1.0
	pub.publish(cmd)
	
	
def reset():
	rospy.wait_for_service("reset")
	test_bg = rospy.ServiceProxy("reset", Empty)
	test_bg()
 

 	
B1 = Button(text = "FW", command=fw)
B1.place(x=150, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=150, y=170)

B3 = Button(text = "SL", command=sl)
B3.place(x=60, y=90)

B4 = Button(text = "SR", command=sr)
B4.place(x=250, y=90)

B5 = Button(text = "RotateR", command=rotater)
B5.place(x=280, y=150)

B6 = Button(text = "RotateL", command=rotatel)
B6.place(x=10, y=150)

B6 = Button(text = "Reset", command=reset)
B6.place(x=140, y=90)

frame.mainloop()
