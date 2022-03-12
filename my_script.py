from tools.rabota_parser import RabotaByVacancyParser
from clients.http_client import HTTPClient
from requests import codes


def text_finder(text_to_find: str):
    url = 'https://rabota.by/search/vacancy'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/94.0.4606.61 Safari/537.36"}

    text_to_find_amount = 0
    page_num = 0

    while True:
        params = {'text': text_to_find, 'page': page_num, 'city': 'Minsk'}
        page_with_vacancies = HTTPClient().get(url, headers=headers, params=params)
        status = page_with_vacancies.status_code
        if status == codes.ok:
            vacancies_link_list = RabotaByVacancyParser().find_vacancy_links(page_with_vacancies)

            for vacancy_link in vacancies_link_list:
                vacancy_page = HTTPClient().get(vacancy_link, headers=headers)
                vacancy_text = RabotaByVacancyParser().get_vacancy_text(vacancy_page)
                text_to_find_amount += vacancy_text.count(text_to_find)

            page_num += 1
        else:
            break

    print(f'Text {text_to_find} is mentioned {text_to_find_amount} times on {page_num} pages. Each page contains '
              f'this text {text_to_find_amount / page_num} times in average.')


if __name__ == '__main__':

    text_finder('python')
    text_finder('linux')
    text_finder('flask')
