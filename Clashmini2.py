# -*- encoding=utf8 -*-
__author__ = "XLS"

import pprint

from airtest.report.report import simple_report
from public_method import *
from shop import *
from collocation import *

auto_setup(__file__, logdir=True, devices=["Android:///", ])

# script content
print("start...")
start_app("com.supercell.clashmini")
jump_collocation()
click_unlocked()
log_folder = create_timestamp_folder("./log/")
log_path = log_folder + "/log.html"
simple_report(__file__, logpath=True, output=log_path)
