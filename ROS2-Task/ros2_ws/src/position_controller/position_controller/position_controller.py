import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class PositionController(Node):
    def __init__(self):
        super().__init__("position_controller")
        self.subscription = self.create_subscription(
            Twist,
            "movement_command",
            self.movement_callback,
            10
        )
        self.subscription
        self.x = 0
        self.y = 0

    def movement_callback(self, msg):
        self.x += msg.linear.x
        self.y += msg.linear.y
        self.get_logger().info(f"x: {self.x}, y: {self.y}")
    

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