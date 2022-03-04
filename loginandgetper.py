
from selenium import webdriver
import time
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

from selenium.webdriver.chrome.options import Options

class CreateDriver():
    def create_driver_session(self,session_id,executor_url):
        org_command_execute = RemoteWebDriver.execute
        def new_command_execute(self, command, params=None):
            if command == "newSession":
                return {'success': 0, 'value': None, 'sessionId': session_id}
            else:
                return org_command_execute(self, command, params)

        RemoteWebDriver.execute = new_command_execute

        new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        new_driver.session_id = session_id
        RemoteWebDriver.execute = org_command_execute

        return new_driver


class Getfollowers(CreateDriver):
    def usercon(self,user_name,password):
        global  boolValue
        boolValue= True
        self.user_name=user_name
        self.password=password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(chrome_options=chrome_options)
        executor_url = browser.command_executor._url
        session_id = browser.session_id
        self.executor_url=executor_url
        self.session_id=session_id
        print("usercon  executor_url", self.executor_url)
        print("usercon  session_id ", self.session_id)
        url="https://www.instagram.com/"
        self.browser=browser
        browser.get(url)
        print("url gorme:", self.browser.current_url)

        print("**-----------*************************-------------------*****************----------********")
        try:
            time.sleep(2)
            doldur1 = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
            doldur2 = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
            doldur1.send_keys(self.user_name)
            doldur2.send_keys(self.password)
            giris_yap = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
            giris_yap.click()
            time.sleep(2)
            boolValue= True
        except:
            print("girişte hata var")
            boolValue = False
        time.sleep(2)

        """
        try:
            acma = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
            if acma:
                acma.click()
                time.sleep(2)
                print("kapatıldı 1")
        except:
            print("konum kapamada hata var ")"""
        try:
            acma1 = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            if acma1:
                acma1.click()
                time.sleep(2)
                print("kapatıldı 2")
        except:
            print("bildirm kapatmada hata var ")

        try:
            profile1 = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]")
            profile1.click()
            print("profil1 fotografına tıklandı")
            profile_button = self.browser.find_element_by_css_selector(".-qQT3")
            profile_button.click()
            time.sleep(2)
            boolValue = True
        except:
            print("profile girişte hata var")
            #boolValue = False
        try:
            profile= self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/section/nav/div[2]/div/div/div[3]/div/div[5]")
            profile.click()
            time.sleep(2)
            print("profil fotografına tıklandı")
            profile_button= self.browser.find_element_by_css_selector(".-qQT3")
            profile_button.click()
            print("profile butonuna tıklandı")

            time.sleep(2)
            boolValue = True
        except:
            print("profile girişte hata var")
            #boolValue = False

        try:
            """**************************************TAKİP EDENLER******************************************"""
            allfol = self.browser.find_elements_by_css_selector(".Y8-fY")
            folwer = allfol[1]
            folwer.click()
            time.sleep(1)
            jscod="""
            followers=document.querySelector(".isgrP");
            followers.scrollTo(0,followers.scrollHeight);
            var lenOfPage=followers.scrollHeight;
            return lenOfPage;
            """
            lenOfPage = self.browser.execute_script(jscod)
            match=False
            while(match==False):
                lastCount = lenOfPage
                time.sleep(1)
                lenOfPage = self.browser.execute_script(jscod)
                if lastCount == lenOfPage:
                    match=True
            names= self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa") #TAKİP EDEN KİŞİLERİ ALIR
            global followers
            followers = list()
            for i in names:
                followers.append(i.text)
            time.sleep(1)
            self.browser.back()
            boolValue = True
        except:
            print("TAKİP EDEN KİŞİLERİ almada hata var")
            boolValue = False

        try:
            """**************************************TAKİP EDİLENLER******************************************"""
            allfol= self.browser.find_elements_by_css_selector(".Y8-fY")
            folwer =allfol[2]
            folwer.click()
            time.sleep(1)
            lenOfPage = self.browser.execute_script(jscod)
            match=False
            while(match==False):
                lastCount = lenOfPage
                time.sleep(1)
                lenOfPage = self.browser.execute_script(jscod)
                if lastCount == lenOfPage:
                    match=True
            global following
            following = list()
            names= self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")   #TAKİP EDİLEN KİŞİLERİ ALIR
            for i in names:
                following.append(i.text)
            time.sleep(1)
            boolValue = True
        except:
            print("TAKİP EDİLEN KİŞİLERİ ALMADA HATA VAR")
            boolValue = False
        try:
            global unfollow
            unfollow=list()
            i = 0
            while True:
                bool = True
                try:
                    for j in followers:
                        if following[i] == j:
                            bool = False
                            continue
                    if bool:
                        unfollow.append(following[i])
                    i += 1
                except IndexError:
                    break
            boolValue = True
        except:
            boolValue = False
            print("unfollower bulmada hata var")
        self.browser.back()
        if boolValue ==False:
            browser.close()
        print("return edilen  executor_url", self.executor_url)
        print("return edilen session_id", self.session_id)
        return  unfollow,self.session_id,self.executor_url,boolValue


    def other_page(self,second_user,session_id,executor_url):
        self.second_user = second_user
        self.session_id=session_id
        self.executor_url=executor_url
        self.browserbool=False
        browser=super(Getfollowers, self).create_driver_session(self.session_id,self.executor_url)
        print("other_page gönderilen isim",self.second_user)
        print("other_page browser executor_url", self.executor_url)
        print("other_page browser session_id", self.session_id)
        try:
            furl="https://www.instagram.com/"
            self.url=furl+second_user
            browser.get(self.url)


        except:
            print("hata aldık.")
            self.browserbool=True
            return self.browserbool
        
        
    def close_upwindows(self,session_id,executor_url):
        try:
            self.session_id = session_id
            self.executor_url = executor_url
            browser = super(Getfollowers, self).create_driver_session(self.session_id, self.executor_url)
            browser.close()


        

        except:
            print("there is a mistake")

        












