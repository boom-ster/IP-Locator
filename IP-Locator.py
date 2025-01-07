import requests
import webbrowser                               #neccessary dependencies to make requests and queries and to open a url in default web browser


def ip_locate(ip):                                                                  #function to fetch ip information from the api
    response = requests.get(f"http://ip-api.com/json/{ip}").json()                  #query sent to the api for performing the search

    chk_status = response.get("status")                                             #checking the status of the response
    if(chk_status == 'success'):
        ip_info = {
            "ip": ip,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country"),
            "status": response.get("status")}                                                   #extracting the relevent information from the api response
        
        latitude = response.get("lat")                                                          #extracting latitude and longitude information for opening the location on the map
        longitude = response.get("lon")

        if latitude and longitude:
            url = f"https://www.google.com/maps/place/{latitude},{longitude}"                   #using the latitude and longitude as an input to google maps to make a query through webbrowser
            webbrowser.open(url)
            return ip_info;                                                                     #returning the relevent ip information

        else:
            print("Failed to open location on map")                                             #if map fails to open, only providing the information to user
            return ip_info
        
    
    else:
        return "Failed to retrieve info. Please make sure you used a correct IPv4 address to perform the search."
    
        
def batch_ip_locate(ip_list):                           #function to provide support for batch IP lookup
    result=[]
    for ip in ip_list:
        ip_info = ip_locate(ip)                         #calling the ip_locate function to perform the IP lookup
        result.append(ip_info)                          #appending the response from the api to the list
    return result                                       #returning the list as a result


def search():

    print("\n")
    searches = int(input("Enter no. of IP Address(es) you want to locate: "))       #input of no. of searches

    ip_list = []                                                                    #list to save the number of IPs passed as an input
    for _ in range(searches):                                                       
        ip_list.append(input("Enter a valid IPv4 address: "))                                         #list to save all the IPs provided to perform IP lookup

    ip_list_info = batch_ip_locate(ip_list)                                         #variable to save all the information provided by the api
    for ip_info in ip_list_info:
        print(ip_info)                                                              #display all the information recieved
    exit()
    
def exit():
    exit = (input("Do you want to exit? (Y/N): \n"))
    if(exit == "Y" or exit == "y"):
        return
    elif(exit == "N" or exit == "n"):
        search()
    else:
        print("INVALID INPUT.")

search()