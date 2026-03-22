import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class distancepub(Node):
    def __init__(self):
        super().__init__('distance_pub') # publisher for distance topic
        self.pub = self.create_publisher(Int32, 'distance', 10)
        self.timer = self.create_timer(1.0, self.send_distance) # runs every 1 sec

    def send_distance(self):
        dist = random.randint(1, 100)  # random distance
        msg = Int32()
        msg.data = dist
        self.pub.publish(msg)
        self.get_logger().info(f'sent distance: {dist}') # printing

def main(args=None):
    rclpy.init(args=args) # start ros
    node = distancepub() # create node
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown() # stop ros

if __name__ == '__main__':
    main() # run everything