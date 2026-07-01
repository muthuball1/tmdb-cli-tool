
# TMDB CLI Tool

A simple CLI tool to fetch movies from The Movie Database (TMDB) API.

## Installation

Clone the repository:
```bash
git clone https://github.com/aadithyamuthukumar/tmdb-cli-tool.git
cd tmdb-cli-tool
```

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory with your TMDB API key:
```API_KEY=YOUR_API_KEY```

> Use your **API Read Access Token (v4 auth)** from TMDB (Settings → API), not the v3 API Key.

## Usage

```bash
python tmdb.py --type "upcoming"
python tmdb.py --type "top_rated"
python tmdb.py --type "popular"
python tmdb.py --type "now_playing"
```

Valid `--type` values: `upcoming`, `top_rated`, `popular`, `now_playing`

## Example Output

```-------------------------
Title: Power Ballad
Released: 2026-05-18
Rating: 7.1
Overview: When Rick, a past-his-prime wedding singer, meets fading boy-band star Danny during a gig, the two bond over music and a late-night jam session. But when Danny turns one of Rick’s songs into the hit that reignites his career, Rick sets out to reclaim the recognition he believes he deserves - even if it means risking everything he cares about.
-------------------------
