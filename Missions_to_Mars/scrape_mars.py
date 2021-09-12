{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "58cceac2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Dependencies\n",
    "import time\n",
    "import pymongo\n",
    "import requests\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "4d8de1ee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "5e2cd554",
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "94604269",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "e3dcb189",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    collection.drop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "31533c77",
   "metadata": {},
   "outputs": [],
   "source": [
    "news_url = 'https://redplanetscience.com'\n",
    "browser.visit(news_url)\n",
    "news_html = browser.html\n",
    "news_soup = bs(news_html,'lxml')\n",
    "news_title = news_soup.find(\"div\",class_=\"content_title\")\n",
    "news_para = news_soup.find(\"div\", class_=\"rollover_description_inner\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "9b67703e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-95-61097c0154ff>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-95-61097c0154ff>\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    base_link = [https:]+jpl_soup.find('div', class_='jpl_logo')\u001b[0m\n\u001b[0m                      ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# jurl = 'https://spaceimages-mars.com'\n",
    "# browser.visit(jurl)\n",
    "# jhtml = browser.html\n",
    "# jpl_soup = bs(jhtml,\"html.parser\")\n",
    "# image_url = jpl_soup.find('div',class_='carousel_container')\n",
    "# base_link = \"https:\"+jpl_soup.find('div', class_='jpl_logo')\n",
    "# feature_url = base_link+image_url\n",
    "# featured_image_title = jpl_soup.find('h1', class_=\"media_feature_title\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "e53dff05",
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementClickInterceptedException",
     "evalue": "Message: element click intercepted: Element <a target=\"_blank\" class=\"showimg fancybox-thumbs\" href=\"image/featured/mars3.jpg\">...</a> is not clickable at point (599, 547). Other element would receive the click: <div class=\"fancybox-overlay fancybox-overlay-fixed\" style=\"width: auto; height: auto; display: block;\">...</div>\n  (Session info: chrome=93.0.4577.63)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mElementClickInterceptedException\u001b[0m          Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-98-dbabd7bba4b5>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     10\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquote\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m     \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlinks\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_by_partial_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'FULL IMAGE'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36mclick\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    823\u001b[0m                 \u001b[0merror\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    824\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 825\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0merror\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    826\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    827\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mcheck\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36mclick\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    816\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mend_time\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    817\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 818\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_element\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    819\u001b[0m             except(\n\u001b[1;32m    820\u001b[0m                 \u001b[0mElementClickInterceptedException\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py\u001b[0m in \u001b[0;36mclick\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     78\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     79\u001b[0m         \u001b[0;34m\"\"\"Clicks the element.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 80\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_execute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCLICK_ELEMENT\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     81\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     82\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0msubmit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py\u001b[0m in \u001b[0;36m_execute\u001b[0;34m(self, command, params)\u001b[0m\n\u001b[1;32m    631\u001b[0m             \u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    632\u001b[0m         \u001b[0mparams\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'id'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_id\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 633\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    634\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    635\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mID\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mElementClickInterceptedException\u001b[0m: Message: element click intercepted: Element <a target=\"_blank\" class=\"showimg fancybox-thumbs\" href=\"image/featured/mars3.jpg\">...</a> is not clickable at point (599, 547). Other element would receive the click: <div class=\"fancybox-overlay fancybox-overlay-fixed\" style=\"width: auto; height: auto; display: block;\">...</div>\n  (Session info: chrome=93.0.4577.63)\n"
     ]
    }
   ],
   "source": [
    "for x in range(1, 6):\n",
    "\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "    quotes = soup.find_all('span', class_='text')\n",
    "\n",
    "    for quote in quotes:\n",
    "        print('page:', x, '-------------')\n",
    "        print(quote.text)\n",
    "\n",
    "    browser.links.find_by_partial_text('FULL IMAGE').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b28ce947",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
