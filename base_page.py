from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.cookie_modal = page.locator(".amgdprcookie-modal-template")
        self.close_cookie_btn = page.locator("#close-modal")
        self.sort_dropdown = page.locator(".sorter-dropdown .init")
        self.sort_price_asc = page.locator('li[data-value="price_asc"]')
        self.products = page.locator(".item.product.product-item")

    def open(self):
        self.page.goto("https://highlifeshop.com/cafe")

    def close_cookies(self):
        if self.cookie_modal.is_visible():
            self.close_cookie_btn.click()
            expect(self.cookie_modal).to_be_hidden()

    def sort_by_price_asc(self):
        self.sort_dropdown.click()
        self.sort_price_asc.click()
        self.products.first.wait_for()
        self.page.wait_for_load_state("networkidle")

    def get_prices(self):
        prices = []

        for product in self.products.all():
            price_el = product.locator("[data-price-amount]")

            if price_el.count() > 0:
                value = price_el.get_attribute("data-price-amount")
                if value:
                    prices.append(float(value))

        return prices
