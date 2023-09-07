from api import api
from flask_restful import Resource
from flask import jsonify, request
from api.util.utc_time import get_current_utc_time, get_current_day


class Main(Resource):

    def get(self):
        slack_name = request.args.get("slack_name", type=str)
        track = request.args.get("track", type=str)

        if slack_name and track:
            json_data = {
                "slack_name": request.args.get("slack_name", type=str),
                "current_day": get_current_day(),
                "utc_time": get_current_utc_time(),
                "track": request.args.get("track", type=str),
                "github_file_url":
                    'https://github.com/timiwritescode/hngx_task_one/blob/main/app.py',
                "github_repo_url":
                    'https://github.com/timiwritescode/hngx_task_one',
                "status_code": 200
            }

            return jsonify(json_data)

        return {"status": "fail",
                "message": "incomplete parameters"}, 400

api.add_resource(Main, '/api')
