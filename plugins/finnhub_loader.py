import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cponsg9r01qiv403hqa0cponsg9r01qiv403hqag")

    news = finnhub_client.general_news('general', min_id=0)

    return news
