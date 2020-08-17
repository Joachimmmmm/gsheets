# gsheets
A python script that allows you to read/write information from a google spreadsheet

In order to get this working for yourself, follow these steps
1.go over to https://console.cloud.google.com/ and create a new project
2.enable google sheets api
3.enable the google drive api and goto credentials and create a new service account, give them the editor role, the go to edit it and create a new key, choose the json file and when you press done it should download your credentials file. Open this in a notepad and look for 'client_email', copy this and paste into your shared tab in your actual google sheet
4. Don't forget to change creds in the code itself as well as changing the sheet name.
