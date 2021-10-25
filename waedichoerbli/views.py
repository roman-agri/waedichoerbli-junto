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
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from juntagrico.models import Member

from juntagrico.dao.depotdao import DepotDao
from juntagrico.dao.listmessagedao import ListMessageDao
from juntagrico.util.temporal import weekdays, start_of_business_year, end_of_business_year
from juntagrico.config import Config
from django.utils import timezone

from waedichoerbli.utils.utils import get_delivery_dates_of_month



# download area for members
@login_required
def download_area(request, success=False):
    return render(request, 'download_area.html', {'success': success})

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

