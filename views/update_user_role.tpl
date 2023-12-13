<html>
<body>
<hr/>
<form action="/user-role/update" method="post">
  <input type="hidden" name="id" value="{{str(userRole.id)}}"/>
  <p>Name:<input name="name" value="{{userRole.name}}"/></p>
  <p>Description:<input name="description" value="{{userRole.description}}"/></p>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>