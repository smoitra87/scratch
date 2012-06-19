"""
Scrape Pubmed publications and get the baker nanomaterials paper

"""

import sys,os
import urlparse

import mechanize

ncbi_url = "http://www.ncbi.nlm.nih.gov/"

br = mechanize.Browser(factory=mechanize.RobustFactory())
br.set_handle_robots(False)

br.open(ncbi_url)
br.follow_link(text="PubMed",nr=0)


##############################
# Failed to do browser automation for this :(


