
# encoding = utf-8
#Reference Code Created from http://dev.splunk.com/view/addon-builder/SP-CAAAFBU
#Create URL Function

def query_url(helper, port_number, themethod):
    #Import Necessary Modules
    import json
    import re, urllib
    from httplib2 import Http
    
    #Validate the Port Number parameter exists
    if not port_number:
        helper.log_error('Some parameters are missing. The required are: IP Address.')
        return
  
    #Check for valid Port number and log if invalid
    pattern=re.compile("\d{1,6}")
    
    if not pattern.match(port_number):
        helper.log_error('Invalid Port Number')
    #Create the URI String that looks for the port
    uri = 'https://isc.sans.edu/api/port/' + port_number
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
        helper.log_error('Failed to query SANS. Port={}, HTTP Error={}, content={}'.format( port_number, resp_headers.status, content))
    else:
        #Grab from the Second Row onwards in order to get rid of data that is not useful and join the rows with a space
        content = str(" ".join(content.split("\n")[1:]))
        #Log this data to Splunk
        helper.log_info('Successfully queried Port={}, content={}'.format(port_number, content))
        #Return the Content
        return content

def process_event(helper, *args, **kwargs):
    #Import Necessary Modules
    import urllib
    #Check for global setting of index
    index = helper.get_global_setting("index") 
    #Log that alert action is starting
    helper.log_info("Alert action sans_port_lookup started.")
    #Check to see if the index is the default index, this should be changed.
    if "main" in index:
        helper.log_info("Warning: Alert action sans_port_lookup sending data to main index, you should change this.")
    
    #query the url from setup
    helper.log_info("Alert action Port Lookup Started.")
    #Get the passed param of port
    port = helper.get_param("port")
    #Log the Port number into a log file
    helper.log_info("Port Number={}".format(port))
    
    #call the query URL REST Endpoint and pass the url
    content = query_url(helper, port, 'GET')  

    #write the response returned to splunk index
    helper.addevent(content, sourcetype="sansisc:port")
    helper.writeevents(index=str(index), host="arf", source="sansisc")
    return 0
