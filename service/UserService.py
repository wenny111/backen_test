from dao.UserDao import UserDao
from entity.UserEntity import LoginRequest, SignUpRequest, UserEntity

class UserService:
	def __init__(self):
		print(self)
		self.userDao = UserDao()

	def userLogin(self, req: LoginRequest):
		user = UserEntity(req.username, req.passwd)
		return self.userDao.hasUser(user)

	def userSignUp(self, req: SignUpRequest):
		user = UserEntity(req.username, req.passwd)
		return self.userDao.addUser(user)
		
