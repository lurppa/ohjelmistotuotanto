*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kela  salasana9
    Output Should Contain  New user registered 

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 letters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  123  kalle123
    Output Should Contain  Username can only contain letters from lower case English alphabet

Register With Valid Username And Too Short Password
    Input Credentials  kela  salasa8
    Output Should Contain  Password must be at least 8 letters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kela  salasanasala
    Output Should Contain  Password must include one non-letter

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command

