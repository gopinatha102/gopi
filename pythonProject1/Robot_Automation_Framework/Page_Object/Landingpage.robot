*** Settings ***
Documentation   All the page objects and keywords of landing page
Library         SeleniumLibrary


*** Variable ***
#${Shop_page_load}           css:.nav-link
${Error_Message_Login}      css:.alert-danger

*** Keywords ***

Fill the login Form
    [arguments]     ${username}     ${password}
    INPUT TEXT      id:username    ${username}
    INPUT PASSWORD  id:password    ${password}
    click button    id:signInBtn

*** Keywords ***
wait untile Element is located in the page
    wait until element passed is located on Page   ${Error_Message_Login}

verify error message is correct
    ${result}=  Get Text    ${Error_Message_Login}
    Should Be Equal As Strings   ${result}      Incorrect username/password.
    Element text should be  ${Error_Message_Login}  Incorrect username/password.

Fill the login Details and Loging Form
    Input Text          id:username      rahulshettyacademy
    Input Password      id:password    larning
    click Element       css:input[value='user']
    wait until element is visible       css:.modal-body
    click button      id:okayBtn
    click button      id:okayBtn
    wait until element is Not visible     css:.modal-body
    select from list by value   css:select.form-control   teach

