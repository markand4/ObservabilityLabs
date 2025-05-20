
Lab 1: Create Your First Browser Synthetic Monitoring Script 🧪

Welcome to Lab 1 of ObservabilityLabs! In this lab, you'll learn how to create a Browser Synthetic Monitoring Script using Python and Selenium, debug it, and upload it to AppDynamics. This step-by-step guide will walk you through the process, ensuring you gain hands-on experience with synthetic monitoring scripting.



🎥 Video Tutorial

Follow along with our detailed video tutorial on our [Cisco Observability YouTube Channel](https://youtu.be/XzE4_croAcU):

▶️ [Watch the Lab 1 Video Here](https://youtu.be/XzE4_croAcU)



🛠 Prerequisites

Before starting this lab, make sure you have the following installed and set up:


[Python 3.7+](https://www.python.org/downloads/)

Ensure Python is installed and added to your system's PATH.
[pip](https://pip.pypa.io/en/stable/installation/)

Python's package manager for installing dependencies.
[Selenium Package](https://pypi.org/project/selenium/)

Install Selenium using pip:
```bash
pip install selenium
```
[Download ChromeDriver Package](https://pypi.org/project/chromedriver-py/)
```bash
pip install chromedriver-py
```

[IDE or Code Editor](https://code.visualstudio.com/)

Use an Integrated Development Environment (IDE) like Visual Studio Code or PyCharm for coding and debugging.
[AppDynamics Synthetic Monitoring License](https://docs.appdynamics.com/appd/24.x/latest/en/splunk-appdynamics-licensing/license-entitlements-and-restrictions)

Ensure your AppDynamics account includes synthetic monitoring capabilities.


🚀 Objectives

By the end of this lab, you will:


Write a simple Browser Synthetic Monitoring Script using Python and Selenium.
Debug and validate your script locally.
Upload the script to AppDynamics for synthetic monitoring.
Configure and test the synthetic monitor in AppDynamics.



🔧 Steps to Complete the Lab

1. Clone the Repository

Clone the ObservabilityLabs repository to your local system:


```bash
git clone https://github.com/markand4/ObservabilityLabs.git
cd ObservabilityLabs/Lab1-FirstBrowserSyntheticMonitoringScript
```

2. Set Up Your Environment

Verify Python installation:

```bash
Copy Code
python --version
Ensure it’s version 3.7 or higher.
```

Install the Selenium package:

```bash
pip install selenium
```

Download and configure the WebDriver:

[Download ChromeDriver Package](https://pypi.org/project/chromedriver-py/) 
```bash
pip install chromedriver-py
```

3. Copy the script and make your own, delete all the steps and add them manually in to test yourself

Copy FirstBrowserSyntheticScript.py
Remove Lines 236-264

4. Debug Your Script Locally

Run the script using your IDE.

Check for any errors in your code.
Verify that the WebDriver opens the browser and performs the desired actions.


5. Upload the Script to AppDynamics

Log in to your AppDynamics Controller.
Navigate to Synthetic Jobs:
Select Create a New Synthetic Job.
Upload your Python script to the job configuration.
Set up monitoring intervals, locations, and other configurations.
Save and activate the synthetic job.


6. Test Your Script in AppDynamics

Run the synthetic job in AppDynamics.
Monitor results:
Verify if the script runs successfully.
Check for any failed steps or errors in the synthetic job logs.
Debug and optimize the script as needed.


📢 Need Help?

If you encounter issues or have questions, feel free to:


Watch the video tutorial: [Cisco Observability YouTube Channel](https://youtu.be/XzE4_croAcU)
Open an issue: [GitHub Issues](../../issues)
Join the discussion: [GitHub Discussions](../../discussions)


✨ Features of This Lab

Hands-on experience with Python and Selenium.
Practical debugging techniques for browser scripts.
Integration with AppDynamics Synthetic Monitoring.
Reusable script templates for future projects.


📜 License

This lab is part of the ObservabilityLabs repository and is licensed under the [Apache License 2.0](../../LICENSE).



📬 Stay Connected

Subscribe to our [Cisco Observability YouTube Channel](https://www.youtube.com/@CiscoObservability) for more tutorials and labs.
Follow this repository for updates on new labs and features.


Let’s build something amazing together! 🚀
