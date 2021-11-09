% include('new_item.tpl')

<h1>Items</h1>
<form action="/delete" method="post">
%for row in rows:
    <div>
        <b>Item:</b> {{row[1]}} <b>Price:</b> {{row[2]}} <button type="submit" name="delete" value='{{row[0]}}'>Delete</button>
    </div>
%end
</form>