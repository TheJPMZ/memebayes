import re


def check_probability(prob) -> bool:
    if not 0.0 < prob < 1:
        raise ValueError("Probability should be a float between 0.0 and 1.0")
    return True


def check_parents(nodes, parents) -> bool:
    if parents and not all(node in nodes for node in parents):
        raise ValueError(f"All parents should already be nodes. '{[x for x in parents if x not in nodes]}'")
    return True


class BayesNode:
    def __init__(self, name: str, parents: list = None, pt: dict = None) -> None:
        self.prob_table = {}
        self.name = name
        self.parents = parents or []

        if pt:
            self.set_prob_table(pt)

    def set_parents(self, new_parents) -> None:
        self.parents = new_parents

    def set_prob_table(self, table) -> None:

        regex = "^-?[A-Za-z-](\|[A-Za-z-]+)?$"

        for x in table:
            if not bool(re.match(regex, x)):
                print(f"{x} doesn't match the correct format. Correct: (A|BC)")
                return None

        for x in table.values():
            if not isinstance(x, float):
                print(f"Values need to be float. {x} isn't a float.")
                return None

        self.prob_table = table.copy()

        for x in table.items():
            inverse = {x[0][1:]: 1 - x[1]} if x[0] == "-" else {"-" + x[0]: 1 - x[1]}
            self.prob_table.update(inverse)

    def update_prob_table(self, addition) -> None:
        self.prob_table.update(addition)

    def check_node(self) -> bool:
        ind = len(self.parents)

        if not len(self.prob_table) == (2 ** ind) * 2:
            return False

        for x in self.prob_table.values():
            check_probability(x)

        if not self.name:
            return False

        return True

    def get_factors(self) -> dict:
        return self.prob_table

    def prob(self) -> float:
        return self.prob_table[self.name]

    def __eq__(self, name) -> bool:
        return self.name == name

    def __str__(self) -> str:
        return f"P({self.name}|{''.join([str(elem) for elem in self.parents])})".replace("|)", ")")

    def __repr__(self) -> str:
        return "(Node {})".format(self.name)


class BayesNetwork:
    def __init__(self, nodes: list) -> None:
        self.nodes = [BayesNode(node) for node in nodes]

    def add_node(self, name: str, parents: list = None, pt: dict = None) -> None:

        if name in self.nodes:
            print("Node already in network")
            return None

        check_parents(parents)

        self.nodes.append(BayesNode(name, parents, pt))

    def edit_node(self, node_name: str, parents: list = None, pt: dict = None) -> None:

        if node_name not in self.nodes:
            print("Node not in network, to add a node use `add_node()`")
            return None

        node = [item for item in self.nodes if item == node_name][0]

        if pt:
            node.set_prob_table(pt)

        if parents:
            check_parents(self.nodes, parents)
            node.set_parents(parents)

    def compact(self) -> str:
        order = []
        copy_nodes = self.nodes.copy()
        for x in self.nodes:
            if not x.parents:
                order.append(x)
                copy_nodes.remove(x)

        while copy_nodes:
            for x in copy_nodes:
                if all(parent in order for parent in x.parents):
                    order.append(x)
                    copy_nodes.remove(x)

        return "".join([str(x) for x in order])

    def defined(self) -> bool:
        for node in self.nodes:
            if not node.check_node():
                return False
        return True

    def show_factors(self):
        for node in self.nodes:
            print(node.name, ":", node.get_factors())
    
    def get_node(self, node_name: str):
        return [item for item in self.nodes if item == node_name][0]

    def query(self, p_query: str):
        division = re.split("\|", p_query)
        variable, evidence = division
        variable = [x for x in variable]
        evidence = [x for x in evidence]

        a = self.enumerate_ask(evidence, [])
        b = self.enumerate_ask(variable, evidence)
        return b/a


        return





    def enumerate_ask(self, variables, evidence):
        ex = variables + evidence
        new_list = []
        count = 0
        while len(self.nodes) > count:
            for node in self.nodes:
                if node in new_list:
                    break
                if len(node.parents) == 0:
                    new_list.append(node)
                    count += 1
                else:
                    test = False
                    for parent in node.parents:
                        if parent not in new_list:
                            break
                        test = True
                    if test:
                        new_list.append(node)
                        count += 1

        return self.enumerate_all(new_list, ex)




    def enumerate_all(self, variables: list[BayesNode], evidence: list[str]):
        if not variables:
            return 1

        y: BayesNode = variables.pop(0)
        y_prob = y.name

        if y.parents:
            y_prob += f"|{''.join([str(elem) for elem in y.parents])}"

        if y.name in evidence:
            prob = y.prob()
            return prob * self.enumerate_all(variables, evidence)
        else:
            p1 = y.prob_table[y_prob]
            p2 = 1 - p1

            return p1 * self.enumerate_all(variables, [*evidence, y.name]) + p2 * self.enumerate_all(variables, [*evidence, f"-{y.name}"])












