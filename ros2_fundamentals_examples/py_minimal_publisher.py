#! /usr/bin/env python3

"""
Description:
    this ros2 node peridically publishes "hello world" message to a topic.

------
publishing topics:
    the channel containing the "hello world" messages
    /py_example_topic - std_msgs/String

Subscription topics:
    None

-------

Author: Hardbotics   
Date: Feb 3 2026
"""

import rclpy #import ros2 client library for python 
from rclpy.node import Node # Import the node class , used for creating nodes

from std_msgs.msg import String #import string message type for ros2

class minimalPyPublisher(Node):

    """ create a minimal publisher node.
    
    """
    def __init__ (self):
        """create a custom node class for publishing messages
        """
        #initialize the node with a name 
        super().__init__('minimal_py_publisher')

        #create a publisher on the topic with a queue size of 10 messages
        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

        #create a timer with a period of 0.5 seconds to trigger publishing of message
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        #intialize a counter variable for message content 
        self.i = 0

    def timer_callback(self):
        """callback function executed periodically by the timer
        """
        #creare a new string message object
        msg = String()
    
        #set the message data with a counter
        msg.data = 'hello world: %d' % self.i

        #publish the messafe you created above to topic
        self.publisher_1.publish(msg)

        #log a message indicating the messag has been published
        self.get_logger().info('Publishing: "%s"' %msg.data)

        self.i = self.i + 1

def main(args = None):
    """Main function to start the ros2 node

    Args:
        args (list, optional): command line arguement, default to none.
    """
    rclpy.init(args = args)

    #create an instance of the minimal publisher node
    minimal_Py_Publisher = minimalPyPublisher()

    rclpy.spin(minimal_Py_Publisher)

    #destroy the node explicitly
    minimal_Py_Publisher.destroy_node()

    #shutdown ros2 communication 
    rclpy.shutdown()

if __name__ == '__main__':
    #execute the main function if the scriot is run directly
    main()
