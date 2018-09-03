from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/pokemon/<query>', methods=['GET'])
def main(query=1):
	# GET
	res = requests.get('http://pokeapi.co/api/v2/pokemon/' + query)
	info = res.json()
	print(info)
	# Display
	if query.isdigit():
		line = 'The pokemon with id ' + str(info['id']) + ' is ' + info['name']
		return render_template('index.html', line=line)
	line = info['name'] + ' has' + ' id ' + str(info['id'])
	return render_template('index.html', line=line)


if __name__ == '__main__':
    app.run()
