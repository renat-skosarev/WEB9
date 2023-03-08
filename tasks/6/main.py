from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    db_sess = create_session()

    for user in db_sess.query(User).filter(User.address == 'module_1', User.position.notlike('%engineer%'),
                                           User.speciality.notlike('%engineer%')):
        print(user.id)


if __name__ == '__main__':
    main()
