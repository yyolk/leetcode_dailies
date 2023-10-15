# leetcode_dailies [![Generate Active Daily Every Day at 00:00 UTC](https://github.com/yyolk/leetcode_dailies/actions/workflows/generate_active_daily.yml/badge.svg)](https://github.com/yyolk/leetcode_dailies/actions/workflows/generate_active_daily.yml)
My daily leetcode problem submissions


## Generate today's boilerplate

Calls the 'undocumented' leetcode graphQL API to query for `activeDailyChallengeQuestion`.

It includes everything we want to generate our answer boilerplate.

```
python -m generate_active_daily
```

### Backfill missing permalinks in the solutions

This is an abnormal operation, it could be run during the daily upkeep, but all new boilerplate solutions include it already[^1].

```
python -m generate_active_daily.backfill_solution_links --no-debug --overwrite
```

## Generate the Solution Directories TOC

Each solution dir has a README.md with a table of contents that is a calendar with the days completed, hyperlinked to that solution file.

```
python -m generate_calendar_toc
```


[^1]: See [#3](https://github.com/yyolk/leetcode_dailies/pull/3) 
  and [#6](https://github.com/yyolk/leetcode_dailies/issues/6)
  for context and last run.
