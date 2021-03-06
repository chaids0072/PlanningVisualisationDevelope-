import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/parser')
import unittest
import plan_generator as step1
import problem_parser as step2
import domain_parser as dom_par
import re


class test_integration_step12(unittest.TestCase):
    # Test if the problem file is not empty, when step1 has been executed
    def test_integration_input_domain_step_12(self):
        step1.get_plan("../../input/domain_blocks.pddl", "../../input/bw08.pddl")
        with open("../../input/bw08.pddl", "r") as f1:
            problemTest = f1.read()
            self.assertTrue(problemTest)

    # Test if the result contains init state, when step1 has been executed
    def test_integration_init_stage_step_12(self):
        step1.get_plan("../../input/domain_blocks.pddl", "../../input/bw08.pddl")
        predicates_list = dom_par.get_domain_json("../../input/domain_blocks.pddl")
        problem_json = step2.get_problem_json("../../input/bw08.pddl",predicates_list)
        text = ''.join(str(e) for e in problem_json)
        st = text[text.index("init") + len("init"):]
        self.assertTrue(problem_json)

    # Test if the result contains goal state, when step1 has been executed
    def test_integration_goal_stage_step_12(self):
        step1.get_plan("../../input/domain_blocks.pddl", "../../input/bw08.pddl")
        predicates_list = dom_par.get_domain_json("../../input/domain_blocks.pddl")
        problem_json = step2.get_problem_json("../../input/bw08.pddl",predicates_list)
        text = ''.join(str(e) for e in problem_json)
        st = text[text.index("goal") + len("goal"):]
        self.assertTrue(st)

    # Test if the result contains predicate - clear , when step1 has been executed
    def test_integration_init_stage_content_step_12_t1(self):
        step1.get_plan("../../input/domain_blocks.pddl", "../../input/bw08.pddl")
        predicates_list = dom_par.get_domain_json("../../input/domain_blocks.pddl")
        problem_json = step2.get_problem_json("../../input/bw08.pddl",predicates_list)
        pattern = re.compile(r'\w\s\w')
        result = pattern.findall(str(problem_json))
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
