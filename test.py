import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

tasks =[
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done": False,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": False,
      "id": 2,
      "title": "Learn Python"
    },
    {
      "description": "",
      "done": False,
      "id": 3,
      "title": "Read a book"
    }]
	
@app.route('/todo/api/v1.0/task',methods=['GET'])
def get_all():
	return jsonify({"tasks" : tasks})
	
	
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [taskz for taskz in tasks if taskz['id'] == task_id]
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
	
@app.route('/todo/api/v1.0/task',methods=['POST'])
def new_entry():
	new = {"description": request.json["description"], "id": request.json["id"], "title": request.json["title"]}
	tasks.append(new)
	return jsonify({"tasks":tasks})
	
	
# @app.route('/todo/api/v1.0/task/<string:name>',methods=['DELETE'])
# def delete_one(name):
	# deleted = [x for x in tasks if x["title"] == name]
	# tasks.remove(deleted[0])
	# return jsonify({"tasks":tasks})
	
@app.route('/todo/api/v1.0/task',methods=['DELETE'])
def delete_one():
	for task in tasks:
		d = -1
		if task["id"] == int(request.json["id"]):
			d = tasks.index(task) +1       
	if d:
		tasks.remove(tasks[d-1])
		return jsonify({"tasks":tasks})
	else:
		return "Error: No id field provided. Please specify an id."
	
	
	
app.run()


# import flask
# from flask import request, jsonify
# import sqlite3 #,string


# app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1>
# <p>A prototype API for distant reading of science fiction novels.</p>'''


# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     conn = sqlite3.connect('books.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()
#     all_books = cur.execute('SELECT * FROM books;').fetchall()

#     return jsonify(all_books)


# @app.errorhandler(404)
# def page_not_found(e):
#     return "<h1>404</h1><p>The resource could not be found.</p>", 404


# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_filter():
#     query_parameters = request.args

#     id = query_parameters.get('id')
#     published = query_parameters.get('published')
#     author = query_parameters.get('author')

#     query = "SELECT * FROM books WHERE"
#     to_filter = []

#     if published:
#         query += ' published=? AND'
#         to_filter.append(published)
#     if author:
#         query += ' author=? AND'
#         to_filter.append(author)
#     if not (id or published or author):
#         return page_not_found(404)

#     query = query[:-4] + ';'
#     conn = sqlite3.connect('books.db')
#     results = []

#     cursor = conn.execute("SELECT ID, TITLE, AUTHOR, PUBLISHED, FIRST_SENTENCE from books")
#     for row in cursor:
#         if str(published) == str(row[3]) and str(author) == str(row[2]):
#             results.append(row[1])

#     return jsonify(results)
    
# @app.route('/api/v1/resources/books', methods=['PUT'])
# def update_base():
#     query_parameters = request.args

#     id = query_parameters.get('id')
#     published = query_parameters.get('published')
#     author = query_parameters.get('author')

#     query = "SELECT * FROM books WHERE"
#     to_filter = []

#     if published:
#         query += ' published=? AND'
#         to_filter.append(published)
#     if author:
#         query += ' author=? AND'
#         to_filter.append(author)
#     if not (id or published or author):
#         return page_not_found(404)

#     query = query[:-4] + ';'
#     conn = sqlite3.connect('books.db')
#     results = []
#     results_list = []

#     cursor = conn.execute("SELECT ID, TITLE, AUTHOR, PUBLISHED, FIRST_SENTENCE from books")
#     for row in cursor:
#         if str(published) == str(row[3]) and str(author) == str(row[2]):
#             results.append(row[4])
#             results_list.append(request.json.get('title'))
#             conn.execute("UPDATE books set TITLE =?  where (PUBLISHED = ? and AUTHOR = ?)", (request.json.get('title'), row[3], row[2]))
#             conn.commit()

#     return jsonify(results_list)


# app.run()
            
            










