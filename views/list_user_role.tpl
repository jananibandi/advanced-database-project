<html>
<body>
<h2>User Roles</h2>
<hr/>
<form action="/user-role" method="get">
  <label for="search">Search User</label>
  <input type="text" id="search" name="query" value="{{query}}"></input>
  <button type="submit">Search</button>
</form>
<table>
% for role in roles:
  <tr>
  <td>{{str(role.name)}}</td>
  <td>{{str(role.description)}}</td>
  <td><a href="/user-role/update/{{str(role.id)}}">update</a></td>
  <td><a href="/user-role/delete/{{str(role.id)}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/user-role/add">Add a new item</a>
<hr/>
</body>
</html>