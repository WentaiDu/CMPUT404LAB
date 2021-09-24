#!/usr/bin/env python3

#print()
#print(f'<b>hello</b>')

import os,json

print("Content-type:text/html\r\n\r\n")
#print("Content-Type: application/json") #let browser know to expect json
print()
print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")
# Question 1
print(os.environ)
#print("Content-Type: application/json") #let browser know to expect json
json_object=json.dumps(dict(os.environ), indent =4)
#print(json_object)

# Question 2
#for param in os.environ.keys():
 #   if(param=="QUERY_STRING"):
 #       print(f"<em>{param}</em> ={os.environ[param]}</li>")
 #       print("<b>%20s</b> %s<br>" % (param, os.environ[param]))
#print(os.environ["QUERY_STRING"])

# Question 3
# print(os.environ["HTTP_USER_AGENT"])

# Question 4

# print("Content-Type: text/plain")
# print()
# print(os.environ)

# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")