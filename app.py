from meteor_reasoner.utils.operate_dataset import return_dataset
from meteor_reasoner.materialization.materialize import materialize
from meteor_reasoner.utils.entail_check import entail
from meteor_reasoner.utils.loader import *
from meteor_reasoner.graphutil.temporal_dependency_graph import CycleFinder
from meteor_reasoner.canonical.utils import find_periods, fact_entailment
from meteor_reasoner.canonical.canonical_representation import CanonicalRepresentation
import time


def call_can(D, program, F):
    CR = CanonicalRepresentation(D, program)
    CR.initilization()
    D1, common, varrho_left, left_period, left_len, varrho_right, right_period, right_len = find_periods(CR)

    can_rep = []
    if varrho_left is not None:
        can_rep.append("left period: " + str(varrho_left))
        for key, values in left_period.items():
            for val in values:
                can_rep.append(str(key) + "@" + str(val))
    else:
        can_rep.append("left period: " + "[" + str(CR.base_interval.left_value - CR.w) + "," + str(CR.base_interval.left_value) + ")")
        can_rep.append("[]")

    if varrho_right is not None:
        can_rep.append("right period: " + str(varrho_right))
        for key, values in right_period.items():
            for val in values:
                can_rep.append(str(key) + "@" + str(val))
    else:
        can_rep.append("right period: "+ "(" + str(CR.base_interval.right_value) + "," + str(CR.base_interval.right_value + CR.w) + "]")
        can_rep.append("[]")

    return fact_entailment(D1, F, common, left_period, left_len, right_period, right_len), "<br/>".join(can_rep)


def is_bounded_intervals(program, dataset):
    # check the program
    for rule in program:
        head = rule.head
        for operator in head.operators:
            if operator.interval.right_value == Decimal("inf"):
                return False
        body = rule.body
        for literal in body:
            if isinstance(literal, BinaryLiteral):
                left_literal = literal.left_literal
                right_literal = literal.right_literal
                for operator in left_literal.operators:
                    if operator.interval.right_value == Decimal("inf"):
                        return False
                for operator in right_literal.operators:
                    if operator.interval.right_value == Decimal("inf"):
                        return False
            else:
                for operator in literal.operators:
                    if operator.interval.right_value == Decimal("inf"):
                        return False

    # check the dataset
    for predicate in dataset:
        for entity in dataset[predicate]:
            for interval in dataset[predicate][entity]:
                if interval.left_value  == Decimal("-inf") or interval.right_value == Decimal("inf"):
                    return False
    return True


def call_mat(D, program, F):
    while True:
        fixpoint = materialize(D, rules=program, K=1)
        if fixpoint:
            if entail(F, D):
                return True
            else:
                return False
        else:
            if entail(F, D):
                return True


def is_entail(raw_program, raw_data, fact):
    mat_template = "<b>Answer</b>: {}<br/> <b>Run time</b>: {}s<br/> <b></b> <b>Materialised facts:</b><br/> {}"
    can_template = "<b>Answer</b>: {}<br/> <b>Run time</b>: {}s<br/> <b></b> <b>Canonical Models:</b><br/> {}"
    if len(raw_data) > 1000:
        return "This is a demo website, please do not upload larger datasets!"
    D = load_dataset(raw_data)
    program = load_program(raw_program)
    fact = parse_str_fact(fact)
    F = Atom(fact[0], fact[1], fact[2])
    begin_time = time.time()
    try:
        CF = CycleFinder(program=program)
        if len(CF.loop) == 0:  # it is a non-recursive program
            while True:
                flag = materialize(D, rules=program)
                if entail(F, D):
                    return mat_template.format("Entailed", max(0.1, round(time.time() - begin_time, 2)), return_dataset(D))
                else:
                    if flag:
                        return mat_template.format("Not Entailed", max(0.1, round(time.time() - begin_time, 2)), return_dataset(D))
        cnt = 0
        D1 = copy.deepcopy(D)
        while cnt < 100:
            cnt += 1
            flag = materialize(D1, rules=program, K=1)
            if flag:
                if entail(F, D1):
                    return mat_template.format("Entailed", max(0.1, round(time.time() - begin_time, 2)), return_dataset(D1))
                else:
                    return mat_template.format("Not Entailed", max(0.1, round(time.time() - begin_time, 2)), return_dataset(D1))
            if entail(F, D1):
                return mat_template.format("Entailed", max(0.1, round(time.time() - begin_time, 2)), return_dataset(D1))

        # if bounded intervals call Canonical Interpretation
        if is_bounded_intervals(program, D):
                flag, can_rep = call_can(D, program, F)
                cost_time = round(time.time() - begin_time, 2)
                if flag:
                    return can_template.format("Entailed", max(0.1, cost_time), can_rep)
                else:
                    return can_template.format("Not Entailed", max(0.1, cost_time), can_rep)
        else:
            return "automata"
    except:
        return "Exceptions happen, please check whether the syntax of the dataset and the program is correct!"


if __name__ == "__main__":
    #dataset = ["Alive(adam)@0"]
    dataset = [
        "HighTemperature(sensor1) @ [0, 27.5]",
        "HighTemperature(sensor2) @ 3.5",
        "HighTemperature(sensor2) @ 5.1",
        "HighTemperature(sensor2) @ 10",
        "HighTemperature(sensor2) @ 14.7",
        "HighTemperature(sensor2) @ 20",
        "SameLocation(sensor1, sensor2) @ (-inf, +inf)"
    ]
    program = [
    "Overheat(X): - ALWAYS[-10, 0]HighTemperature(X)",
    "Overheat(X): - ALWAYS[-20, 0]SOMETIME[-5.5, 0]HighTemperature(X)",
    "Alert: - Overheat(X), Overheat(Y), SameLocation(X, Y)"]

    #program = ["ALWAYS[0,1] Alive(X) :-  Alive(X)", "Immortal(X) :- ALWAYS[0,+inf) Alive(X)"]
    dataset = ["A@[1,10]"]
    program = ["A:-SOMETIME[-1,0]A"]
    fact = "A@-1"
    #fact = "Alert@25"
    result = is_entail(program, dataset, fact)
    print(result)