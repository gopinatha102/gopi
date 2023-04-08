*** Settings ***
Documentation   A resource file with reuasable keywords and variables..
...
...             the system specific keywords create here from our own
...             domain specific language. they utilize keyword provided
...             by the imported SeleniumLibray.
Library         SeleniumLibrary
Resource        ../Page_Object/Generic.robot

*** Variable ***
${user_name}     rahulshettyacademy
${Invalid_password}     learnin
${valid_password}       learning
${url}      https://rahulshettyacademy.com/loginpagePractise/
${driver_path}   C:/Users/DELL/OneDrive/Documents/chromedriver
*** Keywords ***

Open the browser with the Mortgage payment url
    Create Webdriver    Chrome 	executable_path=${driver_path}
    Go To   https://rahulshettyacademy.com/loginpagePractise/

Close Browser session
    Close Browser

wait until element passed is located on Page
    [arguments]     ${page_locator}
    wait until element is visible    ${page_locator}