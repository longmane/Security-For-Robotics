#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# BEGIN KEYMAP
# key_mapping = { 'w': [ 0, 1], 'x': [0, -1], 
# 								'a': [-1, 0], 'd': [1,  0], 
# 								's': [ 0, 0] }
# END KEYMAP

keyins = {'r': 'r', 'h': 'h'}

# def keys_cb(msg, twist_pub):
# 	# BEGIN CB
# 	if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
# 		return # unknown key.
# 	vels = key_mapping[msg.data[0]]
# 	# END CB
# 	t = Twist()
# 	t.angular.z = vels[0]
# 	t.linear.x  = vels[1]
# 	twist_pub.publish(t)

def need2send(msg, sendmsg):
	print 'Send callback is happening!!\n\n'
	if msg in keyins:
		print str(msg) + '\n'
		print msg.data[0]
		sendmsg.publish(msg.data[0])

if __name__ == '__main__':
	rospy.init_node('userkey')
	print 'Userkey node started\n\n'
	sendmsg = rospy.Publisher('usersays', String, queue_size=1)
	rospy.Subscriber('keys', String, need2send, sendmsg)
	rospy.spin()