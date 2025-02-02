import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# Load student data from the JSON file
def load_data():
    with open('q-vercel-python.json', 'r') as file:
        data = json.load(file)
    return data

# Handler class to process incoming requests
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)

        # Get 'name' parameters from the query string
        names = query.get('name', [])

        # Load data from the JSON file
        data = load_data()

        # Prepare the result dictionary
        result = {"marks": []}
        for name in names:
            # Find the marks for each name
            for entry in data:
                if entry["name"] == name:
                    result["marks"].append(entry["marks"])

        # Send the response header
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS for any origin
        self.end_headers()

        # Send the JSON response
        self.wfile.write(json.dumps(result).encode('utf-8'))
