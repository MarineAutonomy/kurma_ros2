import rclpy
from rclpy.node import Node
import socket

class SocketPublisher(Node):
    def __init__(self):
        super().__init__('socket_publisher')
        self.get_logger().info('Socket Publisher Node Started')

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 10000)  # Update with the desired IP and port
        self.sock.connect(self.server_address)

        self.timer = self.create_timer(1.0, self.publish_values)

    def publish_values(self):
        # Example values to send
        value1 = 10
        value2 = 20.5
        value3 = 'Hello from ROS2'

        try:
            # Send the values through the socket
            message = f'{value1},{value2},{value3}'
            self.sock.sendall(message.encode())
            self.get_logger().info(f'Sent: {message}')
        except Exception as e:
            self.get_logger().error(f'Failed to send values: {e}')

    def __del__(self):
        self.sock.close()

def main(args=None):
    rclpy.init(args=args)
    node = SocketPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
