#!/usr/bin/env python3

'''
Script adapted from
https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py
by Long Qian
'''

POST_DIR = '_posts/'
TAG_DIR = 'tag/'

def read_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

import glob
import re
def all_tags():
    tags = set()
    for filename in glob.glob(f'{POST_DIR}*md'):
        matches = re.search('^tags:.*$', read_file(filename), re.MULTILINE)
        if matches:
            tags.update(matches.group().replace('tags:', '').split())
    return tags

import os
if not os.path.exists(TAG_DIR):
    os.makedirs(TAG_DIR)

for tag in all_tags():
    template = read_file('tag-page.template').replace("{tag}", tag)
    write_file(f'{TAG_DIR}{tag}.md', template)
    print(f'Generated page for tag "{tag}".')