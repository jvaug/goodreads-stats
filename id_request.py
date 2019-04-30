import keys
from betterreads import client
import time

key = keys.key
secret = keys.secret

gc = client.GoodreadsClient(key, secret)


user_id = int(input("Please input your user id #: "))

#add user shelf lookup


shelf = input("Please input your shelf name: ")

if shelf == "":
	shelf = "read"

#set user
user = gc.user(user_id)

#list of book objects
shelf_list = user.per_shelf_reviews(shelf_name=shelf)

#list of author ids
authors_on_shelf = []

for i in range(len(shelf_list)):
	authors_on_shelf.append(shelf_list[i].book['authors']['author']['id'])


gender = []

#iterate through all authors in list
for id_ in authors_on_shelf:
	author = gc.author(author_id=id_)
	gender.append(author.gender)
	time.sleep(1.5)

gender_counts = []

for a in set(gender):
	gender_counts.append([a, gender.count(a)])

#graphing

from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("bars.html")

genders = [b[0] if b[0] != None else 'None' for b in gender_counts]
counts = [b[1] if b[1] != None else 0 for b in gender_counts]

p = figure(x_range=genders, plot_height=250, title="Gender Counts",
           toolbar_location=None, tools="")

p.vbar(x=genders, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)