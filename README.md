SANS ISC Adaptive Response Action


This app was created to allow Security team to query SANS ISC APIs as an adaptive response action.  These APIs allow you to programmatically query fields and provide additional context whilst you are threat hunting.

Subscribe to the Stormcenter Podcast!
ITunes
https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?id=304863991

Google Play
https://play.google.com/music/listen?t=SANS_Internet_Storm_Center_Daily_Network_Security_and_Information_Security_Podcast&view=/ps/Iwyezwxzllryi4ho4r4jprvhp2y

The API Reference is located at https://isc.sans.edu/api/

The three APIs that you can query are IP, Port and ASN

Steps to install
Download from Splunkbase 
Create a new index if need be.  In my examples I created a new index called osint_data
Install the App
After installation go to https://your.splunk.address/en-GB/app/TA-sans_isc/configuration
If you have a proxy configure it under the proxy settings
If you want to change logging settings click logging
Click Add-On Settings - Specify the index name that you created before
Configure the index macro `sans_index` by copying macros.conf to a local folder within the app. This should be the index you configured in teh step above.

Have issues?

Requires Splunk Common Information Model App if you do not Enterprise Security
https://splunkbase.splunk.com/app/1621/

Submit to https://github.com/secops4thewin/TA-sans_isc

The use of the APIs of SANS Internet Storm Center are subject to the terms and conditions set out by SANS Internet Storm Center

