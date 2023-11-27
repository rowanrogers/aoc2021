from helper.fetchInput import get_input
from collections import namedtuple
import itertools
from math import prod


# first 3 bits - version numbers
# next 3 bits - typeid numbers

#type id 4 means a literal value

# you read 5 character patterns, if the first character of each pattern is a 1 then it's not the last pattern
# if it is a 0 then it's the last 5 bit pattern
# once you've got your 5 bit pattersn you remove the leading character and read it as a binary number

# if type id is anything other than 4 then it's an operator
# in which case the 7th bit (after the 3 version bits and typeid bits) is the length type id.
# if length typeid = 0 then the next 15 bits are a number representing the total length in bits of sub-packets contained by the packet

# if length typeid = 0 then the next 11 bits are a number representing the total number of sub-packets contained by the packet


def hex_to_bits(it):
    for c in it:
        n = int(c, 16)
        yield n & 8 != 0
        yield n & 4 != 0
        yield n & 2 != 0
        yield n & 1 != 0


def next_bits(it, n):
    value = 0
    for _ in range(n):
        value = 2 * value + next(it)
    return value


def parse_packet(it):

    version = next_bits(it, 3)
    typeid = next_bits(it, 3)

    if typeid == 4:

        value = 0

        while True:
            cont = next(it)
            value = 16 * value + next_bits(it, 4)

            if not cont:
                return Literal(version=version, value=value)


    if next(it):
    # this tests the length id. If 1 then we know number of subpackets

        children = [parse_packet(it) for _ in range(next_bits(it, 11))]

    else:
        children = []
        it2 = itertools.islice(it, next_bits(it, 15))

        try:
            while True:
                children.append(parse_packet(it2))

        except StopIteration:
            pass

    return Operator(version=version, type=typeid, children=children)


Literal = namedtuple("Literal", ("version", "value"))
Operator = namedtuple("Operator", ("version", "type", "children"))

init = get_input(16).strip()

input_string = "".join(bin(x)[2:].zfill(4) for x in list(map(lambda char: int(char, 16), init)))
it = iter(bool(int(x)) for x in input_string)

final_log = parse_packet(it)

def eval_packet(packet):
    if isinstance(packet, Literal):
        return packet.value
    elif packet.type == 0:
        return sum(map(eval_packet, packet.children))
    elif packet.type == 1:
        return prod(map(eval_packet,packet.children))
    elif packet.type == 2:
        return min(map(eval_packet,packet.children))
    elif packet.type == 3:
        return max(map(eval_packet, packet.children))
    elif packet.type == 5:
        return int(eval_packet(packet.children[0]) > eval_packet(packet.children[1]))
    elif packet.type == 6:
        return int(eval_packet(packet.children[0]) < eval_packet(packet.children[1]))
    elif packet.type == 7:
        return int(eval_packet(packet.children[0]) == eval_packet(packet.children[1]))


print(eval_packet(final_log))