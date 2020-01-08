from flask import Flask

app = Flask(__name__)

# Show all catalog
@app.route('/')
def showcatalog():
    return "show catalog main page"


# Show login page
@app.route('/login')
def showlogin():
    return "login page"


# Add item 
@app.route('/catalog/new')
def newItem():
    return "add new item"


# Show catalog items
@app.route('/catalog/<string:cat_name>')
def showItems(cat_name):
    return "catalog %s items" % cat_name


# Show item description
@app.route('/catalog/<string:cat_name>/<string:item_name>')
def showDescription(cat_name, item_name):
    return "description of item %s" %item_name


# Edit item
@app.route('/catalog/<string:cat_name>/<string:item_name>/edit')
def editItem(cat_name, item_name):
    return "Edit item %s" %item_name    


# Delete item
@app.route('/catalog/<string:cat_name>/<string:item_name>/delete')
def deleteItem(cat_name, item_name):
    return "Delete item %s" %item_name



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)