from peewee import *

db = SqliteDatabase('kent.db')
db.connect()

class UserRole(Model):
    name = CharField()
    description = CharField()
    class Meta:
        database = db 

class User(Model):
    name = CharField()
    studentId = CharField()
    userRoles = ForeignKeyField(UserRole, backref='users', null=True)
    class Meta:
        database = db 

def set_up_database():
    db.drop_tables([UserRole, User], safe=True)
    db.create_tables([UserRole, User])

def get_user_roles(id=None):
    if id==None:
        roles = UserRole.select()
    else:
        roles = UserRole.select().where(UserRole.id == id)
    return roles

def get_filtered_user_roles(query):
    roles = UserRole.select().where(UserRole.name.contains(query))
    return roles

def add_user_role(name, description):
    role = UserRole(name=name, description=description)
    role.save()

def update_user_role(id, name, description):
    role = UserRole.select().where(UserRole.id == id).get()
    role.description = description
    role.name = name
    role.save()

def delete_user_role(id):
    role = UserRole.select().where(UserRole.id == id).get()
    role.delete_instance()

## User Entiity operations
def get_users(id=None):
    if id==None:
        users = User.select()
    else:
        users = User.select().where(User.id == id)
    return users

def get_filtered_user(query):
    users = User.select().where(User.name.contains(query))
    return users

def add_user(name, studentId, userRoleId):
    user = User(name=name, studentId=studentId, userRoles=userRoleId)
    user.save()

def update_user(id, name, studentId, userRoleId):
    user = User.select().where(User.id == id).get()
    user.name = name
    user.studentId = studentId
    user.userRoles = userRoleId
    user.save()

def delete_user(id):
    #Item.delete().where(Item.id == id).execute()
    user = User.select().where(User.id == id).get()
    user.delete_instance()


