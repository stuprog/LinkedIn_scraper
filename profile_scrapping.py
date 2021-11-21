from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from user import User
import time

from utils import scroll_down


def scrap_profile_link(driver):
    driver.find_element(By.XPATH, "//a[@class='ember-view block']").click()
    time.sleep(2)
    profile_url = driver.current_url
    driver.get(profile_url)
    return profile_url


def scrap_profile_info(driver):
    link = scrap_profile_link(driver)
    user = User()
    user.profile_url = link
    # will be used in the while loop
    scroll_down(driver, 0, 1000)
    src = driver.page_source
    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')
    profile_section = soup.find('section', {'class': 'artdeco-card ember-view pv-top-card'})
    intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
    name_loc = intro.find("h1")
    # Extracting the Name
    name = name_loc.get_text().strip()
    # strip() is used to remove any extra blank spaces
    works_at_loc = intro.find("div", {'class': 'text-body-medium'})
    # this gives us the HTML of the tag in which the Company Name is present
    # Extracting the Company Name
    works_at = works_at_loc.get_text().strip()
    location_loc = profile_section.find_all("span", {'class': 'text-body-small inline t-black--light break-words'})
    # Extracting the Location
    # The 2nd element in the location_loc variable has the location
    location = location_loc[0].get_text().strip()
    user.location = location
    user.name = name
    user.title = works_at
    job_title = profile_section.find("div", {"class": "text-body-medium break-words"}).get_text().strip()
    user.position = job_title;
    feed_link = "https://www.linkedin.com/feed/"
    driver.get(feed_link)
    src1 = driver.page_source
    soup1 = BeautifulSoup(src1, 'lxml')
    profile_feed_section = soup1.find('div', {'class': 'feed-identity-module artdeco-card overflow-hidden mb2'})
    profile_views = profile_feed_section.find('div', {
        'class': 'feed-identity-widget-item__icon-stat t-12 t-black t-bold flex-1'}).get_text().strip()
    profile_connection_section = profile_feed_section.find_all('a', {
        'href': ['/mynetwork/invite-connect/connections/', '/mynetwork/']})
    connections_count = profile_connection_section[0].find('span', {
        'class': 'feed-identity-widget-item__stat'}).get_text().strip()
    user.profile_views = profile_views
    user.connections = connections_count
    return user
