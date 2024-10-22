# A lower case stroke dictionary.
import re

LONGEST_KEY = 2

SHOW_STROKE_TRIGGER = 'STR*L'

PARTS_MATCHER = re.compile(
    r'(#?)(S?)(T?)(K?)(P?)(W?)(H?)(R?)(A?)(O?)([-*]?)(E?)(U?)(F?)(R?)(P?)(B?)(L?)(G?)(T?)(S?)(D?)(Z?)'
)

class Fingers:
    def __init__(self, front, side):
        self.front = front
        self.side = side

def construction(left, right, star):
    space = " "
    left_fingers = space.join(filter(bool, left.front))
    right_fingers = space.join(filter(bool, right.front))
    left_thumb = space + left.side if left.side else ''
    right_thumb = right.side + space if right.side else ''
    if left_fingers and star == "-" :
            star = ''
    left_star = star
    right_star = star
    gap = " " + space
    if not (left_fingers or left_thumb) :
        gap = ''
        left_star = ''
    if not (right_fingers or right_thumb) :
        gap = ''
        right_star = ''
    return '"' + left_fingers + left_star + left_thumb + \
           gap + right_thumb + right_star + right_fingers + '"'

def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    if SHOW_STROKE_TRIGGER != key[0]:
        raise KeyError
    if len(key) == 1:
        return ' '

    stroke = key[1]
    match = PARTS_MATCHER.fullmatch(stroke)
    if not match:
        raise KeyError
    (ht, s1, t1, k, p1, w, h, r1, a, o, star, e, u, f,
     r2, p2, b, l, g, t2, s2, d, z) = match.groups()
    left = Fingers( [ht + s1, t1 + k, p1 + w, h + r1], a + o )
    right = Fingers( [f + r2, p2 + b, l + g, t2 + s2, d + z], e + u )
    return construction(left, right, star).lower()
