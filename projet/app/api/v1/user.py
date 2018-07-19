from app.libs.redprint import Redprint

api = Redprint('user')

@api.route('',methods=['GET'])
def get_user():
    return 'I am Simon'

@api.route('',methods=['POST'])
def update_user():
    return 'update Simon'

@api.route('/create')
def create_user():
    pass


