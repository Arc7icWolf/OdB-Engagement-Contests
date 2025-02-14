import streamlit as st

# ---- CSS per sfondo e centratura ----
st.markdown(
    """
    <style>
    /* Sfondo */
    .stApp {
        background-image: url("https://files.peakd.com/file/peakd-hive/arc7icwolf/23wMgpxaWnhqwUSGxBdP7z4VCd6AFzQfGrFYVVcyHLhLjnfZXfhyoJskq4Vha6QAuDbVP.jpeg");
        background-size: cover;
    }

    /* Centrare il testo */
    .title, .stMarkdown {
        text-align: center;
    }

    /* Centrare le immagini */
    .stImage {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Titolo e introduzione ----
st.title("Olio di Balena Engagement Contests")
st.markdown("### Scegli qua sotto il contest a cui sei interessato!")
st.markdown("Sei qui per un po' di dati? Clicca su un'immagine per accedere al post!")

# ---- Tabella con immagini e link ----
posts = [
    {"image": "https://files.peakd.com/file/peakd-hive/arc7icwolf/23wMgpxaWnhqwUSGxBdP7z4VCd6AFzQfGrFYVVcyHLhLjnfZXfhyoJskq4Vha6QAuDbVP.jpeg", "link": "https://peakd.com/hive-146620/@balaenoptera/olio-di-balena-scegli-il-migliore-autore-della-settimana-top-author-of-the-week-week-41-jwj"},
    {"image": "https://files.peakd.com/file/peakd-hive/arc7icwolf/23wMgpxaWnhqwUSGxBdP7z4VCd6AFzQfGrFYVVcyHLhLjnfZXfhyoJskq4Vha6QAuDbVP.jpeg", "link": "https://peakd.com/hive-146620/@balaenoptera/untoandbisunto-14-contest-decentralizzato-settimanale-su-olio-di-balena-prize-pool-100-hive-nuovo-tema--vincitori-12-contest"},
    {"image": "hhttps://files.peakd.com/file/peakd-hive/arc7icwolf/23wMgpxaWnhqwUSGxBdP7z4VCd6AFzQfGrFYVVcyHLhLjnfZXfhyoJskq4Vha6QAuDbVP.jpeg", "link": "https://peakd.com/hive-146620/@bencwarmer/eng-ita-odb-engagement-contest"},
]

# Creazione delle colonne per la visualizzazione delle immagini
cols = st.columns(len(posts))
for i, post in enumerate(posts):
    with cols[i]:
        st.markdown(f'<a href="{post["link"]}" target="_blank"><img src="{post["image"]}" width="100%"></a>', unsafe_allow_html=True)

