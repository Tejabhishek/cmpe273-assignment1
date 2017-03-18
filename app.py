from flask import Flask
import sys
from flask import Flask
from github import Github
from flask import json
import yaml

app = Flask(__name__)

@app.route('/v1/<filename>')
def config(filename):
    path = sys.argv[1].split("/")
    g = Github()
    repo = g.get_user(path[3]).get_repo(path[4])
    fileObj = repo.get_contents(filename)
    ext = filename.split(".")
    if (ext[1] == "yml" ):
        cnt = (fileObj.content.decode('base64'))
        return yaml.dump(cnt)
    if (ext[1] == "json"):
        cnt = (fileObj.content.decode('base64'))
        return json.dumps(cnt)

if __name__=="__main__":
    app.run(debug= True,host='0.0.0.0')
