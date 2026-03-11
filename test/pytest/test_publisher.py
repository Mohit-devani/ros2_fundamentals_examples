#!usr/bin/env python3

"""
test suits for the ros2 minimal publisher node.

this script contains unit tests for the verifying the functionality of a minimal ros2 publisher.
It tests the creation, message counter increment, and message content formatting.

---------------
Subscription topics:
None

---------------

Publishing topics:
- /py_example_topic (std_msgs/msg/String): Example messages with incrementing counter.

:author : Hardbotics
:date : 09/03/2026

"""

import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher

def test_publisher_creation():
    """
    Test if the publisher node can be created successfully.
    
    This test verifies that the publisher node initializes without errors and is ready to publish messages.
    
    1. The node name is set correctly.
    2. the publisher object exists and is of the correct type.
    3. the topic name is correct.
    
    : raise AssertionError: If any of the checks fail

    """

    #initialize the ROS2 communication
    rclpy.init()

    try:
       # create an instance of our publisher node
       node = MinimalPyPublisher()

       #test 1: verify the node has the expected name 
       assert node.get_name() == "minimal_py_publisher"

       #test2: verify the publisher exists and has the correct topic name 
       assert hasattr(node, 'publisher_1')
       assert node.publisher_1.topic_name == '/py_example_topic'

    finally:
        # cleanup for ros2 communication
        rclpy.shutdown()

def test_message_counter():
    """
    Test if the message counter increments correctly.
    
    This test verifies that the counter (node.i) increases by 1 after each timer callback execution,
    
    :raises: AssertionError if the counter does not increment as expected.

    """

    rclpy.init()

    try:
        node = MinimalPyPublisher()

        # store the initial value of the counter
        initial_counter = node.i

        # simulate timer callback execution
        node.timer_callback()
        assert node.i == initial_counter + 1

    finally:
        rclpy.shutdown()
    

def test_message_content():
    """
    Test if the message content is formatted correctly.
    
    This test verifies that the message published by the node contains the expected string format,
    including the correct counter value.
    
    :raises: AssertionError if the message content does not match the expected format.

    """

    rclpy.init()

    try:
        node = MinimalPyPublisher()

        node.i = 5
        msg = String()

        msg.data = f'Hello World: {node.i}'
        assert msg.data == 'Hello World: 5'

    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    pytest.main(['-v'])
