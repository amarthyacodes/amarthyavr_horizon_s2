import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class distancesub(Node):
    def __init__(self):
        super().__init__('command')

        self.subscription = self.create_subscription(String, 'rover_command', self.callback, 10)
      # runs whenever a command is received
    def callback(self, msg):
        self.get_logger().info(f'Command received: {msg.data}')

def main(args=None):
    rclpy.init(args=args) # start ros
    node = distancesub() # create node
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown() # stop ros