# dota_teams = ["Liquid", "Virtus.pro", "PSG.LGD", "Team Secret"] 
# data = [[1, 2, 1, 'x'],
#   ['x', 1, 1, 'x'],
#   [1, 'x', 0, 1],
#   [2, 0, 2, 1]] 
# format_row = "{:>12}" * (len(dota_teams) + 1)
# print(format_row.format("", *dota_teams))
# for team, row in zip(dota_teams, data):
# print(format_row.format(team, *row))

def print_table(headers, matrix):
    column_lengths = [len(name) + 5 for name in headers]
    for row in matrix:
        for i, val in enumerate(row):
            column_lengths[i] = max(column_lengths[i], len(str(val)) + 5)
        
    format_row = ''.join([f'{{:<{length}}}' for length in column_lengths])
    print(format_row.format(*headers))
    for row in matrix:
        print(format_row.format(*row))


def print_markdown_table(headers, matrix):
    print('|' + '|'.join(headers) + '|')
    print('| -- ' * len(headers) + '|')
    for row in matrix:
        print('|' + '|'.join(str(val) for val in row) +'|')