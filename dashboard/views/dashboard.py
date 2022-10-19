
from django.shortcuts import render
from django.views import View
from datetime import date, datetime
from dashboard.models import CONTACTED, PENDING, UNSEEN, ApplyForThisPosition, Blog, CurrentOpportunities, LetsTalk, Subscribe, TeamMembers
from utils.datetime_utils import DateOperationMixin
from django.db.models import Count


class DashboardView(View, DateOperationMixin):
     
    @staticmethod
    def get_context(request, start, end):
        let_talk = LetsTalk.objects.filter(created_at__date__range=[start, end]).values('status').annotate(count=Count('status'))
        # print("pending::::::::::", pending.query)
        for item in let_talk:
            if item['status'] == PENDING:
                global pending 
                pending = item['count']
            if item['status'] == CONTACTED:
               global contacted
               contacted = item['count']
        total_blog = Blog.objects.all().count()
        total_subscribe = Subscribe.objects.all().count()
        total_teammembers = TeamMembers.objects.all().count()
        opportunities = CurrentOpportunities.objects.values('status').annotate(count=Count('status'))
        unseen_application = ApplyForThisPosition.objects.filter(status=UNSEEN).count()
        active_opportunities = 0
        closed_opportunities = 0
        for item in opportunities:
            if item['status'] == 0:
                active_opportunities = item['count']
            if item['status'] == 1:
               closed_opportunities = item['count']
        context = {
            "pending": pending,
            "contacted": contacted,
            "total_blog": total_blog,
            "total_subscribe": total_subscribe,
            "total_teammembers": total_teammembers,
            "closed_opportunities": closed_opportunities,
            "unseen_application": unseen_application,
            "active_opportunities": active_opportunities

        }
        return context
    def get(self, request):
        data = request.GET
        today = date.today().strftime("%Y-%m-%d")
        date_range = data.get('selected_range')
        if date_range:
            if date_range == 'last_seven_days':
                data = self.get_context(request,self.last_seven_days(), today)
            if date_range == 'last_fifteen_days':
                data = self.get_context(request,self.last_fifteen_days(), today)
            if date_range == 'last_thirty_days':
                data = self.get_context(request,self.last_thirty_days(), today)
            if date_range == 'last_six_months':
                print(self.six_month_previous_date())
                data = self.get_context(request,self.six_month_previous_date(), today)
            if date_range == 'last_year':
                data = self.get_context(request,self.last_year(), today)
        else:
            data = self.get_context(request,self.last_thirty_days(), today)

        return render(request, 'dashboard.html',data)