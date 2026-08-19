import webbrowser
from urllib.parse import quote


def google_search(query):
    query = query.strip()

    if not query:
        return

    print(f"🔎 Searching Google for: {query}")

    url = "https://www.google.com/search?q=" + quote(query)

    webbrowser.open(url)


def youtube_search(query):
    query = query.strip()

    if not query:
        return

    print(f"🎬 Searching YouTube for: {query}")

    url = "https://www.youtube.com/results?search_query=" + quote(query)

    webbrowser.open(url)


def execute_web_command(command):

    command = command.lower().strip()

    if command.startswith("search for "):
        query = command.replace("search for ", "", 1).strip()
        google_search(query)
        return True

    if command.startswith("search "):
        query = command.replace("search ", "", 1).strip()
        google_search(query)
        return True

    if command.startswith("google "):
        query = command.replace("google ", "", 1).strip()
        google_search(query)
        return True

    if command.startswith("youtube "):
        query = command.replace("youtube ", "", 1).strip()
        youtube_search(query)
        return True

    if command.startswith("search youtube for "):
        query = command.replace(
            "search youtube for ", "", 1
        ).strip()

        youtube_search(query)
        return True

    return False