import unittest
import server.PddLparser.visualiserFile.PredicateParser.plan_generator as step1
import server.PddLparser.visualiserFile.PredicateParser.problem_parser as step2
import server.PddLparser.visualiserFile.PredicateParser.predicates_generator as step3
import server.PddLparser.visualiserFile.PredicateParser.domain_parser as dom_par

class MyTestCase(unittest.TestCase):
    # Test remove_unused_char
    def test_remove_unused_char(self):
        input = [{"action": "abc effect:bca"}]
        output = step1.remove_unused_char(input)
        result = True
        if "effect" in output:
            result = False
        self.assertTrue(result)

    #  Test get_stages to see if it can generate an output
    def test_get_stages(self):
        domain_file = "../../input/domain_grid.pddl"
        problem_file = "../../input/gw01.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_grid.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        self.assertTrue(stages)

    #  Test get_stages to see if it can generate an output correctly
    def test_get_stages(self):
        # the amount of stages generated
        domain_file = "../../input/domain_grid.pddl"
        problem_file = "../../input/gw01.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_grid.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file, predicates_list)
        result = len(stages["stages"]) - 1 # minus initial stage

        # the amount of stages expected
        expect = plan['result']['length']
        self.assertTrue(result is expect)

if __name__ == '__main__':
    unittest.main()
