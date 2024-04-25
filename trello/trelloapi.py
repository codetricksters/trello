import requests
from requests import HTTPError


class trello:

    def __init__(self, key, token, board):
        self.key = key
        self.token = token

    def get_board(self, board):
        url = f'https://api.trello.com/1/boards/{board}'

        parameters = {
            'actions': 'all',
            'boardStars': 'none',
            'cards': 'none',
            'card_pluginData': 'false',
            'checklists': 'none',
            'customFields': 'false',
            'fields': 'name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames',
            'lists': 'open',
            'members': 'none',
            'memberships': 'none',
            'membersInvited': 'none',
            'membersInvited_fields': 'all',
            'pluginData': 'false',
            'organization': 'false',
            'organization_pluginData': 'false',
            'myPrefs': 'false',
            'tags': 'false',
            'key': self.key,
            'token': self.token,
        }

        response = requests.get(url, params=parameters)

        try:
            assert response.status_code == 200
        except HTTPError as e:
            raise e

        return response.json()

    def get_cards(self):
        url = f'https://api.trello.com/1/boards/{self.board}/cards/'

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }
        parameters = {'key': self.key, 'token': self.token}
        response = requests.get(url, headers=headers, params=parameters)
        try:
            assert response.status_code == 200
        except HTTPError as e:
            raise e

        return response.json()

    def get_card_by_id(self, card_id):
        self.card_id = card_id

        url = f'https://trello.com/1/boards/{self.board}/cards/{self.card_id}'

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }
        parameters = {'key': self.key, 'token': self.token}

        response = requests.get(url, headers=headers, params=parameters)
        try:
            assert response.status_code == 200
        except HTTPError as e:
            raise e

        return response.json()

    def get_member(self, member):
        url = f'https://api.trello.com/1/members/{member}'

        parameters = {
            'boardBackgrounds': 'none',
            'boardsInvited_fields': 'name,closed,idOrganization,pinned',
            'boardStars': 'false',
            'cards': 'none',
            'customBoardBackgrounds': 'none',
            'customEmoji': 'none',
            'customStickers': 'none',
            'fields': 'all',
            'organizations': 'none',
            'organization_fields': 'all',
            'organization_paid_account': 'false',
            'organizationsInvited': 'none',
            'organizationsInvited_fields': 'all',
            'paid_account': 'false',
            'savedSearches': 'false',
            'tokens': 'none',
            'key': self.key,
            'token': self.token,
        }

        response = requests.get(url, params=parameters)
        try:
            assert response.status_code == 200
        except HTTPError as e:
            raise e

        return response.json()
