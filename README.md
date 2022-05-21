## Simple MQTT Client and Broker

### MQTT Client is based on paho-mqtt

pip install paho-mqtt

### MQTT Broker is based on hbmqtt

pip install hbmqtt


### Broker config

config = {

    'listeners': {
    
        'default': {
        
            'type': 'tcp',
            
            'bind': '192.168.55.105:9999',
            
            'max-connections': 50,
            
        },
        
    },
    
    'sys_interval': 90,
    
    'timeout-disconnect-delay': 300, # in seconds before broker kicks-off the client
    
    'topic-check': {
    
        'enabled': True,
        
        'plugins': ['topic_taboo'],
        
    }
    
}
