from cryptographyFramework import *

initializeWrite()
user = "luis"
password = "luis123"
encryptedText = encryptMessage(user, password, "Dianhos e Tchainas")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Tchucas e Mandruvos")
saveNewLine(encryptedText)

