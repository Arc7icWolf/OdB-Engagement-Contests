import streamlit as st
import requests
import json


# Send request, get response, return decoded JSON response
def get_response(data, session: requests.Session):
    urls = [
        "https://api.deathwing.me",
        "https://api.hive.blog",
        "https://hive-api.arcange.eu",
        "https://api.openhive.network",
    ]
    for url in urls:
        request = requests.Request("POST", url=url, data=data).prepare()
        response_json = session.send(request, allow_redirects=False)
        if response_json.status_code == 502:
            continue
        response = response_json.json().get("result", [])
        if len(response) == 0:
            print(f"{response_json.json()} from this {data}")
        return response


def get_posts(session: requests.Session):
    authors = ["balaenoptera", "balaenoptera", "bencwarmer"]
    clues = ["Top Author of", "UNTO&BISUNTO:", "OdB Engagement"]
    contest_posts = []
    for author in authors:
        data = (
            f'{{"jsonrpc":"2.0", "method":"bridge.get_account_posts", '
            f'"params":{{"sort":"posts", "account": "{author}", '
            f'"limit": 10}}, "id":1}}'
        )
        posts = get_response(data, session)
        for post in posts:
            author = post["author"]
            permlink = post["permlink"]
            title = post["title"]
            cover = post["json_metadata"].get("image", [])
            if not cover:
                cover = post["json_metadata"].get("links", [])
            for clue in clues:
                if clue in title:
                    contest_posts.append(
                        {
                            "image": cover[0].strip(") "),
                            "link": "https://peakd.com/@" + author + "/" + permlink,
                        }
                    )
                    clues.remove(clue)
                    break

    return contest_posts


def mainpage(session: requests.Session):
    st.markdown(
        """
        <style>
        /* Sfondo */
        .stApp {
            background-image: url("https://files.peakd.com/file/peakd-hive/arc7icwolf/23wMgpxaWnhqwUSGxBdP7z4VCd6AFzQfGrFYVVcyHLhLjnfZXfhyoJskq4Vha6QAuDbVP.jpeg");
            background-size: cover;
            background-position: center;
        }

        /* Stile del testo con bordo nero sfumato */
        h1, h2, h3, p, .stMarkdown {
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        }

        /* Centrare le immagini */
        .stImage {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---- Titolo centrato ----
    st.markdown(
        "<h1 style='text-align: center;'>Olio di Balena Engagement Contests</h1>",
        unsafe_allow_html=True,
    )

    # ---- Introduzione ----
    st.markdown("### Scegli qua sotto il contest a cui sei interessato!")

    # ---- Tabella con immagini e link ----
    posts = get_posts(session)

    # Definiamo il numero di colonne per riga
    NUM_COLS = 3

    # Creazione della griglia dinamica
    rows = [posts[i : i + NUM_COLS] for i in range(0, len(posts), NUM_COLS)]

    for row in rows:
        cols = st.columns(len(row))  # Crea un numero di colonne pari ai post nella riga
        for i, post in enumerate(row):
            with cols[i]:
                st.markdown(
                    f'<a href="{post["link"]}" target="_blank">'
                    f'<img src="{post["image"]}" style="height:200px; width:auto; max-width:100%;">'
                    f"</a>",
                    unsafe_allow_html=True,
                )

    # ---- Testo sotto le immagini ----
    st.markdown(
        "### Sei qui per un po' di dati? Clicca sul menù a tendina a fianco per accedere a ciò che cerchi!"
    )


if __name__ == "__main__":
    try:
        with requests.Session() as session:
            mainpage(session)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"JSON decode error or missing key: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
