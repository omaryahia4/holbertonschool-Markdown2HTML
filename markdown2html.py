#!/usr/bin/python3
"""Markdown to HTML"""
from sys import argv, exit, stderr
import os, hashlib

def input_check():
    """Check input"""
    if len(argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    if not os.path.isfile(argv[1]):
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)

def file_to_array():
    with open(argv[1], 'r') as file:
        array = [line for line in file]
    return array

def parse_style(string):
    result = string
    if result.count('**') >= 2:
        i = 0
        while i < result.count('**'):
            result = result.replace('**', '<b>', 1)
            result = result.replace('**', '</b>', 1)
            i += 2
    
    if result.count("__") >= 2:
        i = 0
        while i < result.count('__'):
            result = result.replace('__', '<em>', 1)
            result = result.replace('__', '</em>', 1)
            i += 2
    return result

def parse_crypting(string):
    result = string
    if result.count('[[') == 1:
        text = result[result.index('[') + 2:result.index(']')]
        crypted = hashlib.md5(text.encode()).hexdigest()
        result = result.replace('[[', '').replace(']]', '').replace(text, crypted)
    if result.count('((') == 1:
        text = result[result.index('(') + 2:result.index(')')]
        crypted = text.replace('C', '').replace('c', '')
        result = result.replace('((', '').replace('))', '').replace(text, crypted)
    return result
        

def array_parser(array):
    result = ""
    i = 0
    while i < len(array):
        if '#' in array[i]:
            h_level = array[i].count("#")
            text = array[i].strip('#\n').rstrip().lstrip()
            html = "<h{}>{}</h{}>".format(h_level, text, h_level)
            result += html + '\n'
        elif '-' in array[i]:
            result += "<ul>\n"
            while i < len(array) and '-' in array[i]:
                text = array[i].strip('-\n').rstrip().lstrip()
                html = "<li>{}</li>".format(text)
                result += html + '\n'
                i += 1
            result += "</ul>\n"
        elif '*' in array[i]:
            result += "<ol>\n"
            while i < len(array) and '*' in array[i]:
                text = array[i].strip('*\n').rstrip().lstrip()
                html = "<li>{}</li>".format(text)
                result += html + '\n'
                i += 1
            result += "</ol>\n"
        elif array[i] != '\n':
            result += "<p>\n"
            while i < len(array) and array[i] != '\n':
                if i + 1 < len(array) and array[i + 1] != '\n':
                    result += array[i].replace('\n', '\n<br/>\n')
                elif array[i] != '\n':
                    result += array[i]
                i += 1
            result += "</p>\n"
        i += 1
    return result

def file_writer(text, html_file):
    with open(html_file, 'w') as file:
        file.write(text)
    exit(0)

def main():
    """Main func"""
    input_check()
    array = file_to_array()
    for i in range(len(array)):
        array[i] = parse_style(array[i])
        array[i] = parse_crypting(array[i])
    text = array_parser(array)
    file_writer(text, argv[2])


if __name__ == "__main__":
    main()
