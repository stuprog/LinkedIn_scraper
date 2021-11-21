import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from post import Post
from utils import scroll_down, extract_number


def redirect_to_all_posts(driver, url):
    driver.get(url)
    scroll_down(driver, 0, 1000)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='pv-profile-section__card-action-bar artdeco-container-card-action-bar "
                       "artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid "
                       "artdeco-button--muted ember-view']"))))
    time.sleep(2)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Posts']"))))

    scroll_down(driver, 0, 1000)
    time.sleep(2)
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    activity_section = soup.find('div', {'class': 'pv-recent-activity-detail__outlet-container'})
    all_posts = activity_section.findAll("div", {
        'class': 'occludable-update ember-view'})
    for post in all_posts:
        inspect_post(post)


def inspect_post(post_element):
    post_entity = Post()
    post_entity.owner = post_element.find('div', {'class': 'visually-hidden'}).get_text().strip()
    post_entity.time = post_element.find('span', {'class': 'visually-hidden'}).get_text().strip()
    post_element.find('li-icon', {'type': 'people-icon'}).get_text().strip()
    views = post_element.find_all('span', {'class': ['va-entry-point__num-views', 'icon-and-text-container t-14 '
                                                                                  't-black--light t-normal']})
    post_entity.views = extract_number(views[0].get_text().strip())[0]
    post_entity.interaction = post_element.find('span', {
        'class': 'v-align-middle social-details-social-counts__reactions-count'}).get_text().strip()
    if post_element.findAll('span', {'class': 'break-words'}):
        post_entity.type_of_content = 'Text Post'
        parent_span = post_element.find('span', {'class': 'break-words'})
        post_entity.text_content = parent_span.find('span', {'dir': 'ltr'}).get_text().strip()
    if post_element.findAll('div', {'aria-label': 'Video player'}):
        post_entity.type_of_content = 'Video'
        video_link_forbidden = post_element.find('video', {'class': 'vjs-tech'}).attrs['src']
        post_entity.content = video_link_forbidden.replace('amp;', '')
    if post_element.findAll('img', {'class': 'ivm-view-attr__img--centered feed-shared-image__image lazy-image '
                                             'ember-view'}):
        post_entity.type_of_content = 'Image'
        post_entity.content = post_element.find('img', {
            'class': 'ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view'}).attrs['src']
    print(post_entity)
