import os
import argparse

from typing import List

PATH = os.path.dirname(os.path.realpath(__file__))

LEVEL_SYMBOLS = {
    1: '-',
    2: '*',
    3: '+'
}


def get_content(path: str = PATH) -> List[str]:
    lines = []

    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path) and full_path.endswith('.md'):
            with open(full_path) as file:
                for line in file:
                    if line.startswith('#'):
                        parts = line.split()
                        level = len(parts[0])
                        content = parts[1:]
                        content_title = ' '.join(content)
                        content_link = '-'.join([c.lower() for c in content])

                        indentation = get_correct_indentation(lines, level)
                        lines.append('{}{} [{}]({}#{})\n'
                                     .format(indentation, LEVEL_SYMBOLS.get((level - 1) % 3 + 1, '-'),
                                             content_title, item, content_link))

        elif os.path.isdir(full_path):
            lines.extend(get_content(full_path))

    return lines


def generate_mark_down_table_of_content(content: List[str],
                                        file_name: str = 'Table of Content',
                                        file_type: str = 'md',
                                        target_location: str = PATH):
    contents = ['# Table of Content\n', ''] + content
    file = '{}.{}'.format(file_name, file_type)
    file = os.path.join(target_location, file)

    with open(file, 'w') as writer:
        writer.write('\n'.join(contents))


def get_correct_indentation(lines: List[str], level: int) -> str:
    if not lines:
        return ''
    elif (level - 1) - lines[-1].count('\t') > 1:
        return '\t' * (lines[-1].count('\t') + 1)
    return '\t' * (level - 1)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=
                                     'Utilities to generate table of content across multiple markdown files',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-p', '--path', type=str,
                        help='root file path to start collect markdown files from', default=PATH)
    parser.add_argument('-s', '--save_path', type=str,
                        help='file path to save generated table of content markdown file', default=PATH)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    content = get_content(args.path)
    generate_mark_down_table_of_content(content)


if __name__ == '__main__':
    main()
