import unittest


class Entity:
    type = None
    value = None


def eat_entity(s):
    e = Entity()
    if s.startswith('</'):
        e.type = 'color_close_tag'
        endpos = s.find('>')
        e.value = s[2:endpos]
    elif s.startswith('<'):
        e.type = 'color_open_tag'
        endpos = s.find('>')
        e.value = s[1:endpos]
    elif s[0].isalpha():
        e.type = 'lowercase_letter'
        endpos = 0
    elif s[0].isspace():
        e.type = 'space'
        endpos = 0

    return e, s[endpos + 1:]


def count_colors(s):
    color_stack = []

    color_cnts = {
        'red': 0,
        'blue': 0,
        'yellow': 0
    }

    while len(s) > 0:
        entity, s = eat_entity(s)
        if entity.type == 'color_open_tag':
            color_stack.append(entity.value)
        elif entity.type == 'color_close_tag':
            color_stack.pop()
        elif entity.type == 'lowercase_letter':
            if color_stack:
                current_color = color_stack[-1]
                color_cnts[current_color] += 1

    return [
        color_cnts['red'],
        color_cnts['yellow'],
        color_cnts['blue']
    ]


class Test(unittest.TestCase):
    def test_1(self):
        s = '<yellow>aaa<blue>bbb</blue>ccc</yellow>dddd<red>abc</red>'
        self.assertEqual([3, 6, 3], count_colors(s))

    def test_2(self):
        s = '<yellow>aaa<blue>bbb</blue>ccc</yellow>'
        self.assertEqual([0, 6, 3], count_colors(s))

if __name__ == '__main__':
    text = raw_input()
    for cnt in count_colors(text):
        print cnt,