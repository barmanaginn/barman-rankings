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

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from barman.acl import active_required
from management.forms import SearchProductForm

from . import PluginApp


@active_required
@login_required
def ranking(request):
    """
    Displays the ranking page.
    """
    best_buyers = User.objects.order_by("-profile__debit")[
        : PluginApp.BarmanPluginMeta.RANKINGS_LENGTH
    ]
    best_drinkers = User.objects.order_by("-profile__alcohol")[
        : PluginApp.BarmanPluginMeta.RANKINGS_LENGTH
    ]
    form = SearchProductForm(request.POST or None)
    if form.is_valid():
        product_ranking = form.cleaned_data["product"].ranking
    else:
        product_ranking = None
    return render(
        request,
        "barman_rankings/ranking.html",
        {
            "best_buyers": best_buyers,
            "best_drinkers": best_drinkers,
            "product_ranking": product_ranking,
            "form": form,
        },
    )
