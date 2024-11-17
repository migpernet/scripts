#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker',anonymous=True)

    pub = rospy.Publisher('/chatter',String,queue_size=100)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        texto = 'Hello world %s' % rospy.get_time()

        rospy.loginfo(texto)

        pub.publish(texto)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass