import codeforces_problem_wrapper
import codeforces_contest_wrapper


PROBLEM_LINK = 'https://codeforces.com/problemset/problem/'
CONTEST_LINK = 'https://codeforces.com/contest/'


app = flask.Flask(__name__)

@app.route("/",methods=['GET'])
def contest_data():
    contest_id = flask.request.args['id']
    return flask.jsonify( codeforces_contest_wrapper.parse_contest(PROBLEM_LINK + contest_id))
