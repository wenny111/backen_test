from typing import Dict, List

class UserEntity:
	def __init__(self, username: str, passwd: str, userId: int = None):
		self.username = username
		self.passwd = passwd
		if(userId):
			self.userId = userId

# define login entity
class LoginRequest:
	def __init__(self, json: Dict):
		# print(json)
		# print(self)
		self.valid = True
		keys: List = ['username', 'passwd']

		# params check not equal 0
		for key in keys:
			val = json.get(key)
			if val:
				self.__dict__[key] = val
			else:
				return "lack params exception: {}".format(repr(self.value))

# define register entity
class SignUpRequest:
    def __init__(self, json: Dict):
        self.valid = True
        keys: List = ['username', 'passwd']
        
        # params check
        for key in keys:
            val = json.get(key)
            if val:
                self.__dict__[key] = val
            else:
                return "lack params exception: {}".format(repr(self.value))


