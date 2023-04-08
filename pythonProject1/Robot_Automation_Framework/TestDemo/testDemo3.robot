*** Setting ***
Documentation  To validate the Login from
Library  SeleniumLibrary
Library     Collections
Library     String
Test Setup      Open the browser with the Mortgage payment url
Test Teardown    Close Browser session
Resource    resource.robot

*** Variable ***
${Error_Message_Login}      css:.alert-danger


*** Test Cases ***
Validate Child window Functionality
   Select the link of Child window
   Verify the user is Switched to Child window
   Grab the Email id in the Child window
   switch to Parent window and enter the Email


*** Keywords ***
Select the link of Child window
    click element   css:.blinkingText
    sleep   5

Verify the user is Switched to Child window
    switch window   NEW
    element text should be  css:h1  DOCUMENTS REQUEST

Grab the Email id in the Child window
    ${text}=    get text    css:.red
    @{words}=   Split String     ${text}    at
    #0--->please email u
    #1--->mentor@rahulshettyacademy.com with below template to receive response
    ${text_split}=      Get From List       ${words}    1
    log  ${text_split}
    @{words_2}=   Split String    ${text_split}
    #0-->mentor@rahulshettyacademy.com
    ${email}=   Get From list   ${words_2}     0
    Set Global Variable    ${email}
switch to Parent window and enter the Email
    Switch window      MAIN
    Title should be     LoginPage Practise | Rahul Shetty Academy
    Input Text          id:username      ${email}