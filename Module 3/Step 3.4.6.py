import requests, re


def get_one_level_urls(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return re.findall(r'href=\"(.*)\"', response.text)
    else:
        return []


def is_reachable(from_url: str, to_url: str):
    refs = get_one_level_urls(from_url)
    for ref in refs:
        if to_url in get_one_level_urls(ref):
            return 'Yes'
    return 'No'


# print(is_reachable(input(), input()))

a = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
b = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
print(is_reachable(a, b))  # Yes

a = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
b = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
print(is_reachable(a, b))  # No

a = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
b = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
print(is_reachable(a, b))  # Yes
