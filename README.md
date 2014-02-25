ganetimgr
=========

ganetimgr is a web platform that eases the provisioning of virtual machines over multiple ganeti clusters.
It leverages Ganeti's RAPI functionality to administer the clusters, and is stateless from the VM perspective.
The project is written in Django and uses Bootstrap for the frontend.
In essence, ganetimgr aims to be the frontend of a VPS service.

The main project repository is at [code.grnet.gr](https://code.grnet.gr/projects/ganetimgr).

## Setup Instructions

For detailed instructions, go to our [readthedocs](http://ganetimgr.readthedocs.org/en/latest/) page.

## Actions needed on version upgrades

### Migrating to v.1.4.1
Bugfix/Feature Enhancements release

settings.py:
- Copy the FLATPAGES dict from settings.py.dist to allow handling of flatpages

### Migrating to v.1.4.0
Debian wheezy/Django 1.4 compatibility

settings.py:
 - If migrating from a squeeze installation pay attention to
   Django 1.4 changes as depicted in settings.py file, especially the
   introduction of the staticfiles django app
 - Set the FEED_URL to an RSS news feed if desired
 - Setup WebSockets VNCAuthProxy if desired
 - If WebSockets NoVNC is setup, set the WEBSOCK_VNC_ENABLED to True
   and the NOVNC_PROXY and NOVNC_USE_TLS to match your setup
 - Update the BRANDING dict to match your needs
 - Perform south migration

======================================================================

### Migrating to v.1.3.0

 - Set the WHITELIST_IP_MAX_SUBNET_V4/V6 to desired max
	whitelist IP subnets in settings.py
 - Perform south migration

======================================================================

### Migrating to v.1.2.3
 - Make sure to include `HELPDESK_INTEGRATION_JAVASCRIPT_PARAMS` in settings.py.
If you deploy Jira and want to set custom javascript parameters, set
```
HELPDESK_INTEGRATION_JAVASCRIPT_PARAMS = { 'key' : 'value' # eg. 'customfield_23123': '1stline' }
```
In any other case set
```
HELPDESK_INTEGRATION_JAVASCRIPT_PARAMS = False
```

======================================================================

### Migrating to v1.2.2
- Make sure to restart watcher.py

======================================================================

### Migrating to >= v1.2
- Make sure to:
    - Set the RAPI_TIMEOUT in settings.py (see .dist)
    - Set the NODATA_IMAGE path in settings.py.dist
    - Update urls.py to urls.py.dist
    - Copy templates/analytics.html.dist to templates/analytics.html.

=====================================================================

### Migrating to v1.0:
 - install python-ipaddr lib
 - update settings.py and urls.py with latest changes from dist files
Run:
manage.py migrate

If your web server is nginx, consider placing:
```
proxy_set_header X-Forwarded-Host <hostname>;
```
in your nginx site location part and
```
USE_X_FORWARDED_HOST = True
```
in your settings.py.
The above ensures that i18n operates properly when switching between languages.

=====================================================================

## License
Copyright © 2010-2014 Greek Research and Technology Network (GRNET S.A.)

Copyright © 2010-2012 Apollon Oikonomopoulos (@apoikos)

Copyright © 2011-2014 Leonidas Poulopoulos (@leopoul)

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
SOFTWARE.
