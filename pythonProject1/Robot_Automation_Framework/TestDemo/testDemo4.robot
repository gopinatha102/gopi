*** Setting ***
Documentation  To validate the Login from
Library  SeleniumLibrary
Test Teardown    Close Browser
Test Template    Validate UnSuccesful Login

*** Variable ***
${Error_Message_Login}      css:.alert-danger

*** Test Cases ***      username    password
Invalid username        dashed      learning
Invalid password        rahulshetty  fdedd
special characters      @#$         learning

*** Keywords ***
Validate UnSuccesful Login
    [Arguments]     ${username}     ${password}
    Open the browser with the Mortgage payment url
    Fill the login Form     ${username}      ${password}
    wait untile it checked and display error message
    verify error message is correct

Open the browser with the Mortgage payment url
    Create Webdriver    Chrome 	executable_path=C:/Users/DELL/OneDrive/Documents/chromedriver
    Go To   https://rahulshettyacademy.com/loginpagePractise/

Fill the login Form
    [arguments]     ${username}     ${password}
    INPUT TEXT      id:username    ${username}
    INPUT PASSWORD  id:password    ${password}
    click button    id:signInBtn


wait untile it checked and display error message
    wait until element is visible   ${Error_Message_Login}

verify error message is correct
    ${result}=  Get Text    ${Error_Message_Login}
    Should Be Equal As Strings   ${result}      Incorrect username/password.
    Element text should be  ${Error_Message_Login}  Incorrect username/password.
