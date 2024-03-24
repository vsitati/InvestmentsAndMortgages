from config import RunConfig

from playwright.sync_api import Page

def base_url():
    return RunConfig.url