import pandas as pd
from flask import  Flask, render_template

app = Flask(__name__)
df = pd.read_csv('dictionary.csv')
@app.route("/lesson")
def lesson():
    return render_template("lesson.html")

@app.route('/lesson/api/v1/<word>')
def api(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    return {
        "definition": definition.replace("\n", ''),
        "word": word
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)
