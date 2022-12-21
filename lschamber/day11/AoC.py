from typing import Callable
from functools import reduce


class Monkey:
    def __init__(self, starting_items: list, operation: Callable[[int], int]):
        self._operation = operation
        self._items = starting_items
        self._nb_inspect = 0
        self._test_value = None
        self._true_send = None
        self._false_send = None

    def setup_monkey_redirect(self, test_value: int, true_send: 'Monkey', false_send: 'Monkey'):
        self._test_value = test_value
        self._true_send = true_send
        self._false_send = false_send

    def inspect_items(self):
        new_items = list()
        for item in self._items:
            self._nb_inspect += 1
            item = int(self._operation(item) / 3)
            new_items.append(item)
        self._items = new_items

    def inspect_items_2(self, PPCM: int):
        new_items = list()
        for item in self._items:
            self._nb_inspect += 1
            item = self._operation(item) % PPCM
            new_items.append(item)
        self._items = new_items

    def add_item(self, item):
        self._items.append(item)

    def send_items(self):
        while len(self._items) > 0:
            current_item = self._items.pop()
            if current_item % self._test_value == 0:
                self._true_send.add_item(current_item)
            else:
                self._false_send.add_item(current_item)

    def debug(self):
        print(self._items)
        print(self._nb_inspect)

    def nb_inspect(self):
        return self._nb_inspect

    def items(self):
        return self._items

    def test_value(self):
        return self._test_value


def perform_turn(monkeys: list[Monkey]):
    for monkey in monkeys:
        monkey.inspect_items()
        monkey.send_items()


def perform_turn_2(monkeys: list[Monkey], PPCM: int):
    for monkey in monkeys:
        monkey.inspect_items_2(PPCM)
        monkey.send_items()


def compute_part_1(monkeys: list[Monkey]):
    for _ in range(20):
        perform_turn(monkeys)

    values = sorted(map(lambda m: m.nb_inspect(), monkeys), reverse=True)[0:2]
    return values[0] * values[1]


def compute_part_2(monkeys: list[Monkey]):
    PPCM = reduce(lambda a, b: a * b, map(lambda m: m.test_value(), monkeys))
    for _ in range(10000):
        perform_turn_2(monkeys, PPCM)
    values = sorted(map(lambda m: m.nb_inspect(), monkeys), reverse=True)[0:2]
    return values[0] * values[1]


def test1():
    monkeys = test_monkeys()
    assert compute_part_1(monkeys) == 10605


def test2():
    monkeys = test_monkeys()
    assert compute_part_2(monkeys) == 2713310158


def part1():
    monkeys = input_monkeys()
    print(compute_part_1(monkeys))

def part2():
    monkeys = input_monkeys()
    print(compute_part_2(monkeys))


def main():
    # test1()
    # part1()
    # test2()
    part2()


def test_monkeys():
    monkey_0 = Monkey([79, 98], lambda x: x * 19)
    monkey_1 = Monkey([54, 65, 75, 74], lambda x: x + 6)
    monkey_2 = Monkey([79, 60, 97], lambda x: x * x)
    monkey_3 = Monkey([74], lambda x: x + 3)

    monkey_0.setup_monkey_redirect(23, monkey_2, monkey_3)
    monkey_1.setup_monkey_redirect(19, monkey_2, monkey_0)
    monkey_2.setup_monkey_redirect(13, monkey_1, monkey_3)
    monkey_3.setup_monkey_redirect(17, monkey_0, monkey_1)

    return [monkey_0, monkey_1, monkey_2, monkey_3]


def input_monkeys():
    monkey_0 = Monkey([63, 84, 80, 83, 84, 53, 88, 72], lambda x: x * 11)
    monkey_1 = Monkey([67, 56, 92, 88, 84], lambda x: x + 4)
    monkey_2 = Monkey([52], lambda x: x * x)
    monkey_3 = Monkey([59, 53, 60, 92, 69, 72], lambda x: x + 2)
    monkey_4 = Monkey([61, 52, 55, 61], lambda x: x + 3)
    monkey_5 = Monkey([79, 53], lambda x: x + 1)
    monkey_6 = Monkey([59, 86, 67, 95, 92, 77, 91], lambda x: x + 5)
    monkey_7 = Monkey([58, 83, 89], lambda x: x * 19)

    monkey_0.setup_monkey_redirect(13, monkey_4, monkey_7)
    monkey_1.setup_monkey_redirect(11, monkey_5, monkey_3)
    monkey_2.setup_monkey_redirect(2, monkey_3, monkey_1)
    monkey_3.setup_monkey_redirect(5, monkey_5, monkey_6)
    monkey_4.setup_monkey_redirect(7, monkey_7, monkey_2)
    monkey_5.setup_monkey_redirect(3, monkey_0, monkey_6)
    monkey_6.setup_monkey_redirect(19, monkey_4, monkey_0)
    monkey_7.setup_monkey_redirect(17, monkey_2, monkey_1)

    return [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]


if __name__ == '__main__':
    main()
