# Cost of Living Analysis

A financial analysis of the cost of living in Victoria, BC is done using web scraping and displayed using a basic web GUI. Using the newly obtained data, financial information is displayed about real estate prices, average wages, and estimated expenses involved in the costs of living. Dynamic and real-time calculations are then made analyzing scenarios such as: how long it would take to save for a condo down payment or pay off a mortgage at an average wage, and how long to save for a down payment when working a minimum wage job.

## Skills Used:

-   Python
    -   Requests
    -   CSV
    -   Custom Classes and Functions
    -   Flask Bootstrap
-   Data Science
    -   Statistics
-   Web Scraping
    -   BeautifulSoup
-   HTML
-   CSS
    -   Bootstrap
-   UI/UX Design

## Methodology:

-   Each time the site is initialized, the following data is obtained:
    -   Current listed prices for 1 bedroom condos in Victoria, BC
    -   Current average hourly wages from 2 sources posting jobs in Victoria, BC and create an average wage from those sources
    -   Current estimated monthly costs for a single person living in Victoria, BC
-   Time to pay off a mortgage is based off the freshly obtained data and calculated using a 5% interest rate and 10% down payment
-   Minimum wage used in calculations is: `$17.40`
-   **_Note:_** all calculations are estimates and only meant for demonstration purposes

## Screenshots
