from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import dateutil.parser
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/upload/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html');
    #return "<h1>HELLO!</h1>";

#new endpoint
@app.route('/upload',methods=['GET','POST'])
def index2():
    #print(json.loads(request.json) );
    #print(json.loads(request.json["body"])["timeZone"] );
    result = json.loads(request.json["body"]);
    #for item in result["items"]:
    #    print(item);
    #for key,value in dictionary.items():

    #f = open("test.txt","w");
    #f.write("hello world");
    #f.close();

    events = []

    for item in result["items"]:
        start = item["start"]
        end = item["end"]
        if "date" in start:
            start_dt = start["date"]
            setMidnight = dateutil.parser.parse(start_dt)
            end_dt = end["date"]
            alsoSetMidnight = dateutil.parser.parse(end_dt)

        else:
            start_dt = start["dateTime"]
            setMidnight = dateutil.parser.parse(start_dt)
            end_dt = end["dateTime"]
            alsoSetMidnight = dateutil.parser.parse(end_dt)

        events.append((result["summary"], setMidnight.day, (setMidnight.hour * 100 + setMidnight.minute), (alsoSetMidnight.hour * 100 + alsoSetMidnight.minute)))
        # events.append([result["summary"], setMidnight, alsoSetMidnight])
        with open('data.json', 'w') as outfile:
            json.dump(events, outfile)

    # with open('data.json', 'w') as outfile:
    #     json.dump(result, outfile)
    #
    # with open('data.json', 'r') as infile:
    #     fileResult = json.load(infile)
    #
    # for item in fileResult["items"]:
    #     print(item["created"]);
    #
    return jsonify(request.json)

@app.route('/templates/<path:path>')
def send_files(path):
    return send_from_directory('templates', path)

if __name__ == "__main__":
    app.run(debug=True,port=8000);
