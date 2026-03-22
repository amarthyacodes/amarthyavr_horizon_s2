import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class desicion(Node):
    def __init__(self):
        super().__init__('decision_node')

        self.subscription = self.create_subscription(Int32, 'distance', self.callback, 10)

        self.publisher = self.create_publisher(String, 'rover_command', 10)

    def callback(self, msg):
        distance = msg.data # get distance

        if distance < 30:
            command = "stop"
        else:
            command = "move_forward"

        cmd_msg = String()
        cmd_msg.data = command # put command in message
        self.publisher.publish(cmd_msg)

        self.get_logger().info(
            f'Received: {distance} | Command: {command}'
        ) # print both distance and what we decided

def main(args=None):
    rclpy.init(args=args) # start ros
    node = desicion() # create node
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown() # stop ros

