import re
import urllib.request

def get_subheadings(url):
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read().decode('utf-8')

        subheadings = re.findall(r'<h3>(.*?)</h3>', html_content)

        return subheadings

    except Exception as e:
        print("An error occurred: ", str(e))

url = "http://www.columbia.edu/~fdc/sample.html"
subheadings = get_subheadings(url)
print(subheadings)
