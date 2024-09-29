import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore


def main():
    url = "https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html"
    resp = requests.get(url)
    assert resp.status_code == 200
    soup = BeautifulSoup(resp.content, "html.parser")

    _ = soup.find("title").text


if __name__ == "__main__":
    main()
