/**
 * @file cpp_minimal_subscriber.cpp
 * @author Hardbotics
 * @brief Demonstrate subscribing to message on a ROS 2 topic 
 * @date 08-MAR-2026
 * 
 * --------------
 * Subscription Topics:
 * String message
 * /cpp_example_topic - std_msgs/String
 * --------------
 * 
 * Publishing Topics:
 * None
 */

#include "rclcpp/rclcpp.hpp" //Ros2 C++ client library
#include "std_msgs/msg/string.hpp" //Handle string messages

using std::placeholders::_1; //placeholder for callback function

class MinimalCppSubscriber : public rclcpp::Node
{
public:
    MinimalCppSubscriber() : Node("minimal_cpp_subscriber")
    {
        subscriber_ = create_subscription<std_msgs::msg::String>
            ("/cpp_example_topic",
                 10,
                  std::bind (
                    &MinimalCppSubscriber::topicCallback,
                     this,
                      _1));
    }
void topicCallback(const std_msgs::msg::String & msg) const
    {
        RCLCPP_INFO_STREAM(get_logger(), "I heard: " << msg.data.c_str());
    }

private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber_; //subscriber object
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto minimal_cpp_subscriber_node = std::make_shared<MinimalCppSubscriber>();
    rclcpp::spin(minimal_cpp_subscriber_node);

    rclcpp::shutdown();

    return 0;
}