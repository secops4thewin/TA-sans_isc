# TA-sans_isc

This app  was created to allow  Security team to query SANS ISC APIs as an adaptive response action.  These APIs allow you to progrmatically query fields and provide additional context whilst you are threat hunting.

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

Have issues?
Submit to https://github.com/secops4thewin/TA-sans_isc

Example Output - IP
<ip>
 <number>1.85.2.119</number>
 <count>9843</count>
 <attacks>34</attacks>
 <maxdate>2015-11-12</maxdate>
 <mindate>2015-10-08</mindate>
 <updated>2015-11-12 14:03:22</updated>
 <comment/>
 <asabusecontact>anti-spam@ns.chinanet.cn.net</asabusecontact>
 <as>4134</as>
 <asname>CHINANET-BACKBONE No.31,Jin-rong Street</asname>
 <ascountry>CN</ascountry>
 <assize>108902447</assize>
 <network>1.80.0.0/13</network>
 <threatfeeds>
  <blocklistde110>
   <lastseen>2015-11-11</lastseen>
   <firstseen>2015-09-22</firstseen>
  </blocklistde110>
  <blocklistde143>
   <lastseen>2015-11-11</lastseen>
   <firstseen>2015-09-22</firstseen>
  </blocklistde143>
  <blocklistde25>
   <lastseen>2015-11-11</lastseen>
   <firstseen>2015-09-22</firstseen>
  </blocklistde25>
  <blocklistde993>
   <lastseen>2015-11-11</lastseen>
   <firstseen>2015-09-22</firstseen>
  </blocklistde993>
  <blocklistdecourierimap>
   <lastseen>2015-11-11</lastseen>
   <firstseen>2015-09-22</firstseen>
  </blocklistdecourierimap>
  <forumspam>
   <lastseen>2014-05-30</lastseen>
   <firstseen>2013-01-05</firstseen>
  </forumspam>
  <openbl_smtp>
   <lastseen>2015-11-11</lastseen>
   <firstseen>2015-09-27</firstseen>
  </openbl_smtp>
 </threatfeeds>
</ip>

Example Output - Port
<port>
 <number>80</number>
 <data>
  <date>2011-08-03</date>
  <records>183473</records>
  <targets>29763</targets>
  <sources>7565</sources>
  <tcp>152255</tcp>
  <udp>151</udp>
  <datein>2011-08-03</datein>
  <portin>80</portin>
 </data>
 <services>
  <udp>
   <service>www</service>
   <name>World Wide Web HTTP</name>
  </udp>
  <tcp>
   <service>www</service>
   <name>World Wide Web HTTP</name>
  </tcp>
 </services>
</port>


Example Output - ASN
<asnum>
<data>
<number>4837</number>
<ip>222.141.119.085</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-25 10:57:57</updated>
</data>
<data>
<number>4837</number>
<ip>222.140.087.140</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-25 10:58:30</updated>
</data>
<data>
<number>4837</number>
<ip>222.137.179.118</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-25 11:04:49</updated>
</data>
<data>
<number>4837</number>
<ip>221.147.159.136</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-25 15:45:12</updated>
</data>
<data>
<number>4837</number>
<ip>221.144.181.165</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-25 15:45:05</updated>
</data>
<data>
<number>4837</number>
<ip>221.144.181.093</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-25 15:44:56</updated>
</data>
<data>
<number>4837</number>
<ip>221.144.090.078</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-25 15:14:48</updated>
</data>
<data>
<number>4837</number>
<ip>221.143.158.236</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-26 03:19:27</updated>
</data>
<data>
<number>4837</number>
<ip>221.143.042.133</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-26 03:34:26</updated>
</data>
<data>
<number>4837</number>
<ip>221.141.106.246</ip>
<reports>0</reports>
<targets>0</targets>
<firstseen/>
<lastseen/>
<updated>2017-07-26 03:22:09</updated>
</data>
</asnum>
