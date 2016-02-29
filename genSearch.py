#!/usr/bin/python
# -*- coding: utf-8 -*-


''' 
                   _______                       __    
.-----.-----.-----|   _   .-----.---.-.----.----|  |--.
|  _  |  -__|     |   1___|  -__|  _  |   _|  __|     |
|___  |_____|__|__|____   |_____|___._|__| |____|__|__|
|_____|           |:  1   |                            
                  |::.. . |                            
                  `-------'                            
'''
import sys
import webbrowser

print sys.argv
firstName  = str(sys.argv[1])
lastName = str(sys.argv[2])
place = str(sys.argv[3])
when = str(sys.argv[4])
# First name of the individal to search
# firstName = raw_input('First Name of the individual to search: ')
firstName = firstName.replace(" ", "+")

# Last name of individual
#lastName = raw_input('Last Name: ')
lastName = lastName.replace(" ", "+")

# Place where the individual could have lived
#place = raw_input('Where they lived (separate by commas ex. city,state,country): ')
place = place.replace(" ", "")
place = place.replace(",", "%2C")

# When the person could have lived need to restrict to integers
#when = raw_input('Where they lived (year ex. 1771): ')

# Ancestry
ancestry = "http://search.ancestry.com/cgi-bin/sse.dll?gl=allgs&gss=sfs28_ms_f-2_s&new=1&rank=1&msT=1"
ancestry += "&gsfn=" + firstName
ancestry += "&gsln=" + lastName
ancestry += "&mswpn__ftp=" + place
ancestry += "&msbdy=" + when

# Findmypast
findmypast = "http://search.findmypast.com/results/world-records?"
findmypast += "firstname=" + firstName
findmypast += "&lastname=" + lastName
place = place.replace("%2C", "utf002c%20")
findmypast += "&keywordsplace=" + place
findmypast += "&eventyear=" + when + "&eventyear_offset=2"


# Creating the query strings for individual sites
ancestry += "&gsfn=" + firstName
findmypast += "firstname=" + firstName

# Determining whether the name should be exact or not.  Maybe change wording...
#fnexact = raw_input('Exactly that first name?(type \'y\' for yes or just enter for no: ')
# if fnexact == 'y' or fnexact == 'Y':
# 	ancestry += "&gsfn_x=1"
# 	findmypast += "&firstname_variants=true"
# else:
# 	ancestry += "&gsfn_x=0"



# ancestry += "&gsln=" + lastName
# findmypast += "&lastname=" + lastName

# #lnexact = raw_input('Exactly that last name?(type \'y\' for yes or just enter for no: ')
# if lnexact == 'y' or lnexact == 'Y':
# 	ancestry += "&gsln_x=1"
# 	indmypast += "&lastname_variants=true"
# else:
# 	ancestry += "&gsln_x=0"

ancestry += "&mswpn__ftp=" + place
# Changing the place syntax for findmypast
place = place.replace("%2C", "utf002c%20")
findmypast += "&keywordsplace=" + place



ancestry += "&msbdy=" + when
findmypast += "&eventyear=" + when + "&eventyear_offset=2"

ancestry += "&MSAV=1&cp=0&catbucket=rstp&uidh=qth"

# Open tabs
webbrowser.open_new_tab(ancestry)
webbrowser.open_new_tab(findmypast)

#https://familysearch.org/search/record/results?count=20&query=%2Bgivenname%3ADaniel%20%2Bbirth_place%3A%22Iowa%2C%20USA%22~%20%2Bbirth_year%3A1992-1992~
#http://search.findmypast.com/results/world-records?firstname=george&firstname_variants=true&lastname=ebeling&lastname_variants=true&eventyear=1880&eventyear_offset=2&keywordsplace=philadelphiautf002c%20pennsylvania
#http://search.ancestry.com/cgi-bin/sse.dll?gl=allgs&gss=sfs28_ms_f-2_s&new=1&rank=1&msT=1&gsfn=Dan&gsfn_x=0&gsln=Ebeling&gsln_x=0&mswpn__ftp=Broomall%2C%20Pennsylvania%2CUSA&MSAV=1&msbdy=1992&cp=0&catbucket=rstp&uidh=qth
