import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from std_msgs.msg import Bool

class PositionController(Node):
    def __init__(self):
        super().__init__("position_controller")

        #Movement command
        self.movement_subscription = self.create_subscription(
            Twist,
            "movement_command",
            self.movement_callback,
            10
        )
        self.x = 0
        self.y = 0

        #Emergency stop
        self.emergency_subscription = self.create_subscription(
            Bool,
            "emergency_stop",
            self.emergency_callback,
            10
        )
        self.e_brake = False

        #Position publisher
        self.publisher = self.create_publisher(Point, "position", 10)

    def publish_position(self):
        position = Point()
        position.x = self.x
        position.y = self.y
        self.publisher.publish(position)

    def movement_callback(self, msg):
        if not self.e_brake:
            self.x += msg.linear.x
            self.y += msg.linear.y

        if self.x >= 10: self.x = 10
        elif self.x <= -10: self.x = -10

        if self.y >= 10: self.y = 10
        elif self.y <= -10: self.y = -10

        self.publish_position()

        self.get_logger().info(f"x: {self.x}, y: {self.y}")

    def emergency_callback(self, msg):
        self.e_brake = msg.data
        #self.get_logger().info(f"Emergency brake: {self.e_brake}")
    

def main(args=None):
    rclpy.init(args=args)
    node = PositionController()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
if __name__ == "__main__":
    main()