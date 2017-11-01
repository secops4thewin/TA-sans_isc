
# encoding = utf-8
#Reference Code Created from http://dev.splunk.com/view/addon-builder/SP-CAAAFBU
#Create URL Function
def query_url(helper, ip_lookup, themethod):
    #Import Necessary Modules
    import json
    import re, urllib
    from httplib2 import Http
    
    #Validate the IP Address parameter exists
    if not ip_lookup:
        helper.log_error('Some parameters are missing. The required are: IP Address.')
        return
  
    #Check for valid IP Address and log if invalid
    pattern=re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    if not pattern.match(ip_lookup):
        helper.log_error('Invalid IP Address')
    
    #Create the URI String that looks for the IP Address
    uri = 'https://isc.sans.edu/api/ip/{}?json'.format(ip_lookup)
    #Build HTTP Connection
    http = helper.build_http_connection(helper.proxy, timeout=30)
  
    #Create Empty Header Values
    headers = {
    #'header1' : 'header_value'
    }
    
    #Create Vars for response header and content as a result of the request
    resp_headers, content = http.request(uri, method=themethod, headers=headers)
    #If not a valid status code then throw an error   
    if resp_headers.status not in (200, 201, 204):
        helper.log_error('Failed to query SANS. IP={}, HTTP Error={}, content={}'.format( ip_lookup, resp_headers.status, content))
    else:
        #Grab from the Second Row onwards in order to get rid of data that is not useful
        #content = content.split("\n")[1]
        #Log this data to Splunk
        helper.log_info('Successfully queried IP={}, content={}'.format(ip_lookup, content))
        #Return the Content
        contentOut = {}
        contentOut['ip'] = { key:value for (key,value) in json.loads(content).get('ip').items() if value is not None } 
        return json.dumps(contentOut)

def process_event(helper, *args, **kwargs):
    #Import Necessary Modules
    import urllib
    #Check for global setting of index
    index = helper.get_global_setting("index") 
    #Log that alert action is starting
    helper.log_info("Alert action sans_ip_lookup started.")
    #Check to see if the index is the default index, this should be changed.
    if "main" in index:
        helper.log_info("Warning: Alert action sans_ip_lookup sending data to main index, you should change this.")
    
    #query the url from setup
    helper.log_info("Alert action IP Lookup Started.")
    #Get the passed param of ip_lookup
    ip = helper.get_param("ip_lookup")
    #Log the IP Address number into Splunk
    helper.log_info("IP Address={}".format(ip))
    #query API Key alert action input
    
    #call the query URL REST Endpoint and pass the url
    content = query_url(helper, ip, 'GET')  

    #write the response returned to splunk index
    helper.addevent(content, sourcetype="sansisc:ip_json")
    helper.writeevents(index=str(index), host="arf", source="sansisc")
    return 0
