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

from users.models import Profile


@property
def rank(self):
    """
    Computes the rank (by :attr:`gestion.models.Profile.debit`) of the member.
    """
    return Profile.objects.filter(debit__gte=self.debit).count()


Profile.add_to_class("rank", rank)
