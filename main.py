import flask
import codeforces_contest_wrapper

PROBLEM_LINK = 'https://codeforces.com/problemset/problem/'
CONTEST_LINK = 'https://codeforces.com/contest/'

app = flask.Flask(__name__)

@app.route("/",methods=['GET'])
def contest_data():
    contest_id = flask.request.args['id']
    return flask.jsonify( codeforces_contest_wrapper.parse_contest(CONTEST_LINK + contest_id))

if __name__ == '__main__':
    app.run()
