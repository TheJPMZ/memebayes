import re


def query(p_query):
    division = re.split("\|", p_query)
    focus = division[0]
    dado = division[1] if len(division) == 2 else None


if __name__ == '__main__':
    query("A")

if __name__ == '__main__':
    query("A")
    query("-A")
    query("A|B")
    query("A|BC")
    query("A|-BC")
    query("A|B-C")
    query("A|-B-C")
