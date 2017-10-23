
# encoding = utf-8

#Reference Code Created from http://dev.splunk.com/view/addon-builder/SP-CAAAFBU
#Create URL Function
def query_url(helper, asn_number, themethod):
    #Import Necessary Modules
    import json
    import re, urllib
    from httplib2 import Http
    
    #Validate the ASN Number parameter exists
    if not asn_number:
        helper.log_error('Some parameters are missing. The required are: ASN.')
        return
  
    #Check for valid ASN and log if invalid
    pattern=re.compile("\d{1,6}")
    if not pattern.match(asn_number):
        helper.log_error('Invalid ASN Number')
    #Create the URI String that looks for the ASN
    uri = 'https://isc.sans.edu/api/asnum/100/{}?json'.format(asn_number)
    
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
        helper.log_error('Failed to query SANS. ASN={}, HTTP Error={}, content={}'.format( asn_number, resp_headers.status, content))
    else:
        #Grab from the Second Row onwards in order to get rid of data that is not useful and join the rows with a space
        #Log this data to Splunk
        helper.log_info('Successfully queried ASN={}, content={}'.format(asn_number, content))
        contentOut = []
        contentJSON = json.loads(content) 
        helper.log_info("content leng:{}".format(len(contentOut)))
        for event in contentJSON:
            tempContent = { key:value for (key,value) in event.items() if value is not None }
            contentOut.append(json.dumps({'asn':tempContent}))
        #Return the Content
        helper.log_info("ContentOUT: {}".format(contentOut))
        return contentOut

def process_event(helper, *args, **kwargs):
    #Import Necessary Modules
    import urllib
    #Check for global setting of index
    index = helper.get_global_setting("index") 
    #Log that alert action is starting
    helper.log_info("Alert action sans_asn_lookup started.")
    
    #Check to see if the index is the default index, this should be changed.
    if "main" in index:
        helper.log_info("Warning: Alert action sans_asn_lookup sending data to main index, you should change this.")

    #query the url from setup
    helper.log_info("Alert action ASN Lookup Started.")
    #Get the passed param of ASN
    asn = helper.get_param("asn")
    #Log the ASN number into a log file
    helper.log_info("ASN={}".format(asn))
    
    #call the query URL REST Endpoint and pass the url
    content = query_url(helper, asn, 'GET')  
    for event in content:
        #write the response returned to splunk index
        helper.addevent(event, sourcetype="sansisc:asn")
    helper.writeevents(index=str(index), host="arf", source="sansisc")
    return 0
