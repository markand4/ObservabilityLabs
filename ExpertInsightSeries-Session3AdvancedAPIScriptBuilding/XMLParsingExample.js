// -*- coding: utf-8 -*-
// Date: 07/21/2025
// Description: This sample script is a framework and intro API synthetic script that you can use to help you learn API synthetics for Splunk AppDynamics
// Author: Mark Kurpiel
//
// Disclaimer
// Cisco (Splunk AppDynamics)/CSS provides this extension script "as is" without warranties, express or implied.
// Use this script at your own risk. Cisco (Splunk AppDynamics)/CSS is not responsible for any errors,
// data loss, system malfunctions, or other consequences. The user assumes full responsibility for verifying
// functionality and ensuring compliance. Under no circumstances shall Cisco (Splunk AppDynamics)/CSS be liable
// for any direct, indirect, or consequential damages arising from the use of this script. By using it, the user
// agrees to these terms and releases Cisco (Splunk AppDynamics)/CSS from any claims or liabilities.
//

// Javascript based API Monitoring Test

const assert = require("assert");
const xml2js = require('xml2js');
(async () => {
    var url = "https://www.w3schools.com/xml/simple.xml";
    var response = await client.get(url);
    var data = response.body;
    assert.equal(200, response.statusCode);
    xml2js.parseString(data, function(err, result) {
        console.log(result);
    });
})();