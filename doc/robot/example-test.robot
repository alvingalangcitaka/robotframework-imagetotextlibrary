*** Setting ***
Library     ImageToTextLibrary
Library     BuiltIn

*** Test Cases ***
Get Image Text Example
    ${text}=            Get Text From Image         ${CURDIR}/sample-image.png
    Log                 ${text}
    Should Contain      ${text}                     Directory Layout
