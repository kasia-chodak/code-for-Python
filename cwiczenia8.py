# https://github.com/krzysztofmakuch/pythonProgramming/projects/8
import datetime
import sys


def christmas_tree(levels):
    widest = (levels-1)*2 + 1
    tree = ''
    for level in range(0, levels):
        stars = '*' * (level * 2 + 1)
        if len(stars) != widest:
            spaces_len = int((widest - len(stars))/2)
            tree += ' ' * spaces_len + stars + ' ' * spaces_len + '\n'
        else:
            tree += stars + '\n'
    tree += ' ' * int((widest - 3)/2) + '|_|' + ' ' * int((widest - 3)/2) + '\n'
    return tree


def christmas_card(levels, file_out):
    year = datetime.datetime.now().year
    with open(file_out, 'w') as card_file:
        card_file.write(christmas_tree(levels))
        card_file.write('Merry Christmas ')
        card_file.write(str(year))
        card_file.write('!')


# py cwiczenia8.py 11 'card.txt'
# christmas_card(int(sys.argv[1]), sys.argv[2])


class RNA():
    def __init__(self, id, species, sequence):
        self.id = id
        self.species = species
        self.sequence = sequence

    def complement(self):
        complementary = ''
        for base in self.sequence:
            if base == 'A':
                complementary += 'U'
            elif base == 'U':
                complementary += 'A'
            elif base == 'G':
                complementary += 'C'
            elif base == 'C':
                complementary += 'G'
        return complementary

    def length(self):
        return len(self.sequence)

    def __add__(self, other):
        new_RNA = RNA(str(self.id)+'_'+str(other.id), self.species+', '+other.species, self.sequence+other.sequence)
        return new_RNA

    def __str__(self):
        return f'I\'m a {self.__class__.__name__} molecule.'

    def __repr__(self):
        return f'I\'m a {self.species}\'s {self.__class__.__name__} molecule,\nmy id is {self.id}, ' \
               f'and my sequence is as follows:\n{self.sequence}'


class DNA(RNA):
    def __init__(self, id, species, sequence):
        RNA.__init__(self, id, species, sequence)
        self.sequence = self.sequence.replace('U', 'T')

    def complement(self):
        complementary = ''
        for base in self.sequence:
            if base == 'A':
                complementary += 'T'
            elif base == 'T':
                complementary += 'A'
            elif base == 'G':
                complementary += 'C'
            elif base == 'C':
                complementary += 'G'
        return complementary

