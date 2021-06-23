"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DEVIANT ART SCRAPER
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import os, sys, time, re, urllib
import selenium.webdriver as SN
import selenium.webdriver.common.keys as KY
import name_system as NS

DEVIANTART_LOGIN = 'https://www.deviantart.com/users/login'
DEVIANTART_GALLERY = 'https://www.deviantart.com/ARTIST/gallery/all'

LOGIC_PATH = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_PATH = 'C:\Pictures\TYPE\$ sort\\artists'


class DeviantArtScraper(object):
    driver = None

    def __init__(self):

        driverPath = os.path.join(LOGIC_PATH, 'geckodriver_win.exe')

        profile = SN.FirefoxProfile()
        #profile.DEFAULT_PREFERENCES['frozen']['javascript.enabled'] = False    # js needed for scroll down
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.update_preferences()

        self.driver = SN.Firefox(executable_path=driverPath, firefox_profile=profile)
        print(self.driver)

    def close(self):
        time.sleep(2)
        self.driver.close()

    def logIn(self, username, password):

        self.driver.get(DEVIANTART_LOGIN)
        self.driver.maximize_window() 
        time.sleep(0.3)

        usernameLm = self.driver.find_element_by_id('username')
        passwordLm = self.driver.find_element_by_id('password')
        submitLm = self.driver.find_element_by_id('loginbutton')

        usernameLm.send_keys(username)
        passwordLm.send_keys(password)
        time.sleep(1)
        submitLm.send_keys(KY.Keys.ENTER)
        
        time.sleep(3)
        print(self.driver.current_url)

    def getArtPages(self, deviantId):

        url = DEVIANTART_GALLERY.replace('ARTIST', deviantId)
        self.driver.get(url)

        # render thumbnails by scrolling down 
        # must keep a cumulative list because top is scrolled out of view

        bodyLm = self.driver.find_element_by_tag_name('body')
        lastHeight = self.driver.execute_script("return document.body.scrollHeight")
        reachedBottom = False
        reachedBuffer = 0
        pageDownCnt = 0
        pageLs = []

        while not reachedBottom:
            bodyLm.send_keys(KY.Keys.PAGE_DOWN)
            time.sleep(0.6)
            currentHeight = self.driver.execute_script("return document.body.scrollHeight")
            pageDownCnt += 1

            if currentHeight == lastHeight and reachedBuffer == 3:
                reachedBottom = True
            elif currentHeight == lastHeight:
                reachedBuffer += 1
            else:
                lastHeight = currentHeight
                reachedBuffer = 0

            # gather all links to pages with art, preserving their order

            anchorLs = self.driver.find_elements_by_tag_name('a')

            for elem in anchorLs:
                try:
                    href = elem.get_attribute('href')
                    if '/art/' in href and '#comments' not in href and href not in pageLs:
                        pageLs.append(href)
                except:
                    pass

            if pageDownCnt % 5 == 0:
                print(f"images: {len(pageLs)}")

        return pageLs

    def downloadArt(self, pageLink, artistType, collectionArtist):

        self.driver.get(pageLink)
        time.sleep(0.5)

        stageLm = self.driver.find_element_by_xpath('//div[@data-hook="art_stage"]')
        imageLm = stageLm.find_element_by_tag_name('img')
        src = imageLm.get_attribute('src')

        deviantImage = src.split('/')[-1]
        deviantImage = deviantImage.split('?')[0]
        collectionImage = self.getFileName(deviantImage, collectionArtist)

        targetDir = DOWNLOAD_PATH.replace('TYPE', 'Cosplay' if artistType == 'cosplay' else 'Fiction')
        targetDir = os.path.join(targetDir, collectionArtist)
        self.createDirectory(targetDir)

        targetFile = os.path.join(targetDir, collectionImage)
        urllib.request.urlretrieve(src, targetFile)

    def getFileName(self, deviantImage, collectionArtist):

        # the deviant art file name has a structure

        fileRx = r"^([a-zA-Z0-9_-]+)_by_([a-zA-Z0-9_-]+)-[a-z0-9]+.([a-zA-Z]+)"
        match = re.match(fileRx, deviantImage)

        if match is not None:
            artname = match.groups()[0].lower()
            artist = match.groups()[1].lower()
            fileType = match.groups()[2].lower()

            newart = NS.standardizeName(artname)
            fileNo = NS.getFileNo(artist)
            
            newFileName = "{} ({}) {}.{}".format(newart, collectionArtist, fileNo, fileType)

        # the deviant art file name is gibberish

        else:
            gibberish_rx = (r"[a-zA-Z0-9_-]+.([a-zA-Z]+)")
            gmatch = re.match(gibberish_rx, deviantImage)

            fileType = gmatch.groups()[0].lower()
            fileNo = NS.getFileNo(collectionArtist)

            newFileName = "_noname ({}) {}.{}".format(collectionArtist, fileNo, fileType)

        return newFileName

    def createDirectory(self, fullPath):
        if not os.path.exists(fullPath):
            os.mkdir(fullPath)

