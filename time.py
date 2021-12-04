import pytz
import datetime

print(pytz.utc.localize(datetime.datetime.utcnow()).astimezone())