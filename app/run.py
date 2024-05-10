from flask import Flask, render_template,request,jsonify

app=Flask(__name__)
app._static_folder='C:\\Users\\Radeon\\Documents\\projects\\jesterBot\\app\\static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['GET','POST'])
def chatbot():
    return "huh!"

if __name__=="__main__":
    app.run(debug=True)

