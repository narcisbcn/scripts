#!flask/bin/python
from flask import Flask, jsonify, request
import  subprocess

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/hi', methods=['GET'])
def get_hi():
    return "Hello!"


@app.route('/todo/api/v1.0/tasks/uptime', methods=['POST'])
def get_uptime():
  #file = request.form['file']
  cmd = ['uptime']
  p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE)

  out,err = p.communicate()
  return out


@app.route('/todo/api/v1.0/tasks/backup', methods=['POST'])
def get_():
  file = request.form['file']
  cmd = ['foo', 'fooparam']
  p1 = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE)

  f = open(file, 'wb')
  p2 = subprocess.Popen(['gzip'],
                     stdout=f,
                     stderr=subprocess.PIPE,
                     stdin=p1.stdout)

  out,err = p2.communicate()
  f.close()
  return "Done"


if __name__ == '__main__':
    app.run(debug=True)
