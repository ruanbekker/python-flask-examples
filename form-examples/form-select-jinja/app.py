from flask import Flask, render_template, request

app_version = '1.1.0'
countries = ['Australia', 'Mexico', 'New Zealand', 'South Africa', 'Switzerland']

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('form.html', countries=countries)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        return render_template("result.html", result=result) 

if __name__ == '__main__':
    app.run(debug = True)

