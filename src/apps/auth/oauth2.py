#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :oauth2.py
# @Author   :Lowell
# @Time     :2023/8/2 15:11
from httpx_oauth.clients import google, github, microsoft

from src.core.config import settings

# Google
google_oauth2_client = google.GoogleOAuth2(
    settings.GOOGLE_OAUTH_CLIENT_ID,
    settings.GOOGLE_OAUTH_CLIENT_SECRET,
)

# Github
github_oauth2_client = github.GitHubOAuth2(
    settings.GITHUB_OAUTH_CLIENT_ID,
    settings.GITHUB_OAUTH_CLIENT_SECRET,
)

# Microsoft
microsoft_oauth2_client = microsoft.MicrosoftGraphOAuth2(
    settings.MICROSOFT_OAUTH_CLIENT_ID,
    settings.MICROSOFT_OAUTH_CLIENT_SECRET,
)
