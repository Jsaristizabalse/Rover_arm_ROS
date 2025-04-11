#!/usr/bin/python3
import math
import threading
import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
#almacenamos las posiciones de los angulos
angle = np.array([0,0,0,0,0],float)

class Commander(Node):

    def __init__(self):
        super().__init__('commander')
        timer_period = 0.02


        #este arreglo almacena las posiciones de cada joint
        self.angle = angle
        self.mode_selection = 6  # 1:opposite phase, 2:diff_drive, 3: none

        #aqui se publican las posiciones en el topico
        self.pub_pos = self.create_publisher(Float64MultiArray, '/forward_position_controller/commands', 10)
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        self.pub_pos.publish(Float64MultiArray(data=self.angle))


#SE SUSCRIBE AL TOPICO DEL JOYSTICK
class JoySubscriber(Node):
    def __init__(self, commander):
        super().__init__('joy_subscriber')
        self.commander = commander
        self.subscription = self.create_subscription(Joy, 'joy', self.listener_callback, 10)

    def listener_callback(self, data):

        #usamos el lb
        if (data.buttons[6] == 1):
            self.commander.mode_selection = 1
            #movemos la palanca en el eje y
            self.commander.angle[0] = data.axes[0]
        elif(data.buttons[4] == 1):
            self.commander.mode_selection = 2
        elif (data.buttons[7] == 1):
            self.commander.mode_selection = 3
            self.commander.angle[2] = data.axes[0]
        elif (data.buttons[5] == 1):
            self.commander.mode_selection = 4
            self.commander.angle[3] = data.axes[0]
        elif (data.buttons[0] == 1):        
            self.commander.mode_selection = 5
            self.commander.angle[4] = data.axes[0]

        else:
            self.commander.mode_selection = 6   #no hace nada
        



if __name__ == '__main__':
    rclpy.init()

    commander = Commander()
    joy_subscriber = JoySubscriber(commander)
    
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(commander)
    executor.add_node(joy_subscriber)
    
    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()
    rate = commander.create_rate(2)
    try:
        while rclpy.ok():
            rate.sleep()
    except KeyboardInterrupt:
        pass
    
    rclpy.shutdown()
    executor_thread.join()
