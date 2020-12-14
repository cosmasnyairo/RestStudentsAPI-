from flask import Flask, jsonify, request

from db import Database

app = Flask(__name__)


@app.route('/', methods=['GET'])
def fetch_all():
    database = Database()
    try:
        fetched_records = database.fetch_all()
        response = fetched_records
        return jsonify(response), 200
    except Exception as e:
        response = {'The following error occurred:': '{}'.format(e), }
        return jsonify(response), 500


@app.route('/fetch_records', methods=['GET'])
def fetch_records():
    database = Database()
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    required_fields = ['student_id']
    if not all(key in values for key in required_fields):
        response = {'message': 'Required data missing!'}
        return jsonify(response), 400

    try:
        fetched_records = database.fetch_records(int(values['student_id']))
        response = fetched_records.__dict__
        return jsonify(response), 200
    except Exception as e:
        response = {'The following error occurred:': '{}'.format(e), }
        return jsonify(response), 500


@app.route('/add_records', methods=['POST'])
def add_records():
    database = Database()
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400

    required_fields = ['student_name', 'email',
                       'phonenumber', 'student_address', 'entrypoints']
    if not all(key in values for key in required_fields):
        response = {'message': 'Some Required data missing!'}
        return jsonify(response), 400
    try:
        added_records = database.insert_records(
            values['student_name'], values['email'], values['phonenumber'], values['student_address'], values['entrypoints'],)
        response = {'Message': 'Successfully added record'}
        return jsonify(response), 200
    except Exception as e:
        response = {'The following error occurred:': '{}'.format(e), }
        return jsonify(response), 500


if __name__ == "__main__":
    app.run()
