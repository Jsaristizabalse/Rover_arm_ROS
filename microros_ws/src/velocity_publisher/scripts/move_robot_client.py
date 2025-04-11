#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from rover_interfaces.srv import MoveDistance

class MoveRobotClient(Node):
    def __init__(self):
        super().__init__('move_robot_client')
        self.client = self.create_client(MoveDistance, 'move_robot')

        while not self.client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('Esperando el servicio...')

    def send_request(self, distance):
        """ Envia una solicitud al servicio con la distancia deseada """
        request = MoveDistance.Request()
        request.distance = distance

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        return future.result()

def main():
    rclpy.init()
    client = MoveRobotClient()

    try:
        distance = float(input("Ingrese la distancia a mover (m): "))
        response = client.send_request(distance)

        if response.success:
            print(f"✅ El robot se movió {distance} metros correctamente.")
        else:
            print("❌ Hubo un error en el movimiento.")

    except Exception as e:
        print(f"Error: {e}")

    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
