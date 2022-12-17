import time


class BasePage:






    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(self.driver, 10)

        #MWTHOD: create common selenium functions
        #enter_text_by_id(id, text)
        #click_element_by_id(id)
    def enter_text_by_id(selfself, id, text):

        try:
            log.info("enter the text by id..")
            element = self.wdwait.until(EC.presence_of_element_located(By.ID, id)))
            element.click()
            log.info('clicking the text by id..')
        except(NoSuchElementException, TimeoutExeption) as err:
            time.sleep(1)

