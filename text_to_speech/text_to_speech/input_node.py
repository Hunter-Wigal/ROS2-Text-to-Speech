import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class VoicePublisher(Node):

    def __init__(self):
        super().__init__('voice_publisher')
        self.publisher_ = self.create_publisher(String, 'voice', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = String()
        msg.data = input("Enter something for Heimdall to say: ")
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    voice_publisher = VoicePublisher()

    rclpy.spin(voice_publisher)

    voice_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()