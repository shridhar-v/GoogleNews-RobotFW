from Selenium2Library import Selenium2Library
class Selenium2Custom(Selenium2Library):
    """
    Custom wrapper for robotframework Selenium2Library to add extra functionality
    """
    def get_onclick(self, locator):
        """
        Returns the placeholder text of element identified by `locator`.
        """
        element = self._element_find(locator, True, False)
        return element.get_attribute("@outerHTML")