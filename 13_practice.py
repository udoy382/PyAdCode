# -------------------------------------
# Python chapter 13 practice set
# -------------------------------------

#  (1) make a two virtualenv.

#  (2) need input to user and using .formet.
'''
name = input("Enter you name: ")
marks = input("Enter you marks: ")
phone = input("Enter you phone: ")

templete = "The name of the student is {}, his marks are {}, and phone number is {} "
output = templete.format(name, marks, phone)
print(output)
'''

#  (3) make a multiplaction table in vartical
'''
l = [str(i*7) for i in range(1, 11)]
print(l)

varticaltable = "\n".join(l)
print(varticaltable )
'''

#  (4) dibigable 5
'''
l = [1,2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 44, 67, 87, 90, 34, 34, 3, 45]

a = filter(lambda a: a%5==0, l)

print(list(a))
'''

#  (5) print max value in this list.
'''
from functools import reduce

l = [2, 3, 8, 9, 5, 676, 11, 4]

a = reduce(max, l)
# print(max(7, 34, 6))
print(a)
'''

#  (6) make a web server with flask and python.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Hey Udoy!</title>
  </head>
  <body>
    <h1>Saifur Rahman Udoy!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True)
