import json, requests, sys
from bs4 import BeautifulSoup, Comment

if __name__ == "__main__":
    file = sys.argv[1]
    save = sys.argv[2]
    f = open(file)
    data = json.load(f)

    # Generate URL list
    URLs = []
    comments_list = []
    for i in data['results']:
        if i['status'] != 403:
            URLs.append(i['url'])

    for url in URLs:

        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")

            for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
                comments_list.append(comments)
        except:
            pass

    with open(r'{}'.format(sys.argv[2]), 'w') as fp:
        for item in comments_list:
            fp.write("%s\n" % item)