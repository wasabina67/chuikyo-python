import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore


def validate_headers(headers):
    expected_th_set = {
        "回数",
        "開催日",
        "議題等",
        "議事録／議事要旨",
        "資料等",
        "開催案内",
    }
    ths = headers.findAll("th")
    th_set = {th.text for th in ths}
    assert expected_th_set == th_set


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

    table = soup.find("table", {"class": "m-tableFlex"})
    rows = table.findAll("tr")
    headers, latest = rows[0], rows[1]
    validate_headers(headers)

    tds = latest.findAll("td")
    td_num, td_event_date, td_agenda, _, td_docs, _ = tds  # noqa
    latest_num = td_num.text
    print(latest_num)


if __name__ == "__main__":
    main()
