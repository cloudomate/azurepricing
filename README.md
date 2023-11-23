### User Guide for Web Scraping and Data Processing Tool

#### Introduction
This guide provides step-by-step instructions on how to use a custom-built web scraping and data processing tool. It's designed to extract pricing information for virtual machines from specific web pages and consolidate this data into a CSV file. As a prerequiste you will need to have the html files copied in the folder, this needs to be done by visiting the website and copying the files, for chrome you can use developer tool to copy the html body 

#### Requirements
- Google Chrome Browser
- Python 3.x
- Required Python libraries: `selenium`, `pandas`, `bs4` (BeautifulSoup)
- HTML files of the web pages to be scraped (named as `linux.html`, `rhel.html`, `windows.html`)

#### Setup
1. **Install Python Libraries**: 
   Install the required Python libraries by running the following command in your terminal or command prompt:
   ```
   pip install selenium pandas beautifulsoup4
   ```

2. **Download Chrome WebDriver**:
   - Go to the [Chrome WebDriver Downloads page](https://sites.google.com/chromium.org/driver/).
   - Download the version of WebDriver that matches your version of Google Chrome. To check your Chrome version, go to `chrome://version/` in your Chrome browser.
   - Unzip the downloaded file to extract the WebDriver.

3. **Setting Up Chrome WebDriver**:
   - Place the unzipped Chrome WebDriver (`chromedriver.exe` for Windows, `chromedriver` for macOS or Linux) in a known directory on your computer.
   - Add the directory containing the WebDriver to your system's PATH. This allows the script to access WebDriver without specifying its full path.
      - For Windows:
        - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
        - Click on 'Advanced system settings' and then 'Environment Variables'.
        - Under 'System Variables', find and select the 'Path' variable, then click 'Edit'.
        - Add the full path to the directory containing `chromedriver.exe`.
        - Click 'OK' to save the changes.
      - For macOS/Linux:
        - Open Terminal.
        - Use the command `export PATH=$PATH:/path/to/directory` (replace `/path/to/directory` with the directory containing `chromedriver`).
        - To make this change permanent, add the export command to your shell's profile script (like `.bash_profile` or `.bashrc`).

4. **HTML Files**: 
   Place the HTML files (`linux.html`, `rhel.html`, `windows.html`) in the same directory as the script.

#### How to Use
1. **Open the Script**: Open the script in a Python editor or IDE.

2. **Run the Script**: Execute the script. This can typically be done by pressing a run button in your IDE or by typing `python your_script_name.py` in the terminal, where `your_script_name.py` is the name of your script file.

3. **Web Scraping**: The script will use Selenium and BeautifulSoup to read through the provided HTML files and extract relevant pricing data.

4. **Data Processing**: After extraction, the script processes and organizes this data into a structured format.

5. **Output**: The script will output CSV files for each type of VM (Linux, RHEL, Windows) and a consolidated CSV file named `consolidated_uae_north.csv`.

#### Troubleshooting
- If the script fails to run, check that all libraries are installed, and the Chrome WebDriver is correctly set up and added to your system's PATH.
- Verify the HTML files' format and location.
- Look for syntax errors or typos in the script.

