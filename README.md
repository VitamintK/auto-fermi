# auto-fermi
attempt to programmatically generate [fermi problems](https://en.wikipedia.org/wiki/Fermi_problem) from wikipedia content.  WIP: in sketch stage right now (and if you extrapolate from the fates of my previous personal projects, `s/right now/in perpetuity`).

using [mediawiki python package](https://github.com/barrust/mediawiki) to interact with the mediawiki API (although the API has a [pretty serious bug](https://phabricator.wikimedia.org/T201946) and is not officially maintained right now, and the wikipedia team is instead maintaining the ["rest base api"](https://en.wikipedia.org/api/rest_v1/#!/Page_content/get_page_summary_title), so maybe this should use that)

