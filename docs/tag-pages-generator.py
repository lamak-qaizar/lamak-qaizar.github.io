#!/usr/bin/env python3

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''


post_dir = '_posts/'
tag_dir = 'tag/'

def read_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

import glob
total_tags = set()
for filename in glob.glob(f'{post_dir}*md'):
    import re
    matches = re.search('^tags:.*$', read_file(filename), re.MULTILINE)
    if matches:
        total_tags.update(matches.group().replace('tags:', '').split())

import os
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    template = read_file('tag-page.template').replace("{tag}", tag)
    write_file(f'{tag_dir}{tag}.md', template)
print("Tags generated, count", total_tags.__len__())