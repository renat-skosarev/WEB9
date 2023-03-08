from flask import Flask

app = Flask(__name__)


def main():
    global_init(input())
    db_sess = create_session()

    for user in db_sess.query(User).filter(User.age < 18):
        print(str(user) + f' {user.age} years')


if __name__ == '__main__':
    main()
