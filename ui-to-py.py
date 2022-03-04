
from PyQt5 import uic



with open("C:\\Users\\Can\\Documents\\Python\\PayCharm\\Selenium\\.app\\INTERFACEAPP.py","w",encoding="utf-8") as file:
    uic.compileUi("INTERFACEAPP.ui",file)
































"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""



"""
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

class CreateDriver():
    def create_driver_session(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(chrome_options=chrome_options)
        executor_url = browser.command_executor._url
        session_id = browser.session_id
        print("üst sınıftaki executer url",executor_url)
        print("üst sınıftaki sessinn id ",session_id)

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

class Cem_karaca(CreateDriver):
    def usercon(self):
        url = "https://eksisozluk.com/cem-karaca--32837"
        browser = super(Cem_karaca, self).create_driver_session()
        self.browser = browser
        self.browser.get(url)
        print("url gorme:", browser.current_url)
        print("window handle: ",browser.current_window_handle)
        print("browser urlsi",browser.command_executor._url)
        print("browser oturum idsi",browser.session_id)

        time.sleep(5)
    def other_page(self,pagenum=1):
        try:
            self.pagenum = pagenum
            furl = "https://eksisozluk.com/cem-karaca--32837"
            self.url = furl + str(self.pagenum)
            self.browser.get(self.url)
            print("browser1 url gorme:", self.browser.current_url)
            print("browser1 window handle: ", self.browser.current_window_handle)
            print("browser1 browser urlsi", self.browser.command_executor._url)
            print("browser1 browser id si", self.browser.session_id)
        except:
            print("hata aldık amk.")

obje=Cem_karaca()
obje.usercon()
time.sleep(3)
while True:
    response= int(input("değeriniz:"))
    if response != 0:
        response = input("2.değeriniz:")
        obje.other_page("?p="+str(response))
        time.sleep(3)

    else:
        break






"""

























"""

driver = webdriver.Chrome()
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("http://tarunlalwani.com")
time.sleep(2)
print ("session id",session_id)
print ("executer url",executor_url)

def create_driver_session(session_id, executor_url):


    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver
print ("en alttaki ilk print")
driver2 = create_driver_session(session_id, executor_url)
print ("en alttaki print",driver2.current_url)








"""












































