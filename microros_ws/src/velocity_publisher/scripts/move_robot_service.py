#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rover_interfaces.srv import MoveDistance
import math

class MoveRobotService(Node):
    def __init__(self):
        super().__init__('move_robot_service')
        self.srv = self.create_service(MoveDistance, 'move_robot', self.move_robot_callback)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)

        self.current_position = None
        self.target_distance = 0.0
        self.start_position = None
        self.moving = False

    def odom_callback(self, msg):
        """ Actualiza la posición actual del robot """
        self.current_position = msg.pose.pose.position

        # Si el robot está en movimiento, verifica la distancia recorrida
        if self.moving and self.start_position is not None:
            distance_moved = math.sqrt(
                (self.current_position.x - self.start_position.x) ** 2 +
                (self.current_position.y - self.start_position.y) ** 2
            )

            self.get_logger().info(f"Distancia recorrida: {distance_moved:.2f} m")

            # Detener el robot si ya alcanzó la distancia deseada
            if distance_moved >= self.target_distance:
                self.stop_robot()
                self.moving = False

    def move_robot_callback(self, request, response):
        """ Mueve el robot la distancia solicitada """
        self.get_logger().info(f"Recibida solicitud de mover {request.distance} m")

        if self.current_position is None:
            self.get_logger().error("No se ha recibido odometría aún. Intenta de nuevo.")
            response.success = False
            return response

        self.target_distance = request.distance
        self.start_position = self.current_position
        self.moving = True

        # Publicar velocidad para mover el robot
        twist_msg = Twist()
        twist_msg.linear.x = 0.3  # Velocidad constante
        self.publisher_.publish(twist_msg)

        response.success = True
        return response

    def stop_robot(self):
        """ Detiene el robot publicando un mensaje de velocidad 0 """
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
        self.publisher_.publish(twist_msg)
        self.get_logger().info("✅ Robot detenido")

def main():
    rclpy.init()
    node = MoveRobotService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
