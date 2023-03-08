from flask import Flask

app = Flask(__name__)


def main():
    global_init(input())
    db_sess = create_session()

    for user in db_sess.query(User).filter((User.position.like('%chief%')) | (User.position.like('%middle%'))):
        print(user, user.position)


if __name__ == '__main__':
    main()
