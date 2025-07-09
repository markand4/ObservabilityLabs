Expert Insight Series Session 2: Advanced Browser Synthetic Script 🧪

Welcome to Session 2 of our Expert Insight Series on Synthetics! In this lab, you'll learn how to create and debug an advanced browser synthetic script using Python and Selenium, including error handling, assertions, and multi-step user flows.

🎥 Video Tutorial

▶️ [Watch the Session 2 Video Here]()

🛠 Prerequisites

Before starting this lab, make sure you have the following installed and set up:

- [Python 3.7+](https://www.python.org/downloads/)  
  Ensure Python is installed and added to your system's PATH.
- [pip](https://pip.pypa.io/en/stable/installation/)  
  Python's package manager for installing dependencies.
- [Selenium Package](https://pypi.org/project/selenium/)  
  Install Selenium using pip:
  ```bash
  pip install selenium
  ```
- [Download ChromeDriver Package](https://pypi.org/project/chromedriver-py/)  
  ```bash
  pip install chromedriver-py
  ```
- [IDE or Code Editor](https://code.visualstudio.com/)  
  Use an IDE like Visual Studio Code or PyCharm for coding and debugging.
- [AppDynamics Synthetic Monitoring License](https://docs.appdynamics.com/appd/24.x/latest/en/splunk-appdynamics-licensing/license-entitlements-and-restrictions)

Ensure your AppDynamics account includes synthetic monitoring capabilities.

🚀 Objectives

By the end of this lab, you will:

- Write an advanced Browser Synthetic Monitoring script using Python and Selenium.
- Handle login errors and verify error messages.
- Perform multi-step user flows (login, add to cart, checkout).
- Use assertions to validate UI elements and business logic.
- Capture screenshots for both success and error scenarios.
- Debug and validate your script locally.
- Upload the script to AppDynamics for synthetic monitoring.
- Configure and test the synthetic monitor in AppDynamics.

🔧 Steps to Complete the Lab

1. Clone the Repository

   ```bash
   git clone https://github.com/markand4/ObservabilityLabs.git
   cd ObservabilityLabsYoutube/ObservabilityLabs/ExpertInsightSeries-Session2:AdvancedBRUMScriptBuilding
   ```

2. Set Up Your Environment

   Verify Python installation:
   ```bash
   python --version
   # Ensure it’s version 3.7 or higher.
   ```

   Install the Selenium package:
   ```bash
   pip install selenium
   ```

   Download and configure the WebDriver:
   ```bash
   pip install chromedriver-py
   ```

3. Review and Run the Script

   Open [`EIS2-BrowserScript.py`](EIS2-BrowserScript.py) in your IDE.

   - The script demonstrates:
     - Attempting login with a locked-out user and verifying the error message.
     - Logging in with a valid user.
     - Adding multiple items to the cart and verifying their presence.
     - Checking product prices and details.
     - Completing the checkout process.
     - Taking screenshots for both error and success states.

   Run the script locally and check for any errors or screenshots generated (`success.png`, `UserLoginError.png`, etc.).

4. Upload the Script to AppDynamics

   - Log in to your AppDynamics Controller.
   - Navigate to Synthetic Jobs.
   - Select "Create a New Synthetic Job".
   - Upload your Python script to the job configuration.
   - Set up monitoring intervals, locations, and other configurations.
   - Save and activate the synthetic job.

5. Test Your Script in AppDynamics

   - Run the synthetic job in AppDynamics.
   - Monitor results:
     - Verify if the script runs successfully.
     - Check for any failed steps or errors in the synthetic job logs.
     - Debug and optimize the script as needed.

6. Import the Dashboard JSON into AppDynamics Dashboard Studio

   - Log in to your AppDynamics Controller.
   - In the left navigation, go to **Dashboards & Reports**.
   - Click on Dash Studio 
   - Click **Import** and select Browser Synthetic Monitoring Dashboard (Expert Insight Series).json
   - Save the dashboard.

   The dashboard provides visual insights into your synthetic monitor's performance and results.

📢 Need Help?

If you encounter issues or have questions, feel free to:

- Open an issue: [GitHub Issues](../../issues)
- Join the discussion: [GitHub Discussions](../../discussions)

✨ Features of This Lab

- Advanced hands-on experience with Splunk AppDynamics Synthetics.
- Practical debugging techniques for browser scripts.
- Robust error handling and validation.
- Reusable script templates for future projects.

📜 License

This lab is part of the ObservabilityLabs repository and is licensed under the [Apache License 2.0](../../LICENSE).

📬 Stay Connected

Subscribe to our [Cisco Observability YouTube Channel](https://www.youtube.com/@CiscoObservability) for more tutorials and labs.  
Follow this repository for updates on new labs and features.

Let’s build something amazing together! 🚀
