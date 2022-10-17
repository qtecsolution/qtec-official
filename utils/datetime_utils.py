from datetime import timedelta
import datetime

today = datetime.date.today()


def date_range(start, end):
    delta = end - start  # as timedelta
    final_list = []
    for i in range(delta.days + 1):
        days = (start + timedelta(days=i))
        date = days.strftime("%Y-%m-%d")
        a= {
            'date' : date,
            'value': 0
        }
        final_list.append(a)
    return final_list


class DateOperationMixin(object):

    def this_week(self):
        return today.strftime("%V")

    def n_days_ago(self, n):
        return today - datetime.timedelta(days=n)

    def today(self):
        return datetime.datetime.date(datetime.datetime.now())

    def yesterday(self):
        one_days_age = self.n_days_ago(1)
        return one_days_age

    def last_seven_days(self):
        seven_days_ago = self.n_days_ago(7)
        return seven_days_ago

    def last_fifteen_days(self):
        seven_days_ago = self.n_days_ago(15)
        return seven_days_ago

    def last_thirty_days(self):
        thirty_days_ago = self.n_days_ago(30)
        return thirty_days_ago

    def current_month(self):
        month = datetime.datetime.now().month
        return month

    def last_month_year(self):
        first = today.replace(day=1)
        last_month = first - timedelta(days=1)
        print(last_month.strftime("%Y"))
        return last_month.strftime("%Y")

    def last_month(self):
        first = today.replace(day=1)
        lastMonth = first - timedelta(days=1)
        print(lastMonth.strftime("%m"))
        return lastMonth.strftime("%m")

    def current_year(self):
        return today.year

    def last_year(self):
        now = datetime.datetime.now()
        return '{}-{}-{}'.format(now.year - 1,today.month, today.day)

    def six_month_previous_date(self):
        return today - timedelta(days=(6 * 365 / 12))