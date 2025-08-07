from flask_restful import Resource

import src.domain.problem as problem_services

service = problem_services.ProblemService()


class ProblemsResource(Resource):
    def post(self):
        return service.create_problem()


class FindResource(Resource):
    def post(self):
        return service.find_problems()


class FindByHashResource(Resource):
    def get(self):
        return service.find_by_hash()