import requests


origin = input('საიდან:')
destination = input('სად:')

url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}' \
      f'&destination={destination}&key=AIzaSyBQs3__s41n6DzOfVq-z7G5jlYxbPShEOY'

r = requests.get(url=url)

distance = r.json()['routes'][0]['legs'][0]['distance']['text']
duration = r.json()['routes'][0]['legs'][0]['duration']['text']
print(f'{origin}-დან {destination}-მდე მანძილი: {distance}'
      .replace('km', 'კმ'))
print(f'ავტომობილით მგზავრობის სავარაუდო დრო: {duration}'
      .replace('day', 'დღე').replace('hours', 'საათი'))
