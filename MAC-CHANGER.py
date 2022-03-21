#!/usr/bin/env python

import subprocess

subprocess.call("ipconfig wlan0 down", shell=True)
subprocess.call("ipconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ipconfig wlan0 up", shell=True)
