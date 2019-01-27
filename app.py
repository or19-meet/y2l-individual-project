from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET, POST"])
def search():
	if request.method =="POST":
		keyword=request.form["keyword"]
		results=search_db(keyword)
		item = results.first() if results else None 
		return render_template("item.html", search=search)
	else:
		return render_template('sorry.html',query=query, results=results)

# @app.route('/')
# def search():
#     return render_template("store.html")

if __name__ == '__main__':
    app.run(debug=True)

