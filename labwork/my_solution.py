#!/usr/bin/python3
#
# License: CC-0

import sys
import json
import requests

if len(sys.argv) != 4:
	print("syntax: %s [API endpoint URI] [client ID] [assignment_name]" % (sys.argv[0]))
	sys.exit(1)

api_endpoint = sys.argv[1]
client_id = sys.argv[2]
assignment_name = sys.argv[3]

# Example handler for the "strcat" assignment
def handle_strcat(assignment):
	return " ".join(assignment["parts"])

# Example handler for "foobar" assignment
def handle_foobar(assignment):
	return { "foo": "bar" }

session = requests.Session()
# Get the assignment
result = session.get(api_endpoint + "/assignment/" + client_id + "/" + assignment_name)
assert(result.status_code == 200)

# See if we can compute the answer
assignment = result.json()
known_assignment_count = 0
unknown_assignment_count = 0
pass_count = 0
for testcase in assignment["testcases"]:
	if testcase["type"] == "strcat":
		known_assignment_count += 1
		response = handle_strcat(testcase["assignment"])
	elif testcase["type"] == "foobar":
		known_assignment_count += 1
		response = handle_foobar(testcase["assignment"])
	else:
		unknown_assignment_count += 1
		print("Do not know how to handle type: %s" % (testcase["type"]))
		continue

	# We think we have an answer for this one, try to submit it
	result = session.post(api_endpoint + "/submission/" + testcase["tcid"], headers = {
		"Content-Type": "application/json",
	}, data = json.dumps(response))
	assert(result.status_code == 200)
	submission_result = result.json()
	if submission_result["status"] == "pass":
		pass_count += 1
	else:
		print(submission_result)
print("%d known assignments, %d unknown." % (known_assignment_count, unknown_assignment_count))
print("Passed: %d. Failed: %d" % (pass_count, known_assignment_count - pass_count))
