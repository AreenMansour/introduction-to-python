import urllib.parse
import bs4
import sys
import requests
import pickle

def open_file(index_file):
    with open(index_file) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def count_elements(lst, lst2):
    d = dict()
    for element in lst:
        if element not in lst2:
            continue
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    return d


def helper_crawl(url_path):
    response = requests.get(url_path)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    x = [link.get("href") for p in soup.find_all("p") for link in p.find_all("a")]
    x = [element for element in x if element]
    return x


def crawl(base_url, index_file, out_file):
    dic = dict()
    lst_page = open_file(index_file)
    for page in lst_page:
        full_url = urllib.parse.urljoin(base_url, page)
        neighbors = helper_crawl(full_url)
        dic[page] = count_elements(neighbors, lst_page)

    write_file(dic, out_file)


def write_file(dic, out_file):
    with open(out_file, "wb") as f:
        pickle.dump(dic, f)
        f.close()


##################################################################################################


def page_rank(iterations, dict_file, out_file):
    with open(dict_file, "rb") as f:
        d = pickle.load(f)
        f.close()
    dic = dict.fromkeys(d.keys(), 1)
    for l in range(iterations):
        new_dic = dict.fromkeys(d.keys(), 0)
        for i in d.keys():
            for j in d.keys():
                s = 0
                for num in d[i]:
                    s += d[i][num]
                if j in d[i]:
                    new_dic[j] += dic[i] * d[i][j] / s
        dic = dict.copy(new_dic)
    write_file(dic, out_file)


########################################################################################################
"""part3"""


def helper_word_dict(url_path, d, page):
    response = requests.get(url_path)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    for p in soup.find_all("p"):
        content = p.text.split()
        for i in range(len(content)):
            if content[i] not in d:
                d[content[i]] = {page: 1}
            elif content[i] in d and page not in d[content[i]]:
                d[content[i]][page] = 1
            else:
                d[content[i]][page] += 1
    return d


def words_dict(base_url, index_file, out_file):
    dic = dict()
    lst_page = open_file(index_file)
    for page in lst_page:
        full_url = urllib.parse.urljoin(base_url, page)
        dic = helper_word_dict(full_url, dic, page)
    write_file(dic, out_file)


def get_pages(dict):
    lst = []
    for p in dict:
        lst.append(p)
    return lst


def search(words, ranking_dict_file, words_dict_file, max_result):
    with open(ranking_dict_file, "rb") as f:
        ranking_dict = pickle.load(f)
    with open(words_dict_file,"rb") as f:
        words_dict = pickle.load(f)
    words2 = set()
    pages = list(words_dict[words[0]])
    words2.add(words[0])
    for j in range(1,len(words)):
        if words[j] not in words_dict:
            continue
        words2.add(words[j])
        pages = [ pages[i] for i in range(len(pages)) if  pages[i] in words_dict[words[j]]]
    if len(pages) > max_result:
        pages_rank = sorted(pages, key= lambda x:ranking_dict[x], reverse=True)[:max_result]
    else:
        pages_rank = pages
    sort_key = dict()
    for page in pages_rank:
        sort_key[page] = min([ words_dict[word][page] * ranking_dict[page] for word in words2])
    final_pages = sorted(pages_rank, key = lambda x: sort_key[x], reverse=True)
    for page in final_pages:
        print(page, sort_key[page])


if __name__ == '__main__':
    if len(sys.argv) == 5:
        if sys.argv[1] == "crawl":
            base_url = sys.argv[2]
            index_file = sys.argv[3]
            out_file = sys.argv[4]
            crawl(base_url, index_file, out_file)
        if sys.argv[1] == "page_rank":
            iterations = int(sys.argv[2])
            dict_file = sys.argv[3]
            out_file = sys.argv[4]
            page_rank(iterations, dict_file, out_file)
        if sys.argv[1] == "words_dict":
            base_url = sys.argv[2]
            index_file = sys.argv[3]
            out_file = sys.argv[4]
            words_dict(base_url, index_file, out_file)
    if len(sys.argv) == 6:
        query = sys.argv[2]
        ranking_dict = sys.argv[3]
        word_dict = sys.argv[4]
        max_result = int(sys.argv[5])
        search(query.split(), ranking_dict, word_dict, int(max_result))