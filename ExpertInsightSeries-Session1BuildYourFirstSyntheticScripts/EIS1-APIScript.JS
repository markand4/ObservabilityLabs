/* -*- coding: utf-8 -*-
    ##Date 06/23/2025
    Description: This sample intro synthetic script that you can use to help you learn browser synthetics for Splunk AppDynamics
    Author: Mark Kurpiel

    ##############################################################################################################
    #Disclaimer
    #Cisco (Splunk AppDynamics)/CSS provides this extension script "as is" without warranties, express or implied.
    #Use this script at your own risk. Cisco (Splunk AppDynamics)/CSS is not responsible for any errors,
    #data loss, system malfunctions, or other consequences. The user assumes full responsibility for verifying
    #functionality and ensuring compliance. Under no circumstances shall Cisco (Splunk AppDynamics)/CSS be liable
    #for any direct, indirect, or consequential damages arising from the use of this script. By using it, the user
    #agrees to these terms and releases Cisco (Splunk AppDynamics)/CSS from any claims or liabilities.
    #
    ############################################################################################################
*/

const assert = require('assert');
(async () => {
const requestURL = new URL("https://api.agify.io");
const options = {};
const headers = {};
headers.Host = requestURL.hostname;
options.headers = headers;
requestURL.searchParams.set('name', 'Mark ');
options.method = 'GET';
const customClientExtendObj = {};
customClientExtendObj.followRedirect = false
const customClient = client.extend(customClientExtendObj)
var response = await customClient(requestURL, options);
console.log(response);
assert(response['statusCode']=='200');
})();

