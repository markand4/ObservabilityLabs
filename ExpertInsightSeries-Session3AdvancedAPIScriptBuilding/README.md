# Expert Insight Series Session 3: Advanced API Script Building 🔧

Welcome to Session 3 of our Expert Insight Series on Synthetics! In this lab, you'll learn how to create and deploy advanced API synthetic monitoring scripts using JavaScript, including encryption, XML processing, and authentication flows.

## 🎥 Video Tutorial

▶️ [Watch the Session 3 Video Here]()

## 🛠 Prerequisites

Before starting this lab, make sure you have the following installed and set up:

- [Node.js 16+](https://nodejs.org/downloads/)  
  Ensure Node.js is installed and added to your system's PATH.
- [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)  
  Node.js package manager for installing dependencies.
- [IDE or Code Editor](https://code.visualstudio.com/)  
  Use an IDE like Visual Studio Code for coding and debugging.
- [AppDynamics Synthetic Monitoring License](https://docs.appdynamics.com/appd/24.x/latest/en/splunk-appdynamics-licensing/license-entitlements-and-restrictions)
- [got library](https://www.npmjs.com/package/got) (for local testing only)

Ensure your AppDynamics account includes synthetic monitoring capabilities.

## 🚀 Objectives

By the end of this lab, you will:

- Create advanced API Synthetic Monitoring scripts using JavaScript.
- Implement JWT/JWE encryption and decryption for secure API testing.
- Parse and validate XML responses from web services.
- Handle authentication flows and error scenarios.
- Use assertions to validate API responses and business logic.
- Debug and validate scripts locally before deployment.
- Upload scripts to AppDynamics for continuous monitoring.
- Configure synthetic monitors with proper intervals and locations.

## 📁 Lab Files Overview

This lab contains several JavaScript files for different use cases:

### For AppDynamics Deployment:
- **`reqresAppDynamicsVersion.js`** - Basic API authentication and user management testing
- **`JWEEncryption&DecryptionExample.js`** - JWT/JWE encryption demonstration with security validation
- **`XMLParsingExample.js`** - XML response parsing and validation

### For Local Development & Testing:
- **`reqresLocalVersion.js`** - Local version of API testing with got library for debugging

## 🔧 Steps to Complete the Lab

### 1. Clone the Repository

```bash
git clone https://github.com/markand4/ObservabilityLabs.git
cd ObservabilityLabsYoutube/ObservabilityLabs/ExpertInsightSeries-Session3AdvancedAPIScriptBuilding
```

### 2. Set Up Local Environment (for reqresLocalVersion.js only)

For local testing and debugging of the `reqresLocalVersion.js` script:

```bash
# Initialize npm project
npm init -y

# Install dependencies for local testing
npm install got@11

# Add ES module support to package.json
echo '{"type": "module"}' > package.json
```

Create a `.vscode/launch.json` file for debugging:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Local API Script",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/reqresLocalVersion.js",
      "console": "integratedTerminal",
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

### 3. Local Testing & Debugging

**For `reqresLocalVersion.js` ONLY:**

1. **Open the file** in VS Code
2. **Set breakpoints** by clicking in the left margin
3. **Press F5** to start debugging
4. **Step through the code** using F10 (step over) and F11 (step into)
5. **Inspect variables** in the Variables panel
6. **Use the Debug Console** to test expressions

```bash
# Run the local script directly
node reqresLocalVersion.js
```

### 4. Deploy Scripts to AppDynamics

**For ALL OTHER scripts** (`reqresAppDynamicsVersion.js`, `JWEEncryption&DecryptionExample.js`, `XMLParsingExample.js`):

#### 4.1 Upload to AppDynamics

1. **Log in to your AppDynamics Controller**
2. **Navigate to Synthetic Jobs**
3. **Click "Create a New Synthetic Job"**
4. **Select "Script" as the job type**
5. **Choose "JavaScript" as the script language**
6. **Copy and paste your script content** (or upload the file)

#### 4.2 Script-Specific Configuration

**For `reqresAppDynamicsVersion.js`:**
- **Purpose:** Basic API authentication testing
- **Monitors:** Login flow, user retrieval, error handling
- **Interval:** Every 5-15 minutes
- **Locations:** Multiple geographic locations

**For `JWEEncryption&DecryptionExample.js`:**
- **Purpose:** JWT/JWE encryption security testing
- **Monitors:** Encryption/decryption performance, security validation
- **Interval:** Every 30 minutes (more resource intensive)
- **Locations:** Primary data center locations
- **Note:** Requires jose library support in AppDynamics

**For `XMLParsingExample.js`:**
- **Purpose:** XML web service testing
- **Monitors:** XML response validation, parsing performance
- **Interval:** Every 10 minutes
- **Locations:** Regions where XML services are used

#### 4.3 Configure Monitoring Settings

For each script:
1. **Set monitoring intervals** based on criticality
2. **Select geographic locations** for testing
3. **Configure alerting thresholds**
4. **Set up notification channels**
5. **Enable data collection** for performance metrics

### 5. Test Your Scripts in AppDynamics

1. **Run each synthetic job** manually first
2. **Monitor results** in the Synthetic Jobs dashboard:
   - Verify successful execution
   - Check response times and performance
   - Review any failed steps or errors
   - Validate assertions and business logic
3. **Debug and optimize** as needed

### 6. Import Dashboard for Monitoring

1. **Log in to your AppDynamics Controller**
2. **Navigate to Dashboards & Reports**
3. **Click on Dashboard Studio**
4. **Click Import** and select `API Synthetic Monitoring Dashboard (Expert Insight Series).json`
5. **Save the dashboard**

The dashboard provides visual insights into:
- API response times and availability
- Encryption/decryption performance
- XML parsing success rates
- Geographic performance variations
- Error trends and patterns

## 📊 Script Descriptions

### reqresAppDynamicsVersion.js
**Functionality:**
- User authentication flow testing
- API endpoint validation
- Error handling for 404 responses
- Token-based authorization testing
- Multi-step API workflows

**Key Features:**
- Login with credentials
- User data retrieval
- Error scenario testing
- Delayed response handling

### JWEEncryption&DecryptionExample.js
**Functionality:**
- JWT/JWE token creation and validation
- Encryption algorithm testing
- Security compliance verification
- Performance benchmarking

**Key Features:**
- Multiple encryption algorithms
- Token expiration validation
- Security claim verification
- Performance timing tests

### XMLParsingExample.js
**Functionality:**
- XML web service response parsing
- Data structure validation
- XML format compliance checking

**Key Features:**
- XML response parsing
- Structure validation
- Error handling for malformed XML

### reqresLocalVersion.js (Local Only)
**Functionality:**
- Same as AppDynamics version but with local debugging
- Uses got library for HTTP requests
- Includes detailed debugging comments
- Process exit handling for local testing

## 🔍 Debugging Tips

### Local Development (reqresLocalVersion.js):
- Use VS Code debugger with breakpoints
- Check network connectivity to APIs
- Validate JSON responses in Debug Console
- Test error scenarios manually

### AppDynamics Deployment:
- Check synthetic job logs for detailed errors
- Verify API endpoints are accessible from AppDynamics locations
- Monitor performance metrics for bottlenecks
- Use dashboard visualizations for trend analysis

## 📢 Need Help?

If you encounter issues or have questions:

- **Open an issue:** [GitHub Issues](../../issues)
- **Join the discussion:** [GitHub Discussions](../../discussions)
- **Check AppDynamics documentation:** [Synthetic Monitoring Guide](https://docs.appdynamics.com/synthetic-monitoring/)

## ✨ Features of This Lab

- **Advanced JavaScript synthetic monitoring** with real-world scenarios
- **Encryption and security testing** using industry-standard libraries
- **XML processing capabilities** for legacy system integration
- **Local debugging workflow** for efficient development
- **Production-ready scripts** with comprehensive error handling
- **Performance monitoring** and optimization techniques

## 🏗️ Next Steps

After completing this lab:

1. **Customize scripts** for your specific API endpoints
2. **Implement additional security tests** as needed
3. **Create custom dashboards** for your monitoring requirements
4. **Set up automated alerting** for critical failures
5. **Integrate with CI/CD pipelines** for continuous testing

## 📜 License

This lab is part of the ObservabilityLabs repository and is licensed under the [Apache License 2.0](../../LICENSE).

📬 Stay Connected

Subscribe to our [Cisco Observability YouTube Channel](https://www.youtube.com/@CiscoObservability) for more tutorials and labs.  
Follow this repository for updates on new labs and features.

Let’s build something amazing together! 🚀
