# Flight Ticket Price Tracker

Using several APIs, this program allows for a personal and customizable service that sends an email to your inbox whenever a flight to any listed destination is found that matches your desired search parameters. The destination list is flexible and easy to add to, and search parameters are simple to manage and update, all using a Google Sheet. Find cheap flights anywhere in the world on any airline using this program.

## Skills Used:

-   Python
    -   Requests framework
    -   Parsing JSON data
    -   Exception handling
    -   Creating & sending HTML emails
    -   Creating & accessing dictionaries
    -   Custom Classes & Functions
    -   Loops
-   API
    -   GET requests
    -   API search queries
    -   Data POST
    -   Request limiting

![image4](https://github.com/user-attachments/assets/22e498be-3bc8-44de-bd58-4e15f4487272)

![image5](https://github.com/user-attachments/assets/38e92d57-685e-468d-ae65-a33f6b59776e)

## Instructions:

[1. Setup a Google Sheet](#google-sheet-setup)
[2. Create a Project with Sheety API](#create-sheety-project)
[3. Create a Kiwi Account](#create-kiwi-account)
[4. Enter API & Personal Credentials](#enter-credentials)

### Google Sheet Setup

![image](https://github.com/user-attachments/assets/dd0eb99f-3e81-446a-bc35-87569cfa8258)

Create a new Google Sheet and create 4 tabs with the following names:

-   `destinations`
-   `search_parameters`
-   `emails`
-   `search_history`

### Create Sheety Project

![image2](https://github.com/user-attachments/assets/0e390220-78f3-41f7-a3d0-6a8cdc79ab93)

[Sheety](https://sheety.co/) is the API used to both GET and POST fields from our Google Sheet. Full documentation on how to use Sheety can be [found here](https://sheety.co/docs/spreadsheet).

Create a new project and use the link for the new Google Sheet created for this program. The API data for the 4 Google Sheet tabs will be linked to in `src/data_manager.py`.

### Create Kiwi Account

![image3](https://github.com/user-attachments/assets/ffd39058-28f5-49d8-a91b-e8cc23581ead)

[Kiwi](https://tequila.kiwi.com/) is the API used to search for flight deals; full documentation can be [found here](https://tequila.kiwi.com/docs/user_guides/choosing_a_right_solution).

An account must be created on the Tequila portal to access the Kiwi API. Once logged in, create a new solution to obtain your API key. This will be added to `src/flight_search.py`.

### Enter API & Personal Credentials

In a .env file, provide tokens for:

-   Sheety API URL
-   Sheety Bearer Token
-   Kiwi API Key
-   Email App Specific Password
-   Sending/Receiving Email Address
