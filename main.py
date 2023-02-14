import re
from bayes import BayesNetwork


def query(p_query):
    division = re.split("\|", p_query)
    focus = division[0]
    dado = division[1] if len(division) == 2 else None


if __name__ == '__main__':
    query("A")

if __name__ == '__main__':
    net = BayesNetwork(["A","J","T","M","R"])
    net.edit_node("R", pt = {"R": 0.001})
    net.edit_node("T", pt = {"T": 0.002})
    net.edit_node("A", parents = ["R", "T"], pt = {"A|RT": 0.95, "A|R-T": 0.94, "A|-RT": 0.29, "A|-R-T": 0.001})
    net.edit_node("J", parents = ["A"], pt = {"J|A": 0.9, "J|-A": 0.5})
    print(net.defined())
    net.edit_node("M", parents = ["A"], pt = {"M|A": 0.7, "M|-A": 0.01})

    print(net.compact())
    print(net.defined())
    print(net.show_factors())



