from datetime import date, time, datetime, timedelta
from time import strptime
from dateutil import parser
from dateutil.relativedelta import relativedelta
import dateparser

# gestion timezone
from zoneinfo import ZoneInfo

print(date(2020, 1, 1))
print(datetime.today())

now = datetime.now()

print(now.second)

today = date.today()

tomorrow = today.replace(day = today.day +1)



print(date.fromisoformat("2020-10-01"))

print(datetime.strptime("10 Oct 2022", "%d %b %Y"))
print(datetime.strptime("10 May 2022", "%d %B %Y"))
print(now.strftime("%d %B %Y"))

print(parser.parse("10 Oct 2022 at 9:30pm"))

print(dateparser.parse("aujourd'hui"))
print(dateparser.parse("demain"))
print(dateparser.parse("Il y a un mois"))

now = datetime.now()
print(now.tzinfo)

now_in_vancouver = datetime.now(ZoneInfo('America/Vancouver'))
nom_in_montreal = datetime.now(ZoneInfo('America/Montreal'))
now_in_paris = datetime.now(ZoneInfo('Europe/Paris'))

print(now_in_vancouver)
print(nom_in_montreal)
print(now_in_paris)

print(now_in_vancouver > now_in_paris)

print(now_in_vancouver.astimezone(ZoneInfo('Europe/Paris')))

print(datetime(2020, 1, 1, tzinfo=ZoneInfo('Europe/Paris')))

# Attention fuseau horaire
montreal_tz = ZoneInfo('America/Montreal')
march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_8 = datetime(2020, 3, 8, 13, 0, 0, tzinfo=montreal_tz)
print(march_7)
print(march_7.tzname())
print(march_8)
print(march_8.tzname())
# Fuseau horaire international de référence
print(march_7.astimezone(ZoneInfo('UTC')))
print(march_8.astimezone(ZoneInfo('UTC')))

print(timedelta(days=20))
print(datetime.now())
print(datetime.now() + timedelta(days=20, hours=-1))

print(datetime.now() + relativedelta(months=2))