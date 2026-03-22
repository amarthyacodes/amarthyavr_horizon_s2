import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class distancesub(Node):
    def __init__(self):
        super().__init__('distance_sub')
        self.sub = self.create_subscription(Int32, 'distance', self.recv_distance, 10)

    def recv_distance(self, msg):
        self.get_logger().info(f'got distance: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = distancesub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()