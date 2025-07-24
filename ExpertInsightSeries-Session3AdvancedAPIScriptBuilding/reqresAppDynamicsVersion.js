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


// FOR APPDYNAMICS: Use the built-in libraries instead:
const assert = require('assert');
// Note: 'client' is provided by AppDynamics, no need to require it

(async function () {
  try {
    // --- Step 1: Reqres Login (POST /api/login) ---
    
    // FOR APPDYNAMICS: Use client.post instead of requests.post
    const loginResponse = await client.post('https://reqres.in/api/login', {
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1'
      },
      json: {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
      },
    }).json();

   
    
    // Extract token
    const token = loginResponse.token;
    console.log('Login successful, token received:', token);
    

    // --- Step 2: Reqres Get User (GET /api/users/2) ---
    const getUserResponse = await client.get('https://reqres.in/api/users/2', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'x-api-key': 'reqres-free-v1'
      }
    }).json();

    // Assert user retrieval successful
    assert.equal(getUserResponse.data.id, 2, "Unexpected user ID");

    // --- Step 3: Reqres Get User Fail (GET /api/users/23) ---
    // For AppDynamics, we'll make the request and check the response
    const getUserFailResponse = await client.get('https://reqres.in/api/users/23', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'x-api-key': 'reqres-free-v1'
      }
    });
    
    // AppDynamics client returns status code in the response object
    assert.equal(getUserFailResponse.statusCode, 404, "Get User Fail: Expected 404");

    // --- Step 4: Reqres Get User Delay (GET /api/users?delay=3) ---
    const getUserDelayResponse = await client.get('https://reqres.in/api/users?delay=3', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'x-api-key': 'reqres-free-v1'
      }
    }).json();

    // Assert delayed user retrieval successful
    assert(getUserDelayResponse.data, "Get User Delay failed: No data received");

    // FOR APPDYNAMICS: Use console.log (logger may not be available in all environments)
    console.log('Login successful, token received');
    console.log('Get User successful:', getUserResponse.data.email);
    console.log('Get User Delay successful, received', getUserDelayResponse.data.length, 'users');
    console.log('All tests passed successfully!');

  } catch (error) {
    console.error('Test failed:', error.message);
    throw error; // Let AppDynamics handle the failure
  }
})();