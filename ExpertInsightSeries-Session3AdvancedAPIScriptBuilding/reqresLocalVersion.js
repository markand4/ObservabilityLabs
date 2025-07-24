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

// FOR LOCAL: Use got library
import got from 'got';
import assert from 'assert';

// FOR APPDYNAMICS: Use the built-in libraries instead:
// const assert = require('assert');
// Note: 'client' is provided by AppDynamics, no need to require it

(async function () {
// FOR APPDYNAMICS: Remove async function wrapper
  try {
    // --- Step 1: Reqres Login (POST /api/login) ---
    
    // FOR LOCAL: Use got.post
    const loginResponse = await got.post('https://reqres.in/api/login', {
    // FOR APPDYNAMICS: Use client.post instead
    // const loginResponse = await client.post('https://reqres.in/api/login', {
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1'
      },
      json: {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
      },
      // FOR LOCAL: Need responseType for got
      responseType: 'json'
      // FOR APPDYNAMICS: Remove responseType, then add .json() method
    }).json();
    // FOR APPDYNAMICS: Add .json() method here

  
    // Extract token
    const token = loginResponse.token;
    console.log('Login successful, token received:', token);
    // FOR APPDYNAMICS: Same token extraction

    // --- Step 2: Reqres Get User (GET /api/users/2) ---
    // FOR LOCAL: Use got.get
    const getUserResponse = await got.get('https://reqres.in/api/users/2', {
    // FOR APPDYNAMICS: Use client.get instead
    // const getUserResponse = await client.get('https://reqres.in/api/users/2', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'x-api-key': 'reqres-free-v1'
      },
      // FOR LOCAL: Need responseType for got
      responseType: 'json'
      // FOR APPDYNAMICS: Remove responseType, then add .json() method
    }).json();
    // FOR APPDYNAMICS: Add .json() method here

    // Assert user retrieval successful
    assert.equal(getUserResponse.data.id, 2, "Unexpected user ID");
    // FOR APPDYNAMICS: Same assertion works

    // --- Step 3: Reqres Get User Fail (GET /api/users/23) ---
    // For AppDynamics, we'll make the request and check the response
    // FOR LOCAL: Use got.get (without .json() to access statusCode)
    const getUserFailResponse = await got.get('https://reqres.in/api/users/23', {
    // FOR APPDYNAMICS: Use client.get instead
    // const getUserFailResponse = await client.get('https://reqres.in/api/users/23', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'x-api-key': 'reqres-free-v1'
      },
      // FOR LOCAL: Need responseType for got  
      responseType: 'json',
      // FOR APPDYNAMICS: Remove responseType and throwHttpErrors
      throwHttpErrors: false // Don't throw on 4xx/5xx for local testing
      // FOR APPDYNAMICS: Remove throwHttpErrors, client handles this differently
    });
    
    // AppDynamics client returns status code in the response object
    assert.equal(getUserFailResponse.statusCode, 404, "Get User Fail: Expected 404");
    // FOR APPDYNAMICS: Same assertion works

    // --- Step 4: Reqres Get User Delay (GET /api/users?delay=3) ---
    // FOR LOCAL: Use got.get
    const getUserDelayResponse = await got.get('https://reqres.in/api/users?delay=3', {
    // FOR APPDYNAMICS: Use client.get instead
    // const getUserDelayResponse = await client.get('https://reqres.in/api/users?delay=3', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'x-api-key': 'reqres-free-v1'
      },
      // FOR LOCAL: Need responseType for got
      responseType: 'json'
      // FOR APPDYNAMICS: Remove responseType, then add .json() method
    }).json();
    // FOR APPDYNAMICS: Add .json() method here

    // Assert delayed user retrieval successful
    assert(getUserDelayResponse.data, "Get User Delay failed: No data received");
    // FOR APPDYNAMICS: Same assertion works

    // FOR LOCAL: Use console.log
    console.log('Login successful, token received');
    console.log('Get User successful:', getUserResponse.data.email);
    console.log('Get User Delay successful, received', getUserDelayResponse.data.length, 'users');
    console.log('All tests passed successfully!');
    // FOR APPDYNAMICS: Same console.log statements work

  } catch (error) {
    // FOR LOCAL: Use console.error
    console.error('Test failed:', error.message);
    // FOR APPDYNAMICS: Same console.error works
    
    // FOR LOCAL: Use process.exit for local testing
    process.exit(1);
    // FOR APPDYNAMICS: Use throw error instead
    // throw error; // Let AppDynamics handle the failure
  }
})();
// FOR APPDYNAMICS: Remove the async function wrapper entirely

/*
SUMMARY OF CHANGES NEEDED FOR APPDYNAMICS:

1. Remove: import statements
2. Add: const assert = require('assert');
3. Replace: got.post/got.get with client.post/client.get
4. Add: .json() method calls for parsed responses
5. Remove: responseType: 'json' options
6. Remove: throwHttpErrors: false option
7. Replace: process.exit(1) with throw error
8. Remove: async function wrapper
9. Keep: console.log/console.error (they work in AppDynamics)
10. Keep: All assertions (they work the same way)
*/