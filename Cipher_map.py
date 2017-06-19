# -*- coding: utf-8 -*-
import copy


def make_array(atuple):

    arr = []
    for str in atuple:
        li = []
        for s in str:
            li.append(s)
        arr.append(li)
    return arr


# def turn90_passwd(cip_passwd): 应该改变的是X对应的坐标，不是ciphered_password

#     size = len(cip_passwd)
#     copy_passwd = copy.deepcopy(cip_passwd)
#     for r in range(size):
#         for c in range(size):
#             cip_passwd[r][c] = copy_passwd[size - 1 - c][r]
#     return cip_passwd


def get_coords(cipher_grille):
    coords = []
    size = len(cipher_grille)
    for r in range(size):
        for c in range(size):
            if cipher_grille[r][c] == 'X':
                coords.append([r, c])
    return coords


def turn90_coords(coords):

    new_coords = []
    size = len(coords)
    for co in coords:
        # 坐标转换 [r, c] --> [c, size-1-r, ]
        l = [co[1], (size-1-co[0])]
        new_coords.append(l)
    return sorted(new_coords)


def get_passwd(cip_passwd, coords, turn90_time):

    passwd = ''.join(cip_passwd[co[0]][co[1]] for co in coords)
    for i in range(turn90_time):
        coords = turn90_coords(coords)
        for co in coords:
            passwd += cip_passwd[co[0]][co[1]]
    return passwd


def recall_password(cipher_grille, ciphered_password):
    cip_grille = make_array(cipher_grille)
    cip_passwd = make_array(ciphered_password)
    coords = get_coords(cip_grille)
    time = len(cip_grille) - 1
    return get_passwd(cip_passwd, coords, time)

if __name__ == '__main__':

    assert make_array(('X...',
                       '..X.',
                       'X..X',
                       '....')) == [['X', '.', '.', '.'],
                                    ['.', '.', 'X', '.'],
                                    ['X', '.', '.', 'X'],
                                    ['.', '.', '.', '.']]
    arr = [['X', '.', '.', '.'],
           ['.', '.', 'X', '.'],
           ['X', '.', '.', 'X'],
           ['.', '.', '.', '.']]

    assert make_array(('itdf',
                       'gdce',
                       'aton',
                       'qrdi')) == [['i', 't', 'd', 'f'],
                                    ['g', 'd', 'c', 'e'],
                                    ['a', 't', 'o', 'n'],
                                    ['q', 'r', 'd', 'i']]

    cip_passwd = make_array(('itdf',
                             'gdce',
                             'aton',
                             'qrdi'))

    assert get_coords(arr) == [[0, 0], [1, 2], [2, 0], [2, 3]]

    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
