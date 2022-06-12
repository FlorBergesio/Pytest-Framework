from .web_scraping import PageWithListings

def test_web_scraping_trial_merchants(chrome_browser):
    chrome_browser.get("https://techstepacademy.com/trial-of-the-stones")
    html = chrome_browser.page_source

    listings_page = PageWithListings(html)

    highest_wealth_listing = listings_page.highest_wealth
    print("The listing with the highest wealth is: ",
          f"{highest_wealth_listing.name} with ${highest_wealth_listing.wealth}")
