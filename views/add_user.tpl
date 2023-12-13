<html>
<body>
<hr/>
<form action="/add" method="post">
  <p>Name:<input name="name"/></p>
  <p>Student Id:<input name="studentId"/></p>
  <p>User Role: </p>
  <select name="userRoleId">
  <option value="none">None</option>
  % for role in roles:
    <option value="{{role.id}}">{{role.name}}</option>
  % end
  </select>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>