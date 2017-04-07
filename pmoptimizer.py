import os
import shutil
import argparse
from xml.etree import ElementTree as ET

EXT = '.pmdoc'
XML = '.xml'
OPTIMIZED = '_optimized'

def link_to_other_content(filename, link_to):
    tree = ET.parse(filename)
    root = tree.getroot()
    for content in root.findall('contents'):
        for file_list in content.findall('file-list'):
            print(f'linked {file_list.text} to {link_to}')
            file_list.text = link_to
    tree.write(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", help="Name of project to be optimized")
    parser.add_argument("-c", "--choice", help="Choice name which content will be linked to other choces")
    args = parser.parse_args()
    choice = args.choice
    project = args.project

    try:
        shutil.copytree(f'./{project}{EXT}', f'./{project}{OPTIMIZED}{EXT}')
    except FileExistsError:
        shutil.rmtree(f'./{project}{OPTIMIZED}{EXT}')
        shutil.copytree(f'./{project}{EXT}', f'./{project}{OPTIMIZED}{EXT}')

    all_files = os.listdir(f'./{project}{OPTIMIZED}{EXT}')
    files_to_link = list(filter(lambda f: f.endswith(f'{choice}{XML}') and \
                    not f.startswith('01'), all_files))
    files_to_remove = list(filter(lambda f: f.endswith(f'{choice}-contents{XML}') and \
                    not f.startswith('01'), all_files))
    list(map(lambda f: link_to_other_content(f'./{project}{OPTIMIZED}{EXT}/{f}', f'01{choice}-contents{XML}'), files_to_link))
    list(map(lambda f: os.remove(f'./{project}{OPTIMIZED}{EXT}/{f}'), files_to_remove))
