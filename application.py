from bottle import route, post, run, template, redirect, request
import database

database.set_up_database()

@route("/")
def get_users():
    users = database.get_users()
    return template("list_user.tpl", users=users)

@route("/add")
def get_add_user():
    roles = database.get_user_roles()
    return template("add_user.tpl", roles=roles)

@post("/add")
def post_add_user():
    name = request.forms.get("name")
    studentId = request.forms.get("studentId")
    userRoleId = request.forms.get("userRoleId")
    database.add_user(name, studentId, userRoleId)
    redirect("/")    

@route("/update/<id>")
def get_update_user(id):
    users = database.get_users(id)[0]
    roles = database.get_user_roles()
    userRoleId = users.userRoles.id if users.userRoles else ''
    return template("update_user.tpl", user=users, roles=roles, userRoleId=userRoleId)

@post("/update")
def post_update_user():
    name = request.forms.get("name")
    studentId = request.forms.get("studentId")
    id = request.forms.get("id")
    userRoleId = request.forms.get("userRoleId")
    database.update_user(id, name, studentId, userRoleId)
    redirect("/")    

@route("/delete/<id>")
def get_delete_user(id):
    database.delete_user(id)
    redirect("/")


## UserRole routes
@route("/user-role")
def get_user_roles():
    query = request.query.get("query")
    if(query):
        roles = database.get_filtered_user_roles(query)
    else:
        roles = database.get_user_roles()
        query = ''
    return template("list_user_role.tpl", roles=roles, query=query)

@route("/user-role/add")
def get_add_user_role():
    return template("add_user_role.tpl")

@post("/user-role/add")
def post_add_user_role():
    name = request.forms.get("name")
    description = request.forms.get("description")
    database.add_user_role(name, description)
    redirect("/user-role")    

@route("/user-role/update/<id>")
def get_update_user_role(id):
    roles = database.get_user_roles(id)
    return template("update_user_role.tpl", userRole=roles[0])

@post("/user-role/update")
def post_update_user_role():
    name = request.forms.get("name")
    description = request.forms.get("description")
    id = request.forms.get("id")
    database.update_user_role(id, name, description)
    redirect("/user-role")    

@route("/user-role/delete/<id>")
def get_delete_user_role(id):
    database.delete_user_role(id)
    redirect("/user-role")


run(host='localhost', port=8080)