# https://app.codesignal.com/challenge/EaPKfzLacHZWoQA7X
from datetime import datetime

def convertDate(date):
	date_format = "%Y-%m-%d"
	return datetime.strptime(date, date_format)


def roadmap(tasks, queries):
	results = []

	for i, query in enumerate(queries): # query is a single list item
		result = [] # will get appended to results
		for j, task in enumerate(tasks): # task in 
			if convertDate(task[1]) < convertDate(query[1]) < convertDate(task[2]) and query[0] in task[3::]:
				print(str(True) + ": " + str(task[0]))
				result.append(task[0])

	return []

tasks = [["A", "2017-02-01", "2017-03-01", "Sam", "Evan", "Troy"],
 ["B", "2017-01-16", "2017-02-15", "Troy"],
 ["C", "2017-02-13", "2017-03-13", "Sam", "Evan"]]

queries = [["Evan", "2017-03-10"],
 ["Troy", "2017-02-04"]]

result = roadmap(tasks, queries)
print(result)