"""

import requests

tinderAPi_Url = "https://api.gotinder.com/v3/auth/login?locale=en-GB"

payload =  {
    
}
"""

#Requests Kütüphanesini tanımlayalım

import requests

# Telefon doğrulama postu için gerekli bilgileri tanımlayın
url = 'https://api.gotinder.com/v3/auth/login?locale=en-GB'
data = {
    'phone_number': '+90 534 633 09 53',
    
}

# Post isteğini gönderir
response = requests.post(url, data=data)

# Sonuçları kontrol eder
if response.status_code == 200:
    print('Telefon doğrulama postu başarıyla gönderildi!')
else:
    print('Telefon doğrulama postu gönderilemedi.')