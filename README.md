# leetcode_dailies [![Generate Active Daily Every Day at 00:00 UTC](https://github.com/yyolk/leetcode_dailies/actions/workflows/generate_active_daily.yml/badge.svg)](https://github.com/yyolk/leetcode_dailies/actions/workflows/generate_active_daily.yml)
My daily leetcode problem submissions


## Generate today's boilerplate

Calls the 'undocumented' leetcode graphQL endpoint to grab the activeDailyChallengeQuestion.

It includes everything we want to generate our answer boilerplate.

```
python -m generate_active_daily
```

## Generate the Solution Directories TOC

Each solution dir has a README.md with a table of contents that is a calendar with the days completed, hyperlinked to that solution file.

```
python -m generate_calendar_toc
```


## Backlinks

Each problem has at least the date. Most if not all have the problem number.
For a query'able `question` to the leetcode graphQL endpoint, you want to have the `titleSlug`.
This is extractable from the link, and is a requested field in the `generate_active_daily` process.
