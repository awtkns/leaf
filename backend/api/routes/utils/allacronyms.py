
# creidts to ConnorSMaynes: https://github.com/ConnorSMaynes/allacronyms
import requests, re
from lxml.etree import HTML as get_xml
from collections import OrderedDict, namedtuple

SITE = {
    'root'          :   'https://www.allacronyms.com'
    ,'search'       :   '/{keywords}'
    ,'top_topics'   :   '/aa-topics'
    ,'random'       :   '/aa-random-term?nocache=1'
}

Abbreviation = namedtuple( 'Abbreviation', 'rating confidence definition abb' )

class AllAcronyms():
    '''
    Purpose:    The purpose of this class is to function as an unofficial API
                to the website allacronyms.com. It can get cgenerally search the site 
                for abbreviations / definitions.
                The site automatically determines if a definition or abbreviation
                has been searched for.
    '''

    def __init__(self):
        self._categories = None
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

    def _extractAbbreviations( self, SearchResultXML, Random=False):
        '''
        Purpose:    Extract abbreviations from page xml allacronyms.com page.
        Arguments:
            SearchResultXML - xml page - xml page returned in search
            Random - if random is True, retrieve a random acronym. Otherwise, retrieve a valid phrase
        Returns:
            Abbreviations - list of Abbreviation - list of all abbreviations extracted.
        '''
        Abbreviations = []
        
        if SearchResultXML is not None:
            if Random == True:
                AbbrevElms = SearchResultXML.xpath('//div[@class="item_container"]/descendant::*[@href][1]/text()')
                return AbbrevElms[0]
            else: 
                AbbrevElms = SearchResultXML.xpath('//div[@class="item_text"]/text()')   # 1 is the actual results, 2 is RELATED
        
            for AbbrevElm in AbbrevElms:
                Abbreviations.append( AbbrevElm.strip() )
        
        return Abbreviations

    def _search(self, Keywords, Reverse=False, TopCount=1 ):
        '''
        Purpose:    Search the site with the given set of search criteria.
        Arguments:
            Keywords - str - str of keywords to search under. Can be abbreviation
                                or definition
            TopCount - int - number of results to return
        Returns:
            Abbs - list of Abbreviations - Abbreviations returned from search.
        '''

        Abbs = []

        # VALIDATE USER INPUTS
        if Keywords == None:
            raise ValueError( 'ERROR : KEYWORDS CANNOT BE NONE' )
        elif not isinstance( Keywords, str ):
            raise ValueError( 'ERROR : KEYWORDS MUST BE A STRING' )

        SearchURL = SITE['root'] + SITE['search']. \
                    format(keywords=Keywords)

        # INITIAL SEARCH
        SearchResponse = requests.get( SearchURL, headers=self.headers )
        if SearchResponse.status_code != 200:                               # error return no results
            return []
        SearchResultXML = get_xml(SearchResponse.text)

        # GET ABBREVIATIONS UNTIL TOPCOUNT MET OR SEARCH RESULTS END
        Abbs += self._extractAbbreviations( SearchResultXML )
        if len( Abbs ) < TopCount:
            PageCountElms = SearchResultXML.xpath(
                                    '//div[@class="aa-pagination"]' +
                                    '/a[contains(@class,"counter")]' +
                                    '/text()' )
            if len( PageCountElms ) > 0:
                PageCount = int(PageCountElms[0].rsplit('/')[1])
                Search_Base_URL = SearchResponse.url
                iPage = 2
                while len( Abbs ) < TopCount and \
                    iPage < PageCount:
                    Next_Search_URL = Search_Base_URL + '/' + str(iPage)
                    NextSearchResponse = requests.get( Next_Search_URL )
                    NextSearchXML = get_xml( NextSearchResponse.text )
                    Abbs += self._extractAbbreviations( NextSearchXML, False )
                    iPage += 1
                Abbs = self._calculateConfidences( Abbs )

        return Abbs

    def search( self, Keywords, Quantity=1 ):
        '''
        Purpose:    Get abbreviations / definitions / ratings for a string
                    you think may have an abbreviation.
        Arguments:
            Keywords - str - combination of keywords you think might have an abbreviation
            Quantity - int - [ optional ] how many Abbreviations to return
        Returns
            Abbs - Abbreviation or
                   list of Abbreviations -    if Quantity = 1, Abbreviation
                                              if Quantity > 1, [ Abbreviation1, Abbreviation2, ... ]
                                              if no abbreviations found,
                                                 if Quantity = 1, return None
                                                 if Quantity > 1, return []
        '''
        Abbs = self._search( Keywords=Keywords, TopCount=Quantity )
        if len( Abbs ) == 0:
            if Quantity == 1:
                return None
            else:
                return []
        else:
            if Quantity == 1:
                return Abbs[ 0 ]
            else:
                return Abbs[:Quantity]

    def getRandom( self ):
        '''
        Purpose:    Get random abbreviations.
        '''
        RandomURL = SITE['root'] + SITE['random']
        RandomResponse = requests.get( RandomURL, headers=self.headers )
        RandomResultXML = get_xml( RandomResponse.text )

        return self._extractAbbreviations( RandomResultXML, Random=True )
