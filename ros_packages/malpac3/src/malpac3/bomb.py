#!/usr/bin/env python2
#this isn't important enough to license
#disables all networking devices temporarly
import os
import rospy
import time

def killnet():
    os.system("nmcli n off")
    time.sleep(5)
    os.system("nmcli n on")

if __name__ == '__main__':
    killnet()
