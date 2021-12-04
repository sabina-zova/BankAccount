import sqlite3

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT * FROM history"):
#     utc_time = row[0]
#     local_time = pytz.utc.localize(utc_time).astimezone()
#     print("{}\t{}".format(utc_time, local_time))

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, history.account,"
#                       " history.amount FROM history ORDER BY history.time"):
#     print(row)

for row in db.execute("SELECT * FROM localhistory"):
    print(row)
db.close()

