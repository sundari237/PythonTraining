
import numpy as np
import pandas as pd
import requests
import time


# --------------------------------------------------
# TASK 1: LISTS AND DICTIONARIES
# --------------------------------------------------

print("\n--- TASK 1: CARER HOURS ---")

carers = ["Prachi", "Snehal", "Simi", "Monica"]

hours = {
    "Prachi": 6,
    "Snehal": 8,
    "Simi": 5,
    "Monica": 7
}

# Print the list of carers
print("Carers:", carers)

# Print Snehal's hours
print("Snehal's hours:", hours["Snehal"])

# Calculate total hours worked
total_hours = sum(hours.values())
print("Total hours worked:", total_hours)

# Print carers who worked more than 6 hours
print("Carers who worked more than 6 hours:")

for carer, worked_hours in hours.items():
    if worked_hours > 6:
        print(carer, worked_hours)


# --------------------------------------------------
# TASK 2: FUNCTIONS AND CONDITIONS
# --------------------------------------------------

print("\n--- TASK 2: CHECK WEEKLY ALLOWANCE ---")

def check_allowance(total, allowance):

    if total < allowance:
        remaining = allowance - total
        print("Hours remaining:", remaining)

    elif total > allowance:
        exceeded = total - allowance
        print("Hours exceeded:", exceeded)

    else:
        print("Hours exactly match the allowance!")


# Term-time allowance = 26 hours
print("\nWeek 1:")
check_allowance(24, 26)

print("\nWeek 2:")
check_allowance(29, 26)

# Holiday allowance = 31 hours
print("\nHoliday week:")
check_allowance(31, 31)


# --------------------------------------------------
# TASK 3: NUMPY ANALYSIS
# --------------------------------------------------

print("\n--- TASK 3: NUMPY WEEKLY ANALYSIS ---")

weekly_hours = np.array([24, 28, 25, 26, 22, 30, 27])

# Calculate mean
print("Mean hours:", np.mean(weekly_hours))

# Calculate maximum
print("Maximum hours:", np.max(weekly_hours))

# Calculate minimum
print("Minimum hours:", np.min(weekly_hours))

# Calculate standard deviation
print("Standard deviation:", np.std(weekly_hours))

# Count weeks exceeding 26 hours
weeks_over_allowance = np.sum(weekly_hours > 26)

print("Weeks exceeding 26 hours:", weeks_over_allowance)


# --------------------------------------------------
# TASK 4: PANDAS DATAFRAME
# --------------------------------------------------

print("\n--- TASK 4: PANDAS CARE RECORDS ---")

care_data = {
    "Carer": ["Prachi", "Snehal", "Simi", "Monica", "Priya"],
    "Hours": [6, 8, 5, 7, 4]
}

df = pd.DataFrame(care_data)

# Display the complete DataFrame
print("\nAll care records:")
print(df)

# Filter carers who worked more than 5 hours
print("\nCarers who worked more than 5 hours:")
print(df[df["Hours"] > 5])

# Calculate average hours
print("\nAverage hours:", df["Hours"].mean())

# Filter carers who worked fewer than 6 hours
print("\nCarers who worked fewer than 6 hours:")
print(df[df["Hours"] < 6])


# --------------------------------------------------
# TASK 5: HTTP REQUESTS AND JSON
# --------------------------------------------------

print("\n--- TASK 5: FETCH CARE RECORDS ---")

url = "http://localhost:3000/care"

params = {"week": 1}

try:
    response = requests.get(url, params=params, timeout=10)

    # Check whether the request was successful
    response.raise_for_status()

    # Convert JSON response into Python data
    data = response.json()

    print("Returned JSON data:")
    print(data)

    # Print the raw response text
    print("Response text:")
    print(response.text)

except requests.exceptions.RequestException as error:
    print("API request failed:", error)

except ValueError:
    print("The API response is not valid JSON.")


# --------------------------------------------------
# TASK 6: PAGINATION AND RATE LIMITING
# --------------------------------------------------

print("\n--- TASK 6: FETCH ALL CARE RECORDS ---")

url = "http://localhost:3000/care"

page_number = 1
per_page = 100

while True:

    params = {
        "page": page_number,
        "per_page": per_page
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        # Support either a JSON list or a dictionary
        # containing a "records" list
        if isinstance(data, list):
            records = data
        elif isinstance(data, dict) and "records" in data:
            records = data["records"]
        else:
            print("Unexpected API response format.")
            break

        print("\nPage:", page_number)
        print("Records returned:", len(records))
        print(records)

        # Stop when fewer than 100 records are returned
        if len(records) < per_page:
            print("Last page reached.")
            break

        # Move to the next page
        page_number += 1

        # Wait one second before the next request
        time.sleep(1)

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)
        break

    except ValueError:
        print("The API response is not valid JSON.")
        break

print("\n--- PROGRAM FINISHED ---")
