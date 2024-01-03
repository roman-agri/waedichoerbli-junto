import urllib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.management import call_command
from django.urls import reverse
from juntagrico.entity.depot import Depot

import base64
import hmac
import hashlib
from urllib import parse
from datetime import datetime
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from juntagrico.models import Member
from juntagrico.entity.jobs import ActivityArea
from juntagrico.dao.assignmentdao import AssignmentDao
from juntagrico.dao.depotdao import DepotDao
from juntagrico.dao.listmessagedao import ListMessageDao
from juntagrico.util.temporal import weekdays, start_of_business_year, end_of_business_year
from juntagrico.config import Config
from django.utils import timezone

from waedichoerbli.utils.utils import get_delivery_dates_of_month

# special work areas for members
@login_required
def special_work_areas(request):
    '''
    All hidden areas 
    '''
    myareas = ActivityArea.objects.filter(hidden=True)

    renderdict = {
        'areas': myareas,
    }

    return render(request, 'special_work_areas.html', renderdict)

# download area for members
@login_required
def download_area(request, success=False):
    return render(request, 'download_area.html', {'success': success})

# rezepte for members
@login_required
def rezepte(request, success=False):
    return render(request, 'rezepte.html', {'success': success})

# new meber jobs and subscription page
@login_required
def member_jobs_subscription(request, success=False):
    '''
    All jobs of current user and current business year
    '''
    member = request.user.member
    allassignments = AssignmentDao.assignments_for_member_current_business_year(member)
    totalamount = 0
    
    renderdict = {
        'assignments': allassignments,
        'totalamount': totalamount,
    }
    return render(request, 'member_jobs_subscription.html', renderdict)

# depot list generation
@staff_member_required
def list_mgmt(request, success=False):
    return render(request, 'list_mgmt.html', {'success': success})

@staff_member_required
def list_generate(request, future=False):
    def delivery_dates(depot):
        return list(get_delivery_dates_of_month(depot.weekday, int(request.GET.get('month', 0))))
    Depot.delivery_dates = delivery_dates
    call_command('generate_depot_list', force=True, future=future)
    return redirect(reverse('lists-mgmt-success'))

