from duckduckgo_search import DDGS


def web_search(query):

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=3)

        for r in search_results:
            results.append(r["body"])

    return "\n".join(results)