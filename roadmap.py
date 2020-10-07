# https://app.codesignal.com/challenge/EaPKfzLacHZWoQA7X
from datetime import datetime
import numpy as np

def convertDate(date):
	date_format = "%Y-%m-%d"
	return datetime.strptime(date, date_format)


def roadmap(tasks, queries):
	results = []
	# # sort by name first
	# name_tasks = sorted(tasks, key=lambda name: name[0])
	# # then sort by date
	# sorted_tasks = sorted(name_tasks, key=lambda endDate: endDate[2])

	a = np.array(tasks)
	ind = np.lexsort((a[:,2],a[:,0]))    
	sorted_tasks = a[ind]

	for i, query in enumerate(queries): # query is a single list item
		result = [] # will get appended to results
		for j, task in enumerate(sorted_tasks): # task in 
			if convertDate(task[1]) <= convertDate(query[1]) <= convertDate(task[2]) and query[0] in task[3::]:
				# print(str(True) + ": " + str(task[0]))
				result.append(task[0])
		results.append(result)
	return results

# tasks = [["A", "2017-02-01", "2017-03-01", "Sam", "Evan", "Troy"],
#  ["B", "2017-01-16", "2017-02-15", "Troy"],
#  ["C", "2017-02-13", "2017-03-13", "Sam", "Evan"]]

# queries = [["Evan", "2017-03-10"],
#  ["Troy", "2017-02-04"]]

tasks = [["LNWBN","2017-08-13","2017-12-24","Corey","Kyle","Kaleb","Reuben"], 
 ["NSXEN","2017-08-20","2017-09-18","Kai"], 
 ["DNMDC","2017-06-19","2017-08-07","Kaleb","Kai","Kyle","Reuben"], 
 ["UYWEQ","2017-04-23","2017-07-18","Corey","Kyle","Reuben","Kai"], 
 ["LIVNH","2017-11-01","2017-12-24","Kaleb","Kai"]]

queries = [["Corey","2017-10-21"], 
 ["Reuben","2017-03-16"], 
 ["Kaleb","2017-11-22"], 
 ["Kaleb","2017-03-22"], 
 ["Reuben","2017-10-06"]]

result = roadmap(tasks, queries)
print(result)