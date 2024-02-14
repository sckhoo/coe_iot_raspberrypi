import datetime
import pytz


# Define the timestamp in milliseconds
timestamp_ms = 1707408048094

# Convert milliseconds to seconds
timestamp_s = timestamp_ms / 1000

# Convert seconds to a datetime object (assuming UTC time)
dt_utc = datetime.datetime.fromtimestamp(timestamp_s)

# Get your local time zone (replace with your actual time zone)
local_tz = pytz.timezone("Asia/Kuala_Lumpur")  # Example for Kuala Lumpur, Malaysia

# Convert UTC datetime to local time
dt_local = dt_utc.astimezone(local_tz)

# Print the datetime in both UTC and local time
print(f"UTC datetime: {dt_utc}")
print(f"Local datetime: {dt_local.year}")