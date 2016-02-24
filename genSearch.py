#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import webbrowser
#import mechanize
#from bs4 import BeautifulSoup
#import re

ancestry = "http://search.ancestry.com/cgi-bin/sse.dll?gl=allgs&gss=sfs28_ms_f-2_s&new=1&rank=1&msT=1"

firstName = raw_input('First Name of the individual to search: ')
firstName = firstName.replace(" ", "+")

ancestry += "&gsfn=" + firstName

fnexact = raw_input('Exactly that first name?(type \'y\' for yes or just enter for no: ')
if fnexact == 'y' or fnexact == 'Y':
	ancestry += "&gsfn_x=1"
else:
	ancestry += "&gsfn_x=0"

lastName = raw_input('Last Name: ')
lastName = lastName.replace(" ", "+")

ancestry += "&gsln=" + lastName

lnexact = raw_input('Exactly that last name?(type \'y\' for yes or just enter for no: ')
if lnexact == 'y' or lnexact == 'Y':
	ancestry += "&gsln_x=1"
else:
	ancestry += "&gsln_x=0"

ancestry += "&MSAV=1&cp=0&catbucket=rstp&uidh=qth"


webbrowser.open_new_tab(ancestry)

