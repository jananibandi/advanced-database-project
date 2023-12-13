<html>
<body>
<h2>Users</h2>
<hr/>
<table>
% for user in users:
  <tr>
    <td>{{str(user.name)}}</td>
    <td>{{str(user.studentId)}}</td>
    <td>{{user.userRoles.name}}</td>
    <td><a href="/update/{{str(user.id)}}">update</a></td>
    <td><a href="/delete/{{str(user.id)}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add a new item</a>
<hr/>
</body>
</html>