import requests
import services.rabitmq_functions as rabitmq
import services.redis_functions as redis
#Parameters
URL = 'https://worldtimeapi.org/api/timezone'
HEADERS = {'User-Agent': 'Mozilla'}
    
def main():
    try:
        
        #Get all timezones from the Api
        print("Getting all Timezones..")
        res = requests.get(URL, headers=HEADERS)
        time_zones = res.json()
        print("Getting all Timezones - Done!\n")
        
        #Iterate each timezone, pull data and send to the services       
        print("Sending Time-zones..")
        for time_zone in time_zones:
            try:
                
                print(f'Getting {time_zone} data..')
                res = requests.get(f"{URL}/{time_zone}", headers=HEADERS)
                                
                #Send data               
                redis.send_data_to_redis(time_zone, str(res.json()))
                rabitmq.send_message_to_quaue(str(res.json()))
                
                print(f'{time_zone} has been sent successfully!\n')  
                          
            except Exception as e:
                print(f'Error while iterating on {time_zone}: ' + str(e))
                
        print("Sending Time-zones - Done!\n")       
        print("Finished send-timezones.py script")
    except Exception as e:
        print('Error at main: ' + str(e))  
        exit()         
    
    

    
if __name__ == '__main__':
    main()
    

