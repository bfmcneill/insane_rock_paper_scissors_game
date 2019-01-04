import csv
from collections import defaultdict


class Roll:

    def __init__(self):
        self.reader_data, self.reader_fields = self.load_roll_data()
        self.rolls = self.calculate_rolls()
        self.truth_table = self.calculate_truths()

    def load_roll_data(self):
        with open('battle-table.csv') as fin:
            reader = csv.DictReader(fin)
            return list(reader), reader.fieldnames

    def calculate_rolls(self):
        _rolls = self.reader_fields
        _rolls.pop(0)
        keys = list(range(1, len(_rolls) + 1))
        return dict(zip(keys, _rolls))

    def print_attack_options(self):
        for k, v in self.rolls.items():
            msg = f"[{k}] {v}"
            print(msg)

    def calculate_truths(self):
        lst = list(self.reader_data)
        truth = defaultdict(dict)
        for d in lst:
            v = {
                key: value.upper()
                for key, value in d.items() - {'Attacker', }
            }
            truth[d['Attacker']] = v
        return truth
