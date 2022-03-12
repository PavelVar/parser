"""Class with parser for finding different texts in internet sites.
Function 'find_vacancy_links' creates and returns generator with links to vacancies.
Function 'get_vacancy_text' creates and returns text of each vacancy."""
from bs4 import BeautifulSoup
from requests import Response
from typing import Generator


class RabotaByVacancyParser:
    """Allows to find text on pages from internet sites. Extracts data from http responses."""

    @staticmethod
    def find_vacancy_links(page: Response) -> Generator:
        """Gets page and using BeautifulSoup library returns list of links to vacancies from this page """
        soup = BeautifulSoup(page.text, 'html.parser')

        # create list with all strings contained vacancy links
        strings_with_links = soup.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'})

        # cut list members to left links only and returns it
        return (link['href'] for link in strings_with_links)

    @staticmethod
    def get_vacancy_text(page: Response) -> str:
        """Gets page from and using BeautifulSoup library returns text of the vacancy from this page """
        soup = BeautifulSoup(page.text, 'html.parser')

        text = soup.find('div', {'class': 'vacancy-section'}).text.lower()

        return text
