#
# -*- coding: utf-8 -*- vim:fileencoding=utf-8:
# Copyright © 2010-2012 Greek Research and Technology Network (GRNET S.A.)
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
# TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.

from django.contrib import admin
from ganetimgr.apply.models import *
from ganetimgr.ganeti.models import Cluster

def make_fast_create_actions():
    actions = []
    for cluster in Cluster.objects.filter(fast_create=True):
        def _submit_applications(modeladmin, request, queryset):
            for app in queryset:
                if app.status == STATUS_PENDING:
                    app.approve()

                if app.status == STATUS_APPROVED:
                    app.cluster = cluster
                    app.save()
                    app.submit()

        _submit_applications.short_description = "Approve and submit to %s" % \
            cluster.description
        # Change the function name, because the admin interface relies on it
        _submit_applications.func_name = "submit_applications_%s" % \
            str(cluster.slug)
        actions.append(_submit_applications)
    return actions


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["hostname", "applicant", "organization", "cluster",
                    "network", "status", "filed"]
    list_filter = ["status", "network", "organization"]
    list_editable = ["organization", "network"]
    readonly_fields = ["job_id", "backend_message"]
    ordering = ["-filed", "hostname"]
    actions = make_fast_create_actions()
    fieldsets = [
        ('Instance Information', {'fields': ('hostname', 'memory', 'disk_size',
                                             'vcpus', 'operating_system',
                                             'hosts_mail_server') }),
        ('Placement', {'fields': ('network',)}),
        ('Owner Information', {'fields': ('applicant', 'organization',
                                          'admin_contact_name',
                                          'admin_contact_phone',
                                          'admin_contact_email')}),
        ('Backend Information', {'fields': ('status', 'job_id',
                                            'backend_message')})
    ]

admin.site.register(Organization)
admin.site.register(InstanceApplication, ApplicationAdmin)
