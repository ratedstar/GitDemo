import time


class Screenshot():

    def takeScreenshot(self,driver):
        """
        take screenshot on open webpage
        :param driver:
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotpath = "E:\\PythonScreenShot\\"
        destinationfile = screenshotpath+fileName
        try:
            driver.save_screenshot(destinationfile)
            print("Screenshot directory::"+destinationfile)
        except NotADirectoryError:
            print("NotADirectoryError")

