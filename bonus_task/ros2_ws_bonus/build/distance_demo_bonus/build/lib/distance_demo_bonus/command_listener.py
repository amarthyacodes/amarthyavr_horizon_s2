import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandListener(Node):
    def __init__(self):
        super().__init__('command_listener')

        self.subscription = self.create_subscription(
            String,
            'rover_command',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'Command received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = CommandListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()