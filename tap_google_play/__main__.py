"""Entrypoint for tap-google-play.

Copyright (c) 2026 Edgar-Ramírez Mondragón
"""

from __future__ import annotations

from tap_google_play.tap import TapGooglePlay

TapGooglePlay.cli()
