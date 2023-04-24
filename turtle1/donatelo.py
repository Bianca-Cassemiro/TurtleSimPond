#!/usr/bin/env python3

#importação das bibliotecas e funções necessárias
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()
        #Criação de variáveis de controle
        self.session = 1 
        self.controller = 0 
        
    #Função que controla as movimentações que estão senod feitas no momento
    def move_turtle(self):
        if self.session == 1:
            self.firtSession()
            self.controller +=1
        elif self.session == 2:
            self.secondSession()
            self.controller +=1
        else:
            self.thirdSession()
            self.controller +=1

        if self.controller >= 10:
            self.session = (self.session % 3) + 1
            self.controller = 0
    
    #Definição das movimentações
    def firtSession(self):
        self.twist_msg_.linear.x = 0.8 
        self.twist_msg_.angular.z = 0.5
        self.publisher_.publish(self.twist_msg_)

    def secondSession(self):
        self.twist_msg_.linear.x = 0.5
        self.twist_msg_.angular.z = -0.5
        self.publisher_.publish(self.twist_msg_)

    def thirdSession(self):
        self.twist_msg_.linear.x = -1.2
        self.twist_msg_.angular.z = 0.5
        self.publisher_.publish(self.twist_msg_)
   
  

    

def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
