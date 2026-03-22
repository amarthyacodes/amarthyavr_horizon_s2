import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ami/ros2_ws_bonus/install/distance_demo_bonus'
