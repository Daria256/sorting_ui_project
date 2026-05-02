from pages.base_page import BasePage


def test_sorting_by_price(page):
    base = BasePage(page)
    base.open()
    base.close_cookies()
    base.sort_by_price_asc()
    prices = base.get_prices()
    print(prices)
    assert prices == sorted(prices), f"Prices not sorted: {prices}"
