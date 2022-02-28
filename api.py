from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from datetime import datetime
import json

app = Flask(__name__)
api = Api(app)

#parse and validate request arguments
requests_log_args = reqparse.RequestParser()
requests_log_args.add_argument('user_name', type=str, help='user_name is required', required=True)

#load post requests log file
f = open('post_requests_log.json', "r+")
logs = json.load(f)
f.close()

#method to return current time_of_day
def get_tod():
    now = datetime.now().time() # time object
    if now.hour >= 0 and now.hour < 12:
        return 'morning'
    elif now.hour >= 12 and now.hour < 18:
        return 'afternoon'
    elif now.hour >= 18:
        return 'night', 200

class Visit(Resource):
    def get(self):
        return logs['post_requests_log'], 200
    
    def post(self):
        #initial post request log with client ip
        request_log = {'ip' : request.remote_addr,}

        #add sended arguments in the request: user_name
        args = requests_log_args.parse_args()
        request_log.update(args)

        #add time_of_day argument
        request_log.update({"time_of_day" : get_tod()})

        #save log to memory file
        logs['post_requests_log'].append(request_log)
        with open("post_requests_log.json", "w") as outfile:
            json.dump(logs, outfile)

        return request_log, 200

api.add_resource(Visit, '/visit')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')










