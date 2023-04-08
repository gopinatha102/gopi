*** Setting ***
Documentation  To validate the Login from
Library  SeleniumLibrary
Library  Collections
Library  ../CustomLibraries/Shop.py
Test Setup      Open the browser with the Mortgage payment url
Test Teardown    Close Browser session
Resource    ../Page_Object/Generic.robot
Resource    ../Page_Object/Landingpage.robot
Resource    ../Page_Object/Shoppage.robot

*** Variable ***
@{listofProducts}           Blackberry      Nokia Edge

*** Test Cases ***
Validate UnSuccesful Login
    Landingpage.Fill the login Form      ${user_name}      ${Invalid_password}
    Landingpage.wait untile Element is located in the page
    Landingpage.verify error message is correct

Validate Cards display in the Shopping Page
    Landingpage.Fill the login Form     ${user_name}    ${valid_password}
    Shoppage.wait untile Element is located in the page
    Shoppage.Verify Card titles in the Shop page
    add items to cart and checkout  ${listofProducts}


    #Select the Card    Nokia

Select the From and navigate to Child window
   Landingpage.Fill the login Details and Loging Form



