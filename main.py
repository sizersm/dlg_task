import flask
from flask import jsonify

app = flask.Flask(__name__)


"""
I've kept this simple because this is a simple request, though a real Flask application merits an __init__ file
intialization and config file for environment variables, tests structured in their own directory, and I would 
favor class-based views if the app were expected to become more complicated, etc.
"""


def get_numbers_to_add():
    """
    Stand-In for external API service request
    """
    return list(range(10000001))


def get_total(list_elements_func = get_numbers_to_add):
    return sum(list_elements_func())


@app.route('/total', methods=['GET'])
def total_view():
    return jsonify(
        total=get_total()
    )


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)

