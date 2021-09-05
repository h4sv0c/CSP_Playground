from flask import Flask,render_template,request,make_response


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("csp_form.html",csp="???",payload="????")


@app.route("/csp",methods=['GET'])
def playground():
	csp = request.args.get('csp_header')
	payload = request.args.get('payload')
	response = make_response(render_template("csp_form.html",csp=csp,payload=payload))
	response.headers.set("Content-Security-Policy",csp)

	return response


if __name__ == '__main__':
	app.run(debug=True)