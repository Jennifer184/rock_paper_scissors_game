# Rock Paper Scissors Game
# Helpful tutorial to get started: https://www.youtube.com/watch?v=0TTpXDYnAg8

# Create a templates directory in mysite
# and place static html pages there

from flask import Flask, render_template, make_response
import random
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)

class Index(flask_restful.Resource):
    def __init__(self):
        self.playerPick = 0
        self.computerPick = 0
        self.handChoices = {
                1: 'Rock',
                2: 'Paper',
                3: 'Scissors'}
        self.rockDraw = make_response(render_template('rock_draw.html'))
        self.paperDraw = make_response(render_template('paper_draw.html'))
        self.scissorsDraw = make_response(render_template('scissors_draw.html'))
        self.rockScissors = make_response(render_template('rock_scissors.html'))
        self.rockPaper = make_response(render_template('rock_paper.html'))
        self.paperScissors =  make_response(render_template('paper_scissors.html'))
        self.paperRock =  make_response(render_template('paper_rock.html'))
        self.scissorsPaper = make_response(render_template('scissors_paper.html'))
        self.scissorsRock = make_response(render_template('scissors_rock.html'))

    def rockChoice(self):
        pc = self.computerPick

        if self.handChoices[pc] == 'Rock':
            return self.rockDraw
        if self.handChoices[pc] == 'Scissors':
            return self.rockScissors
        else:
            return self.rockPaper

    def paperChoice(self):
        pc = self.computerPick

        if self.handChoices[pc] == 'Paper':
            return self.paperDraw
        if self.handChoices[pc] == 'Scissors':
            return self.paperScissors
        else:
            return self.paperRock

    def scissorsChoice(self):
        pc = self.computerPick

        if self.handChoices[pc] == 'Scissors':
            return self.scissorsDraw
        if self.handChoices[pc] == 'Rock':
            return self.scissorsRock
        else:
            return self.scissorsPaper

    def get(self, userInput):
        self.computerPick = random.choice(list(self.handChoices.keys()))
        self.playerPick = userInput

        if self.handChoices[self.playerPick] == 'Rock':
            return self.rockChoice()

        if self.handChoices[self.playerPick] == 'Paper':
            return self.paperChoice()

        if self.handChoices[self.playerPick] == 'Scissors':
            return self.scissorsChoice()

    # def post(self): # I may want to use this later
    #     json_data = get_json(force=True)
    #     firstname = json_data['firstname']
    #     lastname = json_data['lastname']
    #     return jsonify(firstname=firstname, lastname=lastname)

api.add_resource(Index,'/<int:userInput>')

if __name__ == "__main__":
    app.run(debug=True)
