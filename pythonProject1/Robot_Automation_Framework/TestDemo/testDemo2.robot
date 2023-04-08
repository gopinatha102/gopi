*** Setting ***
Documentation  To validate the Login from
Library  SeleniumLibrary
Library     Collections
Test Setup      Open the browser with the Mortgage payment url
Test Teardown    Close Browser session
Resource    resource.robot

*** Variable ***
${Error_Message_Login}      css:.alert-danger
${Shop_page_load}           css:.nav-link
${Card_title}               css:.card-title

*** Test Cases ***
Validate UnSuccesful Login`
    Fill the login Form      ${user_name}      ${Invalid_password}
    wait untile Element is located in the page   ${Error_Message_Login}
    verify error message is correct

Validate Cards display in the Shopping Page
    Fill the login Form     ${user_name}    ${valid_password}
    wait untile Element is located in the page      ${Shop_page_load}
    Verify Card titles in the Shop page
    Select the Card     Blackberry

Select the From and navigate to Child window
    Fill the login Details and Loging Form


*** Keywords ***

Fill the login Form
    [arguments]     ${username}     ${password}
    INPUT TEXT      id:username    ${username}
    INPUT PASSWORD  id:password    ${password}
    click button    id:signInBtn


wait untile Element is located in the page
    [arguments]  ${element}
    wait until element is visible    ${element}

verify error message is correct
    ${result}=  Get Text    ${Error_Message_Login}
    Should Be Equal As Strings   ${result}      Incorrect username/password.
    Element text should be  ${Error_Message_Login}  Incorrect username/password.

Verify Card titles in the Shop page
   @{expectedList} =    Create List     iphone X    Samsung Note 8    Nokia Edge     Blackberry
   ${elements} =    Get Webelements     ${Card_title}
   @{actualList} =      Create List

   FOR  ${element}  IN   @{elements}
       Log   ${element.text}
       Append To List       ${actualList}    ${element.text}

   END
   Lists Should Be Equal    ${expectedList}     ${actualList}


Select the Card
    [arguments]     ${cardName}
    ${elements} =    Get WebElements     css:.card-title
    ${index}=   Set Variable    1
    FOR  ${element}  IN     @{elements}
          Exit For Loop If    '${cardName}' == '${element.text}'
          ${index}=  Evaluate   ${index} + 1
    END
    Click Button    xpath:(//*[@class='card-footer'])[${index}]/button

Fill the login Details and Loging Form
    Input Text          id:username      rahulshettyacademy
    Input Password      id:password    larning
    click Element       css:input[value='user']
    wait until element is visible       css:.modal-body
    click button      id:okayBtn
    click button      id:okayBtn
    wait until element is Not visible     css:.modal-body
    select from list by value   css:select.form-control   teach

