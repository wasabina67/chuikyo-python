import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore


def validate_title(title):
    expected_title = "中央社会保険医療協議会(中央社会保険医療協議会総会) ｜厚生労働省"
    assert expected_title == title


def main():
    url = "https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html"
    resp = requests.get(url)
    assert resp.status_code == 200
    soup = BeautifulSoup(resp.content, "html.parser")

    title = soup.find("title").text
    validate_title(title)


if __name__ == "__main__":
    main()
