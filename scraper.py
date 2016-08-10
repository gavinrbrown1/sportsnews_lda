# script to pull down some BR pages from their website and get the main article

from urllib.request import urlopen
from bs4 import BeautifulSoup

from time import sleep, time  # so we don't get banned

base_url = "http://bleacherreport.com/articles/"
page_index = 2656275    # current top story index

request_index = 0
successes = 0   # requests not redirected

start = time()

file_index = open('data/file_index.txt', 'w')

while request_index < 100000:
    request_index += 1

    req_url = base_url + str(page_index)

    try:
        reply = urlopen(req_url)
        sleep(1)

        # tracker for my convinience on longer runs
        if request_index % 100 == 0:
            print(request_index)

        # check for redirects
        same = req_url == str(reply.geturl())[ :len(req_url)]

        if same:
            successes += 1
            soup = BeautifulSoup(reply, 'html.parser')
            article = soup.find('div', class_='article_body cf')

            file = open("data/br_html_" + str(page_index) + ".txt", "w")

            file_index.write('br_html_' + str(page_index) + '.txt' + ' ')

            paragraphs = article.find_all('p')
            for graph in paragraphs:
                file.write(graph.get_text())

            file.close()
    except:
        # print('Error on index %i' % page_index)
        pass

    page_index -= 1

file_index.close()

end = time()

print('Requested %i pages for %i articles in %4.1f seconds' % (request_index, successes, end-start))
