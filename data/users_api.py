import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/city/<int:user_id>', methods=['GET'])
def get_city(user_id):

    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': user_id})
    return jsonify(
        {
            'city': user.city,
            'name': f'{user.name} {user.surname}'

        }
    )
