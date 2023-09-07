from engine import api
from flask_restful import Resource
from flask import jsonify
from engine.arguments import main_get_arguments
from engine.util.utc_time import get_current_utc_time, get_current_day


# each key of the json data are entered into 

class Main(Resource):

    def get(self):
        req_args = main_get_arguments.parse_args()

        json_data = {
            "slack_name": req_args['slack_name'],
            "current_day": get_current_day(),
            "utc_time": get_current_utc_time(),
            "track": req_args["track"],
            "github_file_url":
                'https://github.com/timiwritescode/hngx_task_one/blob/main/app.py',
            "github_repo_url": 
                'https://github.com/timiwritescode/hngx_task_one',
            "status_code": 200
        }
        
        return jsonify(json_data)
    
api.add_resource(Main, '/api')    