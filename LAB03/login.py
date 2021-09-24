
import cgi
import cgitb
import os
from http.cookies import SimpleCookie
from templates import login_page, secret_page, after_login_incorrect
import secret
# Create simple login form

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("/head")
print("<body>")
print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
print("</body>")
print("</html>")


form_ok = username == secret.username and password == secret.password
s = SimpleCookie(os.environ["HTTP_COOKIE"])
s_username = None
s_password = None
if s.get("username"):
    s_username = s.get("username").value
if s.get("password"):
    s_password = s.get("password").value

cookie_ok = s_username == secret.username and s_password == secret.password

if cookie_ok:
    username = s_username
    password = s_password

#print("Content-Type: text/html")

if form_ok:
    print("Set-Cookie: username=asdc")
    print("Set-Cookie: password=2000")

#print()
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print("login correctly")
    print(secret_page(username, password))
else:
    print("login incorrectly")
    print(after_login_incorrect())
    print("username = ", username)
    print("password = ", password)
#print()

