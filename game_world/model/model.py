from app import db

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Date,
    Float
)


def to_dict(self):
    ins_dict = {}
    for attr, value in self.__dict__.items():
        if not attr.startswith('_'):
            ins_dict[attr] = value
    return ins_dict


db.Model.to_dict = to_dict


def init_db():
    db.create_all()


def flush():
    db.session.commit()


class GamerTester(db.Model):
    __tablename__ = 'gamer_tester'

    id = db.Column('id', Integer, primary_key=True)
    name = db.Column('username', String(30), unique=True)
    email = db.Column('email', String(50), unique=True)
    password = db.Column('password', String(100), unique=False)

    @classmethod
    def flush_fake_GT(cls, num=1):
        from faker import Factory
        fake = Factory.create()
        import pdb; pdb.set_trace()
        stuff = [
            "name",
            "email",
            "password",
        ]

        for i in xrange(num):
            stuff_dict = {}
            for item in stuff:
                stuff_dict.update(
                    {item: getattr(fake, item)()}
                )
            me = cls(**stuff_dict)
            db.session.add(me)

        flush()
