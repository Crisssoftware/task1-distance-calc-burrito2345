import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import String
import math

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(String, '/turtle1/distance_from_origin', 10)
    def listener_callback(self, msg):
        x = msg.x
        y = msg.y
        dis = String()
        dis.data = str(math.sqrt(x*x+y*y))
        self.publisher_.publish(dis)
        self.get_logger().info('I heard: "%s"' % dis.data )  


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
