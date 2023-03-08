import datetime

import sqlalchemy
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    db_sess.add(get_captain())
    db_sess.add(get_job())

    db_sess.commit()


def get_captain() -> User:
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    return user


def get_job() -> Jobs:
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2;3'
    job.start_date = datetime.datetime.now().date()
    job.is_finished = False
    return job


if __name__ == '__main__':
    main()
