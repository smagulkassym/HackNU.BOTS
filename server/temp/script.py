# import sys
# import json
#
# barcode = sys.stdin.readline().strip()
# fromTime = sys.stdin.readline().strip()
# toTime = sys.stdin.readline().strip()
#
# # Create a dictionary object and convert it to JSON
# response = {
#     "barcode": barcode,
#     "fromTime": fromTime,
#     "toTime": toTime,
# }
# json_response = json.dumps(response)
#
# # Send the JSON object back to Node.js
# sys.stdout.write(json_response)

import subprocess

barcode = '48743587'
fromTime = '2022-01-01 00:00:00'
toTime = '2023-01-04 15:45:00'

# Call the second Python script and pass the arguments
output = subprocess.check_output(["python3", "test.py", barcode, fromTime, toTime])
output = output.decode().strip()

# Print the output from the second script
print("Output from second script:", output)