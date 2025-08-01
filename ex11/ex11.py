import itertools
import collections


class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root: Node):
        self.root = root

    def diagnose(self, symptoms):
        root = self.root
        while root.positive_child and root.negative_child:
            if root.data in symptoms:
                root = root.positive_child
            else:
                root = root.negative_child
        return root.data

    def calculate_success_rate(self, records):
        if not records:
            raise ValueError("recooooordds are empty!!!")
        counter = 0
        for record in records:
            record_illness = record.illness
            record_symptoms = record.symptoms
            illness = self.diagnose(record_symptoms)
            if illness == record_illness:
                counter += 1

        return counter / len(records)

    def all_illnesses(self):
        illnesses = self.all_illnesses_helper(self.root, {})
        d1 = sorted(illnesses.items(), key=lambda kv: kv[1], reverse=True)
        return [d1[i][0] for i in range(len(d1))]

    def all_illnesses_helper(self, root, illnesses):
        if root.positive_child is None and root.negative_child is None:
            if root.data:
                if root.data in illnesses:
                    illnesses[root.data] += 1
                else:
                    illnesses[root.data] = 1
            return illnesses
        self.all_illnesses_helper(root.positive_child, illnesses)
        self.all_illnesses_helper(root.negative_child, illnesses)
        return illnesses

    def paths_to_illness(self, illness):
        path = []
        root = self.root
        paths = []
        self.paths_to_illness_helper(root, illness, path, paths)
        return paths

    def paths_to_illness_helper(self, root, illness, path, paths):
        if illness is not None and root is not None and root.positive_child is None:
            if root.data == illness:
                paths.append(path)
            return
        if illness is None and root is None:
            paths.append(path)
            return
        self.paths_to_illness_helper(root.positive_child, illness, path + [True], paths)
        self.paths_to_illness_helper(root.negative_child, illness, path + [False], paths)

    def minimize(self, remove_empty=False):
        pass


def build_tree_helper(symptoms):
    if not symptoms:
        return Node(None)
    return Node(symptoms[0], build_tree_helper(symptoms[1:]), build_tree_helper(symptoms[1:]))


def check(record, true_lst, false_lst):
    for symptom in true_lst:
        if symptom not in record.symptoms:
            return False
    for symptom in false_lst:
        if symptom in record.symptoms:
            return False
    return True


def return_illness(records, true_lst, false_lst):
    lst = []
    for record in records:
        if check(record, true_lst, false_lst):
            lst.append(record)
    dct = {}
    for record in lst:
        if record.illness in dct:
            dct[record.illness] += 1
        else:
            dct[record.illness] = 1
    if not dct:
        return None
    value = max(dct, key=lambda x: dct[x])
    return value

    # if true_lst in record.symptoms and false_lst not in record.symptoms then save record.illness then return the max repeat illness


def add_illnesses(node, records, true_lst, false_lst):
    if node.positive_child is None:
        illness = return_illness(records, true_lst, false_lst)
        node.data = illness
        return
    add_illnesses(node.positive_child, records, true_lst + [node.data], false_lst)
    add_illnesses(node.negative_child, records, true_lst, false_lst + [node.data])


def build_tree(records, symptoms):
    for s in symptoms:
        if type(s) != str:
            raise TypeError("not striiiiing!!!!!")
    for r in records:
        if type(r) != Record:
            raise TypeError("nooooot record!!")
    if not records:
        root = build_tree_helper(symptoms)
        return Diagnoser(root)
    if not symptoms:
        dict = {}
        for s in records:
            if s.illness in dict:
                dict[s.illness] += 1
            else:
                dict[s.illness] = 1
        d1 = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
        if d1:
            return Diagnoser(Node((d1[0][0])))
        else:
            return Diagnoser(Node(None))
    root = build_tree_helper(symptoms)
    add_illnesses(root, records, [], [])
    return Diagnoser(root)


def optimal_tree(records, symptoms, depth):
    if depth < 0 or depth > len(symptoms):
        raise ValueError("the length inValid!!")
    d = dict()
    for s in itertools.combinations(symptoms, depth):
        diagnoser = build_tree(records, s)
        success = diagnoser.calculate_success_rate(records)
        d[diagnoser] = success
    d1 = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    return d1[0][0]


if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # covid-19   cold

    flu_leaf = Node("covid-19", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)
    print(diagnoser.paths_to_illness(None))
    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

# Add more tests for sections 2-7 here.
