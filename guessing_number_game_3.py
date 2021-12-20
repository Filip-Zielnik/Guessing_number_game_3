from flask import Flask, request

app = Flask(__name__)

FORM_1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game</title>
</head>
<body>
<h1>Imagine number between 1 and 1000 and I will figure it out in maximum of 10 tries!</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</body>
</html>
"""

FORM_2 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game</title>
</head>
<body>
<h1>Is it number {guess}?</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="Too big!">
    <input type="submit" name="user_answer" value="Too small!">
    <input type="submit" name="user_answer" value="You won!">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""

FORM_3 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game</title>
</head>
<body>
<h1>Great, Your number is {guess}!</h1>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    """
    Computer guesses user number.
    :return: Too big!, Too small!, You win!
    """
    if request.method == "GET":
        return FORM_1.format(0, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "Too big!":
            max_number = guess
        elif user_answer == "Too small!":
            min_number = guess
        elif user_answer == "You won!":
            return FORM_3.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return FORM_2.format(guess=guess, min=min_number, max=max_number)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
