<html>
<body>
<hr/>
<form action="/update" method="post">
  <input type="hidden" name="id" value="{{str(user.id)}}"/>
  <p>Name:<input name="name" value="{{user.name}}"/></p>
  <p>Student ID:<input name="studentId" value="{{user.studentId}}"/></p>
  <p>User Role: </p>
  <select name="userRoleId" value="{{user.userRoles.id}}">
  <option value="">None</option>
  % for role in roles:
    <option value="{{role.id}}">{{role.name}}</option>
  % end
  </select>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>