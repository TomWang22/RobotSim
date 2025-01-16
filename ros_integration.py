import rospy
from geometry_msgs.msg import Twist

class ROSIntegration:
    def __init__(self):
        rospy.init_node('robot_simulation', anonymous=True)
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz

    def send_velocity_command(self, linear_x=0.0, angular_z=0.0):
        twist = Twist()
        twist.linear.x = linear_x
        twist.angular.z = angular_z
        self.cmd_pub.publish(twist)
        self.rate.sleep()

if __name__ == "__main__":
    ros = ROSIntegration()
    try:
        while not rospy.is_shutdown():
            ros.send_velocity_command(linear_x=0.5, angular_z=0.0)
    except rospy.ROSInterruptException:
        pass