
import webapp2
from caesar import encrypt
import cgi


page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>ROT13</title>
    <style type="text/css">
        textarea
        {
        width: 600px;
        height: 200px;
        }
        h1
        {
        color: purple;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">ROT13</a>
    </h1>
"""

# html boilerplate
page_footer = """
</body>
</html>
"""



class Index(webapp2.RequestHandler):

#builds the page the first time and retreives the user's information
    def get(self):

        user_input = """
<form method = "post">
<label><p><em>How many places would you like to shift?</em></p></label>
<input type="text" name="places" value="0">
<label><p><em>Enter the text you wish to encrypt</em></p></label>
<textarea name="original">{}</textarea>
<input type="submit">
</form
""".format("")

        response = page_header + user_input + page_footer
        self.response.write(response)

#takes the posted information, runs the encrypt function
#then builds the page again with the encrypted string

    def post(self):
        user_string = self.request.get("original")
        shift_num = self.request.get("places")

        answer = encrypt(cgi.escape(user_string, quote=True), int(shift_num))

        user_input = """
<form method = "post">
<label><p><em>How many places would you like to shift?</em></p></label>
<input type="text" name="places" value="0">
<label><p><em>Enter the text you wish to encrypt</em></p></label>
<textarea name="original">{}</textarea>
<input type="submit">
</form
""".format(answer)

        response = page_header + user_input + page_footer
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', Index),

], debug=True)
