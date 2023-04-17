'''
NOOTSUITE
quick and dirty privacy suite powered by python + flask, deployable in a single touch

To add support for other file types, you can add them to the `sft` list in `app.py`, then write a parser.
After that, you can add the parser to the `parsers` dictionary in `app.py`.
Example entry:
```python
'application/zip': parse_zip
```
'''
home_template = '''
<!DOCUTYPE html>
<html>
    <body>
        <h1>NOOTSUITE</h1>
        <p>quick and dirty privacy suite powered by python + flask, deployable in a single touch</p>
        <input type="text" id="url" placeholder="Enter URL here">
        <button onclick="window.location.href = '/'+encodeURIComponent(document.getElementById('url').value)">Get</button>
    </body>
</html>
'''
from flask import *
from bleach import clean
import urllib.parse
import requests
import bs4

# Supported file types
sft = [
    # text
    'text/html',
    'text/plain',
    'text/css',
    'text/javascript',
    'text/markdown',
    # image
    'image/png',
    'image/jpeg',
    'image/gif',
    'image/svg+xml',
    'image/webp',
    'image/x-icon',
    # audio
    'audio/mpeg',
    'audio/ogg',
    'audio/wav',
    'audio/webm',
    # video
    'video/mp4',
    'video/ogg',
    'video/webm',
    # application
    'application/javascript',
    'application/json',
    'application/pdf',
    'application/xml',
    'application/zip',    
]

# Misc Functions
def get_content_type(url): # Makes a HEAD request to the URL and returns the content type
    return requests.head(url).headers['content-type']

# Parsers
# text parsers
def parse_html(url):
    return str(bs4.BeautifulSoup(requests.get(url).text, 'html.parser'))
def parse_markdown(url):
    return str(bs4.BeautifulSoup(requests.get(url).text, 'markdown'))
def parse_text(url):
    return requests.get(url).text
def parse_css(url):
    return requests.get(url).text
def parse_js(url):
    return requests.get(url).text
# image parsers
def parse_image(url): # Generic image parser, as most image formats use the same parsing methods.
    return requests.get(url).content
# audio parsers
def parse_audio(url): # Refer to line 79
    return requests.get(url).content
# video parsers
def parse_video(url): # Refer to line 79
    return requests.get(url).content
# application parsers
def parse_application(url): # Refer to line 79
    return requests.get(url).content

# Parsers Dictionary
parsers = {
    'text/html': parse_html,
    'text/plain': parse_text,
    'text/css': parse_css,
    'text/javascript': parse_js,
    'text/markdown': parse_markdown,
    'image/png': parse_image,
    'image/jpeg': parse_image,
    'image/gif': parse_image,
    'image/svg+xml': parse_image,
    'image/webp': parse_image,
    'image/x-icon': parse_image,
    'audio/mpeg': parse_audio,
    'audio/ogg': parse_audio,
    'audio/wav': parse_audio,
    'audio/webm': parse_audio,
    'video/mp4': parse_video,
    'video/ogg': parse_video,
    'video/webm': parse_video,
    'application/javascript': parse_application,
    'application/json': parse_application,
    'application/pdf': parse_application,
    'application/xml': parse_application,
    'application/zip': parse_application,
}

def the_grand_parser(url): # The grand parser, which parses the URL and returns the parsed content
    content_type = get_content_type(url)
    parser = parsers[content_type]
    return parser(url)
# App
app = Flask(__name__)
@app.route('/')
def home():
    return home_template

@app.route('/<path:url>')
def get(url):
    url = urllib.parse.unquote(url)
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url # default to http
    return the_grand_parser(url)
app.run(port = 80)
