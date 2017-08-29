from urllib2 import urlopen
from json import load

apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"

#Here is the part you adjust to get different output
apiParam = "/vehicleid/5782"

outputFormat = "?format=json"

response = urlopen(apiUrl + apiParam + outputFormat)

json_obj = load(response)

print '------------------------------'
print '           Result             '
print '------------------------------'
for objectCollection in json_obj['Results']:
	for safetyRatingAttribute, safetyRatingValue in objectCollection.iteritems():
		print safetyRatingAttribute, ": ", safetyRatingValue
