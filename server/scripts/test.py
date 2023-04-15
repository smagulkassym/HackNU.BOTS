import sys
import json

barcode = sys.stdin.readline().strip()
fromTime = sys.stdin.readline().strip()
toTime = sys.stdin.readline().strip()

# Create a dictionary object and convert it to JSON
response = {
    "barcode": barcode,
    "fromTime": fromTime,
    "toTime": toTime,
}
json_response = json.dumps(response)

# Send the JSON object back to Node.js
sys.stdout.write(json_response)
