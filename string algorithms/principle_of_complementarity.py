"""
This file is containing translate from dnk to rnk algorithm.
This algorithm is working with time O(n).
"""


def comp(st: str) -> str:
    """
    This function is realizing algorithm that translate dnk string to rnk.
    This algorithm is working with time O(n).
    And input param recommended to use str python type
    but if you want you can use list[str]
    :param st: dnk string/list[str] input.
    :return: rnk string
    """

    # check input value
    if type(st) != list[str] and type(st) != str:
        # throw exception if not str ot list
        raise ValueError('input string is not str or list[str]')

    # initialize string that will be contain answer
    ans = ''

    for i in range(len(st)):
        # check all the complementarity permutations
        # and add new value into answer string
        if st[i] == 'А':
            ans += 'У'
        elif st[i] == 'Т':
            ans += 'А'
        elif st[i] == 'Г':
            ans += 'Ц'
        elif st[i] == 'Ц':
            ans += 'Г'

    # and return answer
    return ans