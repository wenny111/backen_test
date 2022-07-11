from orm.OrmEntity import db,Usertable

class UserDao:
	# register: save user data and return userId
	def addUser(username, passwd):
		user = Usertable(username = username, passwd = passwd)
		db.session.add(user)
		db.session.commit()
		return user.userId

	# login: get user data 
	def hasUser(username, passwd):
		user = Usertable.query.filter_by(username = username, passwd = passwd)
		for item in user:
			print(item.username)
		return user