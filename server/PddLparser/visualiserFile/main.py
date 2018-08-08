"""This module intergrate all the other module, it takes the domain PDDL, problem PDDL, and 
animation profile, and it write the visualisation file to visualsation.json.
"""
import sys
sys.path.append('../visualiserFile/parser')
from server.PddLparser.visualiserFile.parser import plan_generator  # Step1: get plan from planning domain api
from server.PddLparser.visualiserFile.parser import problem_parser  # Step2: parse problem pddl, to get the inital and goal stage
from server.PddLparser.visualiserFile.parser import predicates_generator  # Step3: manipulate the predicate for each step/stage
from server.PddLparser.visualiserFile.generator import visualisation_generator  # Step4. use the animation profile and stages from step3 to get the visualisation file
from server.PddLparser.visualiserFile.parser import domain_parser  # Step3: extract all the available predicates from problem.pddl
import json

def get_visualisation_file():
    # # This function will call the other modules to generate the visualisaiton file.
    # if len(sys.argv) < 4:
    # 	print("some file is missing, please follow the command below to run the program")
    # 	print("python main.py [dommainfile] [problemfile] [animationprofile]")
    # 	sys.exit()

    domain_file = sys.argv[1]
    problem_file = sys.argv[2]
    animation_file = sys.argv[3]

    # read animation profile from json
    file = open(animation_file)
    content = file.read()
    animation_profile = json.loads(content)

    plan = plan_generator.get_plan(domain_file, problem_file)
    predicates_list = domain_parser.get_domain_json(domain_file)
    problem_json = problem_parser.get_problem_json(problem_file, predicates_list)
    stages = predicates_generator.get_stages(plan, problem_json, problem_file, predicates_list)
    # A file called visualistaion.json will be generated in the folder if successful
    visualisation_generator.get_visualisation_json(stages, animation_profile)

if __name__ == "__main__":
    get_visualisation_file()
