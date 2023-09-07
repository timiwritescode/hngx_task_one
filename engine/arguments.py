from flask_restful import reqparse

# get requests argument for the main resource class
main_get_arguments = reqparse.RequestParser() 
main_get_arguments.add_argument("slack_name", type=str, help="Slack name required",required=True)
main_get_arguments.add_argument("track", type=str, help='track required', required=True)