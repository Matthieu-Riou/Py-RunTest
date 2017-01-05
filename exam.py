#! /usr/bin/env python

def add_ints(a, b):
    ''' (int, int) -> int

    Return the sum of a and b.

    >>> add_ints(1, 1)
    2
    >>> add_ints(1, 3)
    4
    >>> add_ints(1, -6)
    -5
    '''
    return a + b



def f1(n):
    ''' (int) -> int

    Returns 4 times x square plus x plus 9.

    >>> f1(1)
    14
    >>> f1(2)
    27
    >>> f1(100)
    40109
    '''
    



def f2(x, y):
    ''' (float, float) -> float

    Returns x times y over the sum of x, y and 2.

    >>> "%.04f" % f2(1, 8.5)
    '0.7391'
    >>> "%.04f" % f2(9, 2.0)
    '1.3846'
    >>> "%.04f" % f2(1.0, 0)
    '0.0000'
    '''
    



def mul(l):
    ''' (list of int) -> int

    Return the product of every element in the list.

    >>> mul([2, 2])
    4
    >>> mul([1, 2, 2])
    4
    >>> mul([1, 2, 3])
    6
    >>> mul([1, 9, 6, 4, 2, 6, 1, 8, 9, 2])
    373248
    >>> mul([0, 9, 6, 4, 2, 6, 1, 8, 9])
    0
    '''
    return 4 #on purpose error to test partially failed example



def sum_evens(n):
    ''' (int) -> int

    Return the sum of every even number from 0 to n (inclusive).

    >>> sum_evens(4)
    6
    >>> sum_evens(5)
    6
    >>> sum_evens(6)
    12
    '''
    




def surround(c, s):
    ''' (str, str) -> str

    Returns s surrounded on both sides by c.

    >>> surround('+', 'test')
    '+test+'
    >>> surround('!', 'B')
    '!B!'
    '''
    



def center_in_field(c, s, w):
    ''' (str, str, int) -> str

    Returns s centered in a field of characters c with length w.
    If there's an odd number of characters in the field, add the extra character
    on the right.

    >>> center_in_field('.', 'lol', 5)
    '.lol.'
    >>> center_in_field('.', 'lol', 6)
    '.lol..'
    >>> center_in_field('+', 'lol', 7)
    '++lol++'
    >>> center_in_field(' ', 'lol', 8)
    '  lol   '
    '''
    



def comment_block(c, s, w):
    ''' (str, str, int) -> str

    >>> comment_block('#', 'test', 8)
    '########\\n# test #\\n########'
    >>> print comment_block('#', 'test', 10)
    ##########
    #  test  #
    ##########
    '''
    



def is_nucleotide(c):
    ''' (str) -> Boolean

    Return True if c in one of 'ATCG'

    >>> is_nucleotide('A')
    True
    >>> is_nucleotide('B')
    False
    >>> is_nucleotide('1')
    False
    >>> is_nucleotide('!')
    False
    >>> is_nucleotide('G')
    True
    >>> is_nucleotide('C')
    True
    >>> is_nucleotide('T')
    True
    '''
    



def is_valid_dna_sequence(s):
    ''' (str) -> Boolean
    Return True if s is a valid dna sequence (contains only nucleotides)

    >>> is_valid_dna_sequence('AT')
    True
    >>> is_valid_dna_sequence('ATF')
    False
    >>> is_valid_dna_sequence('TTATCCCG')
    True
    >>> is_valid_dna_sequence('TT1TCCCG')
    False
    '''
    



def get_complement(c):
    ''' (str) -> str

    Return the complement of nucleotide nuc.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    '''
    




def get_complement_sequence(s):
    ''' (str) -> str

    Return the complementary sequence of DNA sequence s.

    >>> get_complement_sequence('AT')
    'TA'
    >>> get_complement_sequence('TA')
    'AT'
    >>> get_complement_sequence('CCGCTAT')
    'GGCGATA'
    '''
    




def get_number_from_letter(c):
    ''' (str) -> int
    Return the number corresponding to letter c

    >>> get_number_from_letter('A')
    0
    >>> get_number_from_letter('B')
    1
    >>> get_number_from_letter('Z')
    25
    >>> get_number_from_letter('X')
    23
    '''
    



def get_letter_from_number(n):
    ''' (int) -> str

    >>> get_letter_from_number(0)
    'A'
    >>> get_letter_from_number(2)
    'C'
    >>> get_letter_from_number(24)
    'Y'
    >>> get_letter_from_number(25)
    'Z'
    '''
    



def shift_mod26(n, shift):
    ''' (int) -> int

    Return n shifted by "shift" in the [0-25] space

    >>> shift_mod26(0, 2)
    2
    >>> shift_mod26(25, 2)
    1
    >>> shift_mod26(1, 4)
    5
    >>> shift_mod26(1, 4050)
    21
    '''
    



def encrypt_char(c, shift):
    ''' (str) -> str

    Return an encrypted version of char "c" : it is shifted by "shift" places.

    >>> encrypt_char('A', 1)
    'B'
    >>> encrypt_char('A', 2)
    'C'
    >>> encrypt_char('Z', 2)
    'B'
    '''
    



def encrypt_string(s, shift):
    ''' (str) -> str

    >>> encrypt_string("TEST", 1)
    'UFTU'
    >>> encrypt_string("THIS IS A TEST", 1)
    'UIJT JT B UFTU'
    '''
    




