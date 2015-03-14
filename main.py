from flask import Flask, request, abort
from coreapp import app
import datetime
debug = True

@app.route('/answer', methods=['GET','POST'])
def answer():
	try:
	    month = str(request.form.get('Month'))
	    day = str(request.form.get('Day'))
	    year = str(request.form.get('Year'))
	    date = str(month + " " + day + ", " + year)
	    time = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%A')

	except Exception, e:
		time = str("This is an invalid date")

	answer = """
	<!DOCTYPE html>
	<html lang="en-US">
	<head>
		<title>Day of the Week</title>
	<meta charset="utf-8">
	</head>
	<body>
		<h1>Day of the Week</h1>
		<p>
	""" + time + """
		</p> 
	</body>
	</html>
	"""
	return answer

if __name__ == '__main__':
	app.run(debug = True)