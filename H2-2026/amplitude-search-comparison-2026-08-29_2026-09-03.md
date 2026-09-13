# Amplitude comparison — новый поиск

**Проект Amplitude:** [internet-tourism / B2B](https://app.amplitude.com/analytics/internet-tourism/home)  
**Baseline:** [2026-08-18 — 2026-08-28 UTC](./amplitude-search-baseline-2026-08-18_2026-08-28.md)  
**Post-period:** 2026-08-29 — 2026-09-03 UTC  
**Дата сбора:** 2026-09-04  
**Метрика:** unique users, daily interval; funnels = user-level sequential, convert within 1 day  
**Источник:** Amplitude AI / Product Analytics, read-only запрос из in-app browser.  
**Amplitude thread:** https://app.amplitude.com/agents/internet-tourism/session/637cd424-b968-4c4b-bdaa-daff22732e31/thread/0d255507-c1d1-4c8c-825e-f04ad23279c8

## Scope

Текущий день 2026-09-04 исключён как неполный. Для volume-сравнения используется average per day, потому что baseline содержит 11 дней, а post-period — 6 дней. Сырые суммы daily unique users оставлены только как контроль объёма.

## Daily unique users

| Date | Homepage | Sessions* | Flight search | Flight SERP | Flight booking | Hotel search | Hotel SERP | Hotel booking | Rail search | Rail SERP | Rail booking |
|------|---------:|----------:|--------------:|------------:|---------------:|-------------:|-----------:|--------------:|------------:|----------:|-------------:|
| 2026-08-29 | 100 | 222 | 55 | 55 | 39 | 12 | 16 | 8 | 19 | 23 | 12 |
| 2026-08-30 | 81 | 209 | 52 | 55 | 38 | 8 | 9 | 8 | 18 | 18 | 14 |
| 2026-08-31 | 590 | 1 078 | 343 | 362 | 211 | 47 | 52 | 36 | 74 | 79 | 55 |
| 2026-09-01 | 548 | 966 | 318 | 334 | 209 | 43 | 47 | 22 | 53 | 58 | 37 |
| 2026-09-02 | 581 | 1 057 | 341 | 359 | 223 | 65 | 68 | 43 | 55 | 59 | 38 |
| 2026-09-03 | 593 | 1 045 | 337 | 351 | 219 | 68 | 69 | 36 | 65 | 67 | 46 |

`session_start` здесь тоже посчитан как unique users who started a session, а не как количество сессий.

## Volume comparison

Baseline average/day пересчитан вручную из сохранённого baseline: сумма daily unique users / 11 дней. Post average/day = сумма / 6 дней.

| Metric | Baseline sum | Baseline avg/day | Post sum | Post avg/day | Change/day | Change |
|--------|-------------:|-----------------:|---------:|-------------:|-----------:|-------:|
| Homepage | 4 887 | 444.3 | 2 493 | 415.5 | -28.8 | -6.5% |
| Sessions* | 9 488 | 862.5 | 4 577 | 762.8 | -99.7 | -11.6% |
| Flight search | 2 850 | 259.1 | 1 446 | 241.0 | -18.1 | -7.0% |
| Flight SERP | 3 023 | 274.8 | 1 516 | 252.7 | -22.2 | -8.1% |
| Flight booking | 1 839 | 167.2 | 939 | 156.5 | -10.7 | -6.4% |
| Hotel search | 410 | 37.3 | 243 | 40.5 | +3.2 | +8.7% |
| Hotel SERP | 429 | 39.0 | 261 | 43.5 | +4.5 | +11.5% |
| Hotel booking | 236 | 21.5 | 153 | 25.5 | +4.0 | +18.9% |
| Rail search | 595 | 54.1 | 284 | 47.3 | -6.8 | -12.5% |
| Rail SERP | 635 | 57.7 | 304 | 50.7 | -7.1 | -12.2% |
| Rail booking | 356 | 32.4 | 202 | 33.7 | +1.3 | +4.0% |

## User-level funnels

| Product | Period | Search users | SERP users | Booking users | Search -> SERP | SERP -> booking | Search -> booking |
|---------|--------|-------------:|-----------:|--------------:|----------------:|-----------------:|------------------:|
| Flights | Baseline | 1 174 | 1 172 | 916 | 99.8% | 78.2% | 78.0% |
| Flights | Post | 852 | 847 | 634 | 99.4% | 74.9% | 74.4% |
| Hotels | Baseline | 230 | 222 | 135 | 96.5% | 60.8% | 58.7% |
| Hotels | Post | 153 | 147 | 94 | 96.1% | 63.9% | 61.4% |
| Rail | Baseline | 263 | 262 | 161 | 99.6% | 61.5% | 61.2% |
| Rail | Post | 162 | 161 | 115 | 99.4% | 71.4% | 71.0% |

| Product | Search -> SERP delta | SERP -> booking delta | Search -> booking delta |
|---------|---------------------:|-----------------------:|------------------------:|
| Flights | -0.4 pp | -3.3 pp | -3.6 pp |
| Hotels | -0.4 pp | +3.1 pp | +2.7 pp |
| Rail | -0.2 pp | +10.0 pp | +9.8 pp |

Event sequences:

- Flights: `b2b_flights_search_button_click` -> `b2b_flights_serp_page_open` -> `b2b_flights_booking_button_click`
- Hotels: `b2b_hotels_search_button_click` -> `b2b_hotels_serp_page_open` -> `b2b_hotels_booking_page_open`
- Rail: `b2b_rw_search_button_click` -> `b2b_rw_serp_page_open` -> `b2b_rw_booking_page_open`

## Compact search editor / repeat search coverage

Amplitude taxonomy was searched for names matching:

- `compact`
- `editor`
- `overlay`
- `repeat`
- `serp_search`
- `search_editor`
- `repeat_search`
- `disclosure`

Amplitude did not find matching real events in project `708958`.

Coverage gap remains: current instrumentation cannot directly measure compact search editor exposure, editor opens/cancels/submits, overlay interactions, repeat search from SERP, or successful search refinement. Existing events only measure the broader search -> SERP -> booking progression.

## Measured impact

- Search -> SERP conversion stayed practically flat in all products: flights -0.4 pp, hotels -0.4 pp, rail -0.2 pp.
- Flights downstream conversion weakened: SERP -> booking -3.3 pp and search -> booking -3.6 pp.
- Hotels downstream conversion improved: SERP -> booking +3.1 pp and search -> booking +2.7 pp.
- Rail downstream conversion improved most: SERP -> booking +10.0 pp and search -> booking +9.8 pp, but the post-period sample is smaller.
- Average daily volume did not move uniformly: homepage, sessions, flights, and rail search/serp are lower; hotel search/serp/booking and rail booking are higher.

## Hypotheses and caveats

| Hypothesis | Status |
|------------|--------|
| Новый поиск сломал Search -> SERP | Не подтверждается: все изменения меньше 0.5 pp. |
| Новый поиск улучшил редактирование / repeat search на SERP | Не измеряется: нет matching событий для compact editor / repeat search. |
| Есть flight-specific regression после SERP | Есть описательный сигнал: -3.3 pp SERP -> booking, но причинность не доказана. |
| Hotels/Rail стали конвертировать лучше после SERP | Описательно да, особенно rail, но выборка меньше baseline. |
| Изменение объясняется календарём / weekday mix | Возможно: в post-period два низких выходных дня 2026-08-29 и 2026-08-30; для демо лучше показывать также weekday-only comparison. |
| Изменение вызвано общим traffic/instrumentation shift | Нельзя исключить: sessions и homepage тоже ниже baseline avg/day. |

## Демо-формулировка

Можно говорить: после выката compact search основной вход в воронку не просел — Search -> SERP стабилен по авиа, отелям и ЖД. По downstream-метрикам картина смешанная: авиа немного ниже, отели и ЖД выше. Прямой эффект редактора поиска пока нельзя доказать, потому что нет событий editor open / repeat search from SERP; это отдельная рекомендация по instrumentation.

Нельзя говорить как подтверждённый эффект: новый compact search увеличил repeat search, снизил ошибки или напрямую поднял booking conversion. Для этого нужны события editor/repeat и более длинный post-period.
