# Amplitude baseline — новый поиск

**Проект Amplitude:** [internet-tourism / B2B](https://app.amplitude.com/analytics/internet-tourism/home)  
**Период:** 2026-08-18 — 2026-08-28 UTC  
**Дата сбора:** 2026-08-28  
**Метрика:** unique users, daily interval  
**Источник:** Amplitude AI / Product Analytics, read-only запросы из in-app browser.

## Зачем

Нужен baseline перед оценкой влияния нового поиска через 1-2 недели. Основной вопрос: изменятся ли метрики главной страницы, запуска поиска, открытия выдачи и перехода к бронированию после rollout нового compact search / SERP editor.

## Найденные события

| Направление | Event |
|-------------|-------|
| Главная | `b2b_travel_main_page_view` |
| Сессии | `session_start` |
| Авиа: запуск поиска | `b2b_flights_search_button_click` |
| Авиа: выдача | `b2b_flights_serp_page_open` |
| Авиа: просмотр оффера | `b2b_flights_offer_detail_view` |
| Авиа: переход к бронированию | `b2b_flights_booking_button_click` |
| Отели: запуск поиска | `b2b_hotels_search_button_click` |
| Отели: выдача | `b2b_hotels_serp_page_open` |
| Отели: переход к бронированию | `b2b_hotels_booking_page_open` |
| ЖД: запуск поиска | `b2b_rw_search_button_click` |
| ЖД: выдача | `b2b_rw_serp_page_open` |
| ЖД: переход к бронированию | `b2b_rw_booking_page_open` |
| Ошибки отелей | `hotelflow-search-error-modal`, `hotels-search-form-err-modal` |
| Ошибки ЖД | `rw-search-places-error-modal`, `rw-search-tickets-error-modal` |

## Coverage gaps

Amplitude не нашла отдельные события для:

- открытия compact search editor на SERP;
- повторного поиска из SERP после редактирования;
- единого `search_submit` для всех продуктов;
- надежного error rate по периоду 2026-08-18 — 2026-08-28: error events есть, но Amplitude отметила, что они stale относительно периода и не появились в returned series.

Для оценки нового compact search нужно добавить или проверить события:

- `b2b_search_editor_open`;
- `b2b_search_editor_submit`;
- `b2b_search_editor_cancel`;
- `b2b_search_editor_auto_collapse`;
- `b2b_search_repeat_from_serp`;
- `b2b_search_results_loaded`;
- `b2b_search_results_error`.

Минимальные properties: `product` (`flights` / `hotels` / `rail`), `source` (`home` / `serp_compact` / `trip`), `company_id_hash`, `locale`, `device_type`, `has_trip_context`, `result_count`, `error_code`.

## Daily baseline

Daily unique users, UTC.

| Date | Homepage | Sessions* | Flight search | Flight SERP | Flight booking | Hotel search | Hotel SERP | Hotel booking | Rail search | Rail SERP | Rail booking |
|------|---------:|----------:|--------------:|------------:|---------------:|-------------:|-----------:|--------------:|------------:|----------:|-------------:|
| 2026-08-18 | 543 | 1 098 | 323 | 331 | 206 | 49 | 51 | 26 | 75 | 79 | 41 |
| 2026-08-19 | 520 | 1 025 | 291 | 311 | 185 | 54 | 56 | 24 | 65 | 68 | 40 |
| 2026-08-20 | 489 | 989 | 304 | 323 | 185 | 35 | 36 | 19 | 61 | 64 | 32 |
| 2026-08-21 | 533 | 1 000 | 302 | 318 | 202 | 50 | 52 | 27 | 67 | 71 | 43 |
| 2026-08-22 | 106 | 271 | 72 | 73 | 53 | 10 | 11 | 9 | 22 | 25 | 13 |
| 2026-08-23 | 82 | 231 | 59 | 63 | 34 | 14 | 14 | 13 | 18 | 19 | 9 |
| 2026-08-24 | 612 | 1 080 | 348 | 368 | 238 | 53 | 57 | 37 | 69 | 72 | 38 |
| 2026-08-25 | 553 | 1 065 | 315 | 342 | 206 | 40 | 42 | 19 | 64 | 69 | 40 |
| 2026-08-26 | 548 | 1 066 | 318 | 338 | 205 | 43 | 45 | 25 | 50 | 58 | 36 |
| 2026-08-27 | 520 | 950 | 323 | 344 | 221 | 45 | 47 | 29 | 67 | 70 | 41 |
| 2026-08-28 | 381 | 713 | 195 | 212 | 104 | 17 | 18 | 8 | 37 | 40 | 23 |

`session_start` здесь тоже посчитан как unique users who started a session, а не как количество сессий.

## Daily sums

Сумма daily unique users полезна для volume baseline, но не является deduplicated unique users за весь период.

| Метрика | Сумма daily unique users |
|---------|-------------------------:|
| Homepage | 4 887 |
| Sessions* | 9 488 |
| Flight search | 2 850 |
| Flight SERP | 3 023 |
| Flight booking | 1 839 |
| Hotel search | 410 |
| Hotel SERP | 429 |
| Hotel booking | 236 |
| Rail search | 595 |
| Rail SERP | 635 |
| Rail booking | 356 |

В daily series SERP может быть выше search, потому что события считаются независимо по дням и пользователям. Эти суммы нельзя использовать как настоящую конверсию.

## User-level funnels

Amplitude построила отдельные user-level sequential funnels за весь период. Это основной baseline для conversion.

| Product | Search users | SERP users | Booking users | Search -> SERP | SERP -> booking | Search -> booking |
|---------|-------------:|-----------:|--------------:|----------------:|-----------------:|------------------:|
| Flights | 1 174 | 1 172 | 916 | 99.8% | 78.2% | 78.0% |
| Hotels | 230 | 222 | 135 | 96.5% | 60.8% | 58.7% |
| Rail | 263 | 262 | 161 | 99.6% | 61.5% | 61.2% |

Event sequences:

- Flights: `b2b_flights_search_button_click` -> `b2b_flights_serp_page_open` -> `b2b_flights_booking_button_click`
- Hotels: `b2b_hotels_search_button_click` -> `b2b_hotels_serp_page_open` -> `b2b_hotels_booking_page_open`
- Rail: `b2b_rw_search_button_click` -> `b2b_rw_serp_page_open` -> `b2b_rw_booking_page_open`

## Интерпретация для performance review

Что можно говорить сейчас:

- Есть baseline для главной и трех search funnels перед сравнением после rollout.
- Самый большой объем у авиа: 1 174 search users и 916 booking users в user-level funnel за 2026-08-18 — 2026-08-28.
- По всем трем продуктам почти все пользователи, запустившие поиск, доходят до события открытия SERP.
- Самый большой drop-off находится между SERP и booking: flights 78.2%, hotels 60.8%, rail 61.5%.

Что нельзя утверждать без следующего среза:

- что новый compact search увеличил повторные поиски;
- что пользователи стали чаще редактировать поиск на SERP;
- что снизился error rate;
- что выросла конверсия из SERP в booking.

## Follow-up через 1-2 недели

Повторить эти же срезы за сопоставимый период:

1. Daily unique users по тем же events.
2. User-level funnels по тем же трем последовательностям.
3. Если появятся новые события compact search, добавить отдельный блок:
   - editor open rate = `b2b_search_editor_open` / SERP users;
   - repeat search rate = `b2b_search_repeat_from_serp` / editor open users;
   - repeat search success = `b2b_search_results_loaded` / repeat search submit;
   - error rate = `b2b_search_results_error` / search submit.

Сравнение делать не по сырым daily sums, а по:

- deduplicated funnel users за период;
- per-day average для volume metrics;
- weekday-vs-weekday, если период меньше 14 дней.

