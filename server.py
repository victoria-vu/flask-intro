"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULT = [
    'terrible', 'smelly', 'ugly', 'horrendous']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    <br/><a href="/hello">Come say hi!</a> 
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>

          <form action="/greet">
          What's your name? <input type="text" name="person">
          
          <h2>Would you like a compliment or insult?</h2>

          <div>
          <label for="compliment-select">Choose your compliment:</label>

          <select name="compliment" id="compliment-select">
            <option value="{AWESOMENESS[0]}">{AWESOMENESS[0]}</option>
            <option value="{AWESOMENESS[1]}">{AWESOMENESS[1]}</option>
            <option value="{AWESOMENESS[2]}">{AWESOMENESS[2]}</option>
            <option value="{AWESOMENESS[3]}">{AWESOMENESS[3]}</option>
            <option value="{AWESOMENESS[4]}">{AWESOMENESS[4]}</option>
            <option value="{AWESOMENESS[5]}">{AWESOMENESS[5]}</option>
            <option value="{AWESOMENESS[6]}">{AWESOMENESS[6]}</option>
            <option value="{AWESOMENESS[7]}">{AWESOMENESS[7]}</option>
            <option value="{AWESOMENESS[8]}">{AWESOMENESS[8]}</option>
            <option value="{AWESOMENESS[9]}">{AWESOMENESS[9]}</option>
            <option value="{AWESOMENESS[10]}">{AWESOMENESS[10]}</option>
            <option value="{AWESOMENESS[11]}">{AWESOMENESS[11]}</option>
            <option value="{AWESOMENESS[12]}">{AWESOMENESS[12]}</option>
            <option value="{AWESOMENESS[13]}">{AWESOMENESS[13]}</option>
          </select>

          <input type="submit" value="Submit">
          </div>
          </form>

          </br>

          <div>
          <form action="/diss">
          <label for="insult-select">Choose your insult:</label>
          
          <select name="insult" id="insult-select">
            <option value="{INSULT[0]}">{INSULT[0]}</option>
            <option value="{INSULT[1]}">{INSULT[1]}</option>
            <option value="{INSULT[2]}">{INSULT[2]}</option>
            <option value="{INSULT[3]}">{INSULT[3]}</option>
          </select>

          <input type="submit" value="Submit">
          </div>
          </form>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def get_diss():
    """Get insult only."""

    insult = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hey you. I don't care about your name. I think you're {insult}.
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
