import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class AvoidNode(Node):
    def __init__(self):
        super().__init__('tb3_avoid')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, 'scan', self.callback, 10)
        self.get_logger().info("Obstacle Avoidance Node Started")

    def callback(self, msg):
        twist = Twist()

        # Minimum distance in front arc
        front_ranges = msg.ranges[0:30] + msg.ranges[330:360]
        min_front = min(front_ranges)

        if min_front < 0.5:
            twist.linear.x = 0.0
            twist.angular.z = 0.6
        else:
            twist.linear.x = 0.15
            twist.angular.z = 0.0

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = AvoidNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

