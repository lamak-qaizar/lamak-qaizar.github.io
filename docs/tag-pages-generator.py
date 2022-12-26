#!/usr/bin/env python3

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    with open(filename, 'r', encoding='utf8') as f:
        file = f.read()

        import re
        matches = re.search('^tags:.*$', file, re.MULTILINE)
        if matches:
            total_tags.extend(matches.group().replace('tags:', '').split())

total_tags = set(total_tags)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    with open(tag_filename, 'a') as f:
        write_str = '---\nlayout: posts-by-tag\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
        f.write(write_str)
print("Tags generated, count", total_tags.__len__())