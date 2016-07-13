import argparse
from model.model import db

if __name__ == '__main__':
    '''
    create and delete tables
    '''
    parser = argparse.ArgumentParser(description='operation on database.')
    parser.add_argument('-c', action='store_true', help='create table.')
    parser.add_argument('-d', action='store_true', help='drop table.')
    args = parser.parse_args()
    if args.c:
        db.create_all()
    elif args.d:
        db.drop_all()
