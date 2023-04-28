import geocoder
import folium

class DetectAddress():
    def __init__(self,address):
        self.address = address
    def detectLocation(self):
        try:
            # Use geocoder to get the latitude and longitude of the IP address
            g = geocoder.ip(ip_address)
            latitude, longitude = g.latlng
            # Create a folium map centered at the location of the IP address
            map_ip = folium.Map(location=[latitude, longitude], zoom_start=13)
            # Add a marker at the location of the IP address
            folium.Marker([latitude, longitude]).add_to(map_ip)
            map_ip.save("meramap.html")
            print("Program successfully executed!!\nNow move to html file and check your location.")
        except:
            print("Sorry, An error occurred")


ip_address = str(input("Enter the IP address you wish to locate on maps without quotes: "))
My_IP = DetectAddress(ip_address)
My_IP.detectLocation()
