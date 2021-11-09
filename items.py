import sqlite3
from bottle import redirect, request, route, run, template
from bottle import post, get, put, delete

@route('/')
def todo_list():
    # Send the output from a select query to a template
    conn = sqlite3.connect('items.db')
    c = conn.cursor()    
    c.execute("SELECT * FROM items order by item")
    result = c.fetchall()
    # define a template to be used, and pass the SQL results
    output = template('list', rows=result)
    return output

# Add new items into the database
@post('/add')
def new_item():
    price = request.forms.get("price")
    item = request.forms.get("item")

    if item != "":        
        conn = sqlite3.connect('items.db')
        c = conn.cursor()
        c.execute("INSERT INTO items (item,price) VALUES (?,?)", (item,price))
        conn.commit()
        c.close()

    redirect("/")

# Delete an item in the database
@post('/delete')
def delete_item():
    id = request.forms.get("delete").strip()
               
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    sqlstr = "DELETE FROM items WHERE id=" + str(id)
    c.execute(sqlstr)
    conn.commit()
    c.close()

    redirect("/")

if __name__ == '__main__':
    run(reloader=True, debug=True)