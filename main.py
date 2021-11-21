from authentication import connect_to_linkedin
from post_scrapping import redirect_to_all_posts
from profile_scrapping import scrap_profile_info, scrap_profile_link
from utils import initialize


def scrap_profile():
    driver = initialize()
    connect_to_linkedin(driver, "username", "password")
    user = scrap_profile_info(driver)
    print(user)


def scrap_post():
    driver = initialize()
    connect_to_linkedin(driver, "username", "password")
    redirect_to_all_posts(driver, scrap_profile_link(driver))


if __name__ == '__main__':
    scrap_post()
