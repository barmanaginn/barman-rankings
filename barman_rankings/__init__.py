# barman-rankings - plugin for barman
# Copyright © 2019-2020 Yoann Pietri <me@nanoy.fr>
#
# barman-rankings is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# barman-rankings is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with barman-rankings.  If not, see <https://www.gnu.org/licenses/>.

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from barman.plugin import BarmanPlugin


class PluginApp(BarmanPlugin):
    name = "barman_rankings"

    class BarmanPluginMeta:
        name = "rankings"
        author = "Yoann Pietri"
        description = _("Add rankings to BarMan")
        version = 0.1
        url = "https://github.com/barmanaginn/barman-rankings"
        email = "me@nanoy.fr"

        nav_urls = (
            {
                "text": _("Ranking"),
                "icon": "list-ol",
                "link": reverse_lazy("plugins:barman_rankings:ranking"),
                "permission": None,
                "login_required": True,
                "admin_required": False,
                "superuser_required": False,
            },
        )

        settings = (
            {
                "name": "RANKINGS_LENGTH",
                "description": _("Number of places to display in the ranking"),
                "default": 20,
            },
        )

        user_profile = (
            {"text": _("Rank"), "value": lambda user: user.profile.rank},
            {
                "text": _("Ingerated alcohol"),
                "value": lambda user: "%.2f kg" % user.profile.alcohol,
            },
        )

    def ready(self):
        from . import signals

        return super().ready()


default_app_config = "barman_rankings.PluginApp"
