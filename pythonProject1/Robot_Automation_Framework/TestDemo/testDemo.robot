*** Setting ***
Documentation  To validate the Login from
Library  SeleniumLibrary
Test Teardown    Close Browser

*** Variable ***
${Error_Message_Login}  css:.alert-danger

*** Test Cases ***
Validate UnSuccesful Login
    Open the browser with the Mortgage payment url
    Fill the login From
    wait untile it checked and display error message
    verify error message is correct

*** Keywords ***
Open the browser with the Mortgage payment url
    Create Webdriver    Chrome 	executable_path=C:/Users/DELL/OneDrive/Documents/chromedriver
    Go To   https://rahulshettyacademy.com/loginpagePractise/

Fill the login From
    INPUT TEXT      id:username     rahulshettyacademy
    INPUT PASSWORD  id:password     learnin
    click button    id:signInBtn


wait untile it checked and display error message
    wait until element is visible   ${Error_Message_Login}

verify error message is correct
    ${result}=  Get Text    ${Error_Message_Login}
    Should Be Equal As Strings   ${result}      Incorrect username/password.
    Element text should be  ${Error_Message_Login}  Incorrect username/password.
