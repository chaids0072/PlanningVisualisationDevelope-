import unittest
import server.PddLparser.visualiserFile.parser.plan_generator as step1
import server.PddLparser.visualiserFile.parser.problem_parser as step2
import server.PddLparser.visualiserFile.parser.predicates_generator as step3
import server.PddLparser.visualiserFile.parser.domain_parser as dom_par

class MyTestCase(unittest.TestCase):
    #  Test get_problem_json to see if it can generate an output correctly
    def test_get_problem_json(self):
        # the amount of stages generated
        domain_file = "../../input/domain_grid.pddl"
        problem_file = "../../input/gw01.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_grid.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)

        self.assertTrue(problem_json)


if __name__ == '__main__':
    unittest.main()
