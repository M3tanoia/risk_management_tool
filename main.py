from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    if request.method == 'POST':
        # Process the form data
        company_name = request.form['company_name']
        risk_assessment = {}
        for key, value in request.form.items():
            if key != 'company_name':
                risk_assessment[key] = value
        # Render the results page with the risk assessment data
        return render_template('results.html', company_name=company_name, risk_assessment=risk_assessment)
    else:
        # Render the assessment form
        return render_template('assessment.html')

if __name__ == '__main__':
    app.run(debug=True)
