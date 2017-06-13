from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

import utils

def click_to_new_page(driver, next_page_link_location):
    """Click on the element that permit to access to a new page
    Arguments:
    url (str): url of the actual page
    next_page_link_location (str): Location in dom of next page link
                                   element(Xpath by default)
    """

    try:
        next_page_link = driver.find_element_by_xpath(
            next_page_link_location)
    except NoSuchElementException as e:
        print(
            "[next page link on url : {} has not been found]".format(
                driver.current_url))
        return False
    ActionChains(driver).move_to_element(next_page_link).click().perform()

    def check_staleElement_exception():
        try:
            next_page_link.find_element_by_xpath(next_page_link_location)
            return False
        except StaleElementReferenceException:
            return True
    utils.wait_for(driver.current_url, check_staleElement_exception)
    return True
