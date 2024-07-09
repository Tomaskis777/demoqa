from pages.tables import Tables
import time


def test_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    # assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    time.sleep(2)
    # assert page_tables.no_data.exist()


