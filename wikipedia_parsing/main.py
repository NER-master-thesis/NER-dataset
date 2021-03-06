# -*- coding: utf-8 -*-
"""
Created by e-bug on 07/03/17.
"""

import lxml.etree as ET
import sys


from pages_manager import Pages_manager
from wikipedia_iterator import Wikipedia_iterator
from utils import *
wiki_iterator = Wikipedia_iterator()
pages_manager = Pages_manager()
page = True
#wikipedia_to_wikidata = load_pickle("/dlabdata1/braemy/wikipedia_classification/wikipedia_to_wikidata.p")
#wikidata_to_ner = load_pickle("/dlabdata1/braemy/wikidata-classification/mapping_wikidata_to_NER.p")
#wikiTitle_to_id = load_pickle("/dlabdata1/braemy/wikipedia_classification/title_to_id_170.p")

#wp_to_ner_by_title = load_pickle("/dlabdata1/braemy/wikipedia_classification/wp_to_ner_by_title.p")
personal_titles = load_personal_titles()
#alternative_titles = load_json("/dlabdata1/braemy/wikidataNER/alternative_titles.json")

while page is not None:
    try:
        page =wiki_iterator.next_page()
        if page.is_redirect() or page.title== "NO-TITLE":
            continue
        #if page.id is not None and int(page.id) %10000 == 0:
        #    print(page.id)
        if page.title != "Germany national football team":
            continue
        print(page.get_text())
        sys.exit()
        page.parse(wp_to_ner_by_title=wp_to_ner_by_title, personal_titles=personal_titles,alternative_titles=alternative_titles)
        pages_manager.add_page(page)
    except StopIteration:
        pages_manager.save_all()

pages_manager.save_all()