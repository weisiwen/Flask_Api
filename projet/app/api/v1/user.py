from app.libs.redprint import Redprint

api = Redprint('user')

@api.route('/get')
def get_book():
    return 'I am Simon'

