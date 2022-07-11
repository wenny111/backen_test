from flask import Blueprint, request, Response
import json

from service.UserService import UserService
from entity.UserEntity import LoginRequest, SignUpRequest

router = Blueprint('router',__name__) 

userService = UserService()

@router.route("/", methods = ['GET'])
def test():
    return "<p>笑然 猪猪!</p>"

@router.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    login = LoginRequest(data)
    user = userService.userLogin(login)
    res = Response()
    res.data = json.dumps(user) # dict to json
    return res

@router.route('/signup', methods=['POST'])
def signup():
    # Encode Data Entity
    data = request.get_json()

    # convert json to request entity
    signup = SignUpRequest(data)

    # Process service logic
    userId = userService.userSignUp(signup)

    # Encode response
    res = Response()
    res.data = str(userId)
    return res