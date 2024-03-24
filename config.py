import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:

    cases_path = os.path.join(PRO_PATH, "tests")

    browser = "firefox"

    headless = False

    url = "https://www.imbankgroup.com/ke/"

    rerun = "0"

    max_fail = "5"

    NEW_REPORT = None