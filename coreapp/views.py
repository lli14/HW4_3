# views.py
from coreapp import app

@app.route('/')
def index():
	page = """
	<!DOCTYPE html>
	<html lang="en-US">
	<head>
		<title>Day of the Week</title>
	<meta charset="utf-8">
	</head>
	<body>
		<h1>Day of the Week Finder</h1>
		<p>Pick a Month, Day, and Year, then click submit.</p> 
		<form action="/answer" method="post"> 	
		<select name="Month">
		  <option value="January">1</option>
		  <option value="February">2</option>
		  <option value="March">3</option>
		  <option value="April">4</option>
		  <option value="May">5</option>
		  <option value="June">6</option>
		  <option value="July">7</option>
		  <option value="August">8</option>
		  <option value="September">9</option>
		  <option value="October">10</option>
		  <option value="November">11</option>
		  <option value="December">12</option>
		</select>
		<select name="Day">
		  <option value="1">1</option>
		  <option value="2">2</option>
		  <option value="3">3</option>
		  <option value="4">4</option>
		  <option value="5">5</option>
		  <option value="6">6</option>
		  <option value="7">7</option>
		  <option value="8">8</option>
		  <option value="9">9</option>
		  <option value="10">10</option>
		  <option value="11">11</option>
		  <option value="12">12</option>
		  <option value="13">13</option>
		  <option value="14">14</option>
		  <option value="15">15</option>
		  <option value="16">16</option>
		  <option value="17">17</option>
		  <option value="18">18</option>
		  <option value="19">19</option>
		  <option value="20">20</option>
		  <option value="21">21</option>
		  <option value="22">22</option>
		  <option value="23">23</option>
		  <option value="24">24</option>
		  <option value="25">25</option>
		  <option value="26">26</option>
		  <option value="27">27</option>
		  <option value="28">28</option>
		  <option value="29">29</option>
		  <option value="30">30</option>
		  <option value="31">31</option>
		</select>
		<select name="Year">
		  <option value="2014">2014</option>
		  <option value="2015">2015</option>
		  <option value="2016">2016</option>
		  <option value="2017">2017</option>
		  <option value="2018">2018</option>
		  <option value="2019">2019</option>
		  <option value="2020">2020</option>
		</select>
		 <input value="submit" id="submit" type="Submit">
		 </form>	  
	</body>
	</html>

	"""
	return page