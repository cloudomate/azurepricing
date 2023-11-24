### User Guide for Web Scraping and Data Processing Tool

#### Introduction
This guide provides step-by-step instructions on how to use a custom-built web scraping and data processing tool. It's designed to extract pricing information for virtual machines from specific web pages and consolidate this data into a CSV file. As a prerequiste you will need to have the html files copied in the folder, this needs to be done by visiting the website and copying the files, for chrome you can use developer tool to copy the html body 

#### Requirements
- Google Chrome Browser
- Python 3.x
- Required Python libraries: `pandas`, `bs4` (BeautifulSoup)
- HTML files of the web pages to be scraped (named as `linux.html`, `rhel.html`, `windows.html`)

#### Setup
1. **Install Python Libraries**: 
   Install the required Python libraries by running the following command in your terminal or command prompt:
   ```
   pip install pandas beautifulsoup4
   ```

2. **HTML Files**: 
   Place the HTML files (`linux.html`, `rhel.html`, `windows.html`) in the same directory as the script.

#### How to Use
1. **Open the Script**: Open the script in a Python editor or IDE.

2. **Run the Script**: Execute the script. This can typically be done by pressing a run button in your IDE or by typing `python your_script_name.py` in the terminal, where `your_script_name.py` is the name of your script file.

3. **Web Scraping**: The script will use BeautifulSoup to read through the provided HTML files and extract relevant pricing data.

4. **Data Processing**: After extraction, the script processes and organizes this data into a structured format.

5. **Output**: The script will output CSV files for each type of VM (Linux, RHEL, Windows) and a consolidated CSV file named `consolidated.csv`.

#### Troubleshooting
- If the script fails to run, check that all libraries are installed, and the Chrome WebDriver is correctly set up and added to your system's PATH.
- Verify the HTML files' format and location.
- Look for syntax errors or typos in the script.

