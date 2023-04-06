from os import path


class ScreenshotTool:

    def __init__(self, driver): 
        self.driver = driver
    
    def saveScreenshot(self, fileLocation, testName):
        screenshot_file_path = path.join(fileLocation, f"{testName}.png")
        self.driver.save_screenshot(screenshot_file_path)
      