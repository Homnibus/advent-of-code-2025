import requests
from os.path import exists
from os import makedirs


def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_input_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


def get_instructions_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}"


YEAR = 2025
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "github.com/tomfran/advent-of-code-setup reddit:u/fran-sch, discord:@tomfran#5786"
}
COOKIES = {"session": SESSION}


def get_instructions(day):
    path = f"instructions/{day:02d}.instructions"

    if not exists(path):
        url = get_instructions_url(YEAR, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )

        # Extract only <main> content
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(response.text, "html.parser")
        main_content = soup.find("main")
        content = main_content.get_text(strip=True) if main_content else response.text

        makedirs("instructions", exist_ok=True)
        with open(path, "w") as f:
            f.write(content)

    with open(path, "r") as f:
        return f.read()


def get_input(day):
    path = f"inputs/{day:02d}.input"

    if not exists(path):
        url = get_input_url(YEAR, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        makedirs("inputs", exist_ok=True)
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()
