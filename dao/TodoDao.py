from orm.OrmEntity import db,TodoTable

class TodoDao:
	# get TODOs
	def getTodos(userId):
		todos = TodoTable.query.filter_by(userId = userId).all()
		for item in todos:
			print(item.text)
			# return True

	# add TODOs
	def addTodo(userId, status, text):
		todo = TodoTable(userId = userId, status = status, text = text)
		db.session.add(todo)
		db.session.commit()
		return todo.todoId

	# update TODOs
	def updateTodo(todoId, status):
		todos = TodoTable.query.filter_by(todoId = todoId).update({'status': status})
		db.session.add(todos)
		db.session.commit()
		return True

	# delete Todos
	def deleteTodo(todoId):
		result = TodoTable.query.filter_by(todoId = todoId).first()
		if result:
			db.session.delete(result)
			db.session.commit()
			return True