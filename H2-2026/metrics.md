# Метрики — H2 2026

**Период отчёта:** 2026-07-01 — 2026-08-28  
**Источники:** [Asana-срез](./asana-tasks.md), [Demo 0.0.11](./demos/2026-08/0.0.11-new-obt-demo.md), Amplitude B2B prod `708958`

## Delivery

| Метрика                           | Июль | Август по 26.08 | Итого |
| --------------------------------- | ---: | --------------: | ----: |
| Production task records           |   61 |              50 |   111 |
| Delivery items после дедупликации |   53 |              43 |    96 |
| Story points после дедупликации   |  154 |             148 |   302 |

> Сырая сумма production-записей — 334 SP. Итоговая сумма исключает 32 SP очевидного двойного учёта parent/subtask.

## Текущий pipeline задач

| Состояние                             | Количество | SP с заполненной оценкой |
| ------------------------------------- | ---------: | -----------------------: |
| В работе                              |          1 |                        2 |
| На тестировании / ошибка тестирования |          6 |                        9 |
| Готово к релизу                       |          6 |                        9 |
| Открыто / blocker                     |          3 |                        3 |
| Запланировано на спринт               |          1 |                        0 |
| Без workflow status                   |          1 |                        0 |

Live pipeline содержит 18 актуальных записей. CORP-4076 (ready/archive) и CORP-3007 (backlog/archive) показаны в Asana-срезе как historical carry-over и в эти числа не входят.

## Подтверждённый delivery

| Направление       | Результат                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New OBT stability | 30 дедуплицированных задач / 70 SP из OBT Баги Front                                                                                                                                                |
| Унификация layout | 34 SP; единый контейнер 1440px и устранение layout shift                                                                                                                                            |
| Авиа multi-city   | 13 SP; сложный маршрут поддержан от поиска до оплаты                                                                                                                                                |
| ЖД post-sale      | 8 SP; возврат из деталей заказа                                                                                                                                                                     |
| Employee / guest  | Guest capability + единый drawer в кабинете, авиа, ЖД и отелях                                                                                                                                      |
| Локализация       | [CORP-4535](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1216978052450452): ru/kk/en, parity/quality tests, 0 известных hardcoded user-facing violations по task report   |
| Platform security | [CORP-4513](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1216947017056390): Node.js 24.15.0, npm audit = 0, production build, 165 файлов / 688 unit-тестов по task report |
| Observability     | [CORP-4372](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1216697556263850): интеграция реализована; production rollout ожидает Legal approval                             |
| MICE              | MVP формы через Events API подготовлен к release 0.0.11                                                                                                                                             |
| SERP search overlay | Компакт-поиск на выдаче: клик по сегменту сразу открывает нужное поле (2 действия → 1). Влит в develop 28 августа (`30b7b0139`). Продуктовый эффект ещё не измерен. |
| Smart / FC badge  | Бейдж Smart для `$meta.provider_class === 'FC'` на ветке `feat/CORP-4836-fc-offer-badge`. В production нет. События показа бейджа в Amplitude нет. |

## Product analytics baseline — Amplitude B2B

**Дата снимка:** 2026-08-28  
**Проект:** Amplitude org Internet Tourism, B2B prod `708958`  
**Дашборд:** [Core dashboard](https://app.amplitude.com/analytics/internet-tourism/dashboard/syotujs7)  
**Окно:** last 30 days, unique users, ordered funnel, convert within 1 day  
**Статус:** baseline до выката SERP overlay. Это не post-release эффект.

Access к Amplitude подтверждён. Это закрывает этап «проверить доступ» из [metrics-framework](./metrics-framework.md). Backend orders / GMV по-прежнему authoritative source для KPI 1 (New OBT adoption).

### Core dashboard: search click → bill paid

Шаги совпадают с сохранёнными чартами Avia flow prod / Hotel flow. Сохранённый RW Flow на дашборде заморожен на июнь 2025 (54 пользователя); rail ниже пересчитан за 30 дней теми же шагами.

| Продукт | Search click | SERP | Следующий шаг | Booking | Paid | Search → paid |
| ------- | -----------: | ---: | ------------- | ------: | ---: | ------------: |
| Avia    |        1 823 | 1 813 | 1 569 offer detail |   1 519 | 1 372 |         75.3% |
| Rail    |          471 |   468 | 349 seat      |     291 |   249 |         52.9% |
| Hotels  |          451 |   434 | 343 room      |     275 |   165 |         36.6% |

Сохранённый [Avia flow prod](https://app.amplitude.com/analytics/internet-tourism/chart/ouqkkhvk) за last 7 days: 963 search → 673 paid = 69.9%. Для базы периода использовать 30 дней.

### KPI оверлея поиска — медиана SERP → следующий шаг

Оверлей убирает лишний клик на правку поиска. Если агенты быстрее уточняют запрос, должна упасть медиана времени с выдачи до карточки. Событий `disclosure_open` / `disclosure_close` нет — это прокси, не прямой A/B.

| Flow | Определение | Baseline median | SERP → next unique | Caveat |
| ---- | ----------- | --------------: | -----------------: | ------ |
| Avia SERP → offer detail | median time between `b2b_flights_serp_page_open` and `b2b_flights_offer_detail_view` | 264 с (4.4 мин); avg 6 244 с | 1 569 / 1 813 = 86.5% | длинный хвост; нет события правки поиска |
| Hotels SERP → room | median `b2b_hotels_serp_page_open` → `b2b_hotels_room_page_open` | 91 с | 343 / 434 = 79.0% | тот же compact editor |
| Rail SERP → seat | median `b2b_rw_serp_page_open` → `b2b_rw_seat_page_open` | 55 с | 349 / 468 = 74.6% | тот же compact editor |

### Объём выдачи (event totals, last 30 days)

| Событие | Totals |
| ------- | -----: |
| `b2b_flights_serp_page_open` | 27 931 |
| `b2b_rw_serp_page_open` | 20 563 |
| `b2b_hotels_serp_page_open` | 4 472 |
| `b2b_flights_offer_detail_view` | 15 677 |
| `b2b_flights_booking_button_click` | 17 715 |
| Pay click (avia) | 9 626 |

Короткая авиа-воронка без search click (ordered, 1 day): SERP 1 838 → offer detail 1 577 → booking 1 528 = **83.1%**. Totals detail 15 677 vs booking 17 715 — часть броней минует `offer_detail_view`.

### Avia SERP unique by `device_type`

User property Amplitude, last 30 days. Сумма рядов 2 053 больше 1 838 unique: часть людей заходит с нескольких устройств.

| device_type | Unique users |
| ----------- | -----------: |
| Windows     |        1 507 |
| Apple iPhone |         276 |
| Mac         |          192 |
| Android     |           61 |
| Linux       |           14 |
| Apple iPad  |            3 |

Desktop OS (Windows + Mac + Linux) ≈ 83% рядов, телефоны ≈ 16%. Мобильный оверлей важен, но основной объём — desktop Web.

### Чего в Amplitude нет

- open/close compact search / overlay disclosure;
- повторный поиск с выдачи vs возврат на главную;
- показ и клик Smart / FC бейджа;
- MICE form_start / submit_success;
- employee drawer_open / save_success.

Эти пробелы нельзя закрыть пересчётом Core dashboard. Повторить воронки через 7–14 дней после выката оверлея и сравнить медиану SERP → detail (сейчас 264 с) и Avia search → paid (сейчас 75.3%).

### Детальный baseline 2026-08-18 — 2026-08-28

Отдельный короткий baseline для будущего сравнения нового поиска сохранён в [amplitude-search-baseline-2026-08-18_2026-08-28.md](./amplitude-search-baseline-2026-08-18_2026-08-28.md).

User-level funnels за окно 2026-08-18 — 2026-08-28 UTC:

| Product | Search users | SERP users | Booking users | Search → SERP | SERP → booking | Search → booking |
|---------|-------------:|-----------:|--------------:|--------------:|----------------:|-----------------:|
| Flights | 1 174 | 1 172 | 916 | 99.8% | 78.2% | 78.0% |
| Hotels | 230 | 222 | 135 | 96.5% | 60.8% | 58.7% |
| Rail | 263 | 262 | 161 | 99.6% | 61.5% | 61.2% |

### Post-check 2026-08-29 — 2026-09-03

Первый post-check нового поиска сохранён в [amplitude-search-comparison-2026-08-29_2026-09-03.md](./amplitude-search-comparison-2026-08-29_2026-09-03.md). Текущий день 2026-09-04 исключён как неполный.

Measured impact:

- Search → SERP стабилен: flights −0,4 pp, hotels −0,4 pp, rail −0,2 pp.
- Flights downstream просел: SERP → booking −3,3 pp, search → booking −3,6 pp.
- Hotels downstream вырос: SERP → booking +3,1 pp, search → booking +2,7 pp.
- Rail downstream вырос: SERP → booking +10,0 pp, search → booking +9,8 pp; выборка меньше baseline.
- Compact editor / repeat search from SERP всё ещё не измеряется: matching events `compact`, `editor`, `overlay`, `repeat`, `serp_search`, `search_editor`, `repeat_search`, `disclosure` в Amplitude project `708958` не найдены.

Demo takeaway: новый поиск не показал поломки входа в выдачу; главный подтверждённый gap — отсутствие instrumentation для прямого эффекта compact editor и repeat search.

## Performance и CI

- [CORP-4533](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1216978052450448): до lazy loading локалей обязательная первоначальная загрузка оценена примерно в 293 KB gzip.
- В той же задаче ожидаемая экономия для ru-flow — около 190 KB gzip. Фактический after-замер не зафиксирован.
- [CORP-4648](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1217234377831058): подготовлено разделение 981 frontend-теста — Node 640, DOM 334, i18n 7; Playwright smoke — 8 тестов.
- Целевые времена CI пока не подтверждены post-rollout измерениями; их нельзя считать достигнутым эффектом.

### CORP-4825 — перенос статики Corporate Travel Portal на C3 CDN

**Дата контрольного замера:** 2026-08-26  
**Задача:** [CORP-4825](https://app.asana.com/1/1208507351529750/project/1210670407720851/task/1217836666953975)  
**Сравнение:** frontend `5b19219a4` → `cc4867c54`; staticfiles `9f06375` → `6f93f1a`

Статика личного кабинета B2B вынесена в отдельный namespace `b2b/corporate-travel-portal`. Контрольный замер выполнен по чистым Git-снимкам до и после миграции.

#### Frontend repository и production build

| Метрика                                     |             До |        После |                 Изменение |
| ------------------------------------------- | -------------: | -----------: | ------------------------: |
| Media-файлы в исходниках                    |            515 |          382 |            −133 / −25,83% |
| Объём media в исходниках                    |      8,318 MiB |    0,875 MiB |      −7,443 MiB / −89,48% |
| Media-файлы в `dist`                        |            175 |           51 |            −124 / −70,86% |
| Объём media в `dist`                        |      7,377 MiB |    0,289 MiB |      −7,088 MiB / −96,08% |
| `dist` без source maps                      |     15,314 MiB |    8,215 MiB |      −7,099 MiB / −46,36% |
| Полный `dist`                               |     39,618 MiB |   32,515 MiB |      −7,103 MiB / −17,93% |
| Initial JS gzip                             |      111,9 KiB |    111,9 KiB |            +45 B / +0,04% |
| Total JS gzip                               |      2,090 MiB |    2,077 MiB |          −13 KiB / −0,59% |
| CSS gzip                                    |      168,6 KiB |    168,6 KiB |            +56 B / +0,03% |
| Кандидаты на неиспользуемые локальные media | 83 / 2,579 MiB | 9 / 18,1 KiB | −74 файла / −99,3% объёма |

Initial JS и CSS практически не изменились: миграция не добавила заметной стоимости в критический frontend bundle. Source maps занимают около 24,3 MiB полного `dist`; это deployment overhead, а не пользовательская загрузка.

#### C3 CDN и целостность миграции

| Метрика                                      |                                        Результат |
| -------------------------------------------- | -----------------------------------------------: |
| Media-файлы в `b2b/corporate-travel-portal`  |                                              132 |
| Объём CDN-каталога                           |                                        7,435 MiB |
| Совпадение удалённых frontend-файлов по hash | 132 из 133; 1 неиспользуемый файл не переносился |
| Покрытие production-маппингом                |                                       132 из 132 |
| HTTP-доступность                             |                     132 из 132 ответили `200 OK` |
| Корректный MIME type                         |                                       132 из 132 |
| `ETag` и `Last-Modified`                     |                                       132 из 132 |
| Cache-Control                                |              132 из 132: `public, max-age=14400` |
| Повторный прогон CDN cache                   |                                 132 из 132 `HIT` |
| Warm CDN TTFB                                |              mean 168 ms; p50 141 ms; p95 237 ms |
| Фактический transfer полного каталога        |              7,294 MiB; −1,90% к repository size |

В коде используются 57 точных URL-маппингов и 75 динамических IATA-обложек городов. CDN-сирот и потерь при переносе не обнаружено. Единственный удалённый файл без hash-копии на CDN — неиспользуемый `default.webp` размером 8,3 KiB.

#### Распределение CDN-каталога

| Домен            | Файлы |     Объём |
| ---------------- | ----: | --------: |
| City covers      |    75 | 2,617 MiB |
| Search loader    |     1 | 1,642 MiB |
| Early access     |    18 | 1,206 MiB |
| Referral         |    16 | 0,822 MiB |
| Search hero      |     6 | 0,489 MiB |
| Остальные домены |    16 | 0,659 MiB |

#### Верификация и ограничения

- Production build до и после миграции прошёл успешно.
- Audit tests: 3 из 3; targeted Vitest: 18 из 18.
- Live CDN-проверка выполнена для всех 132 URL с машины разработчика.
- Full-catalog прогон синтетический: ни одна продуктовая страница не загружает все 132 файла одновременно.
- LCP, CLS и route-level transferred bytes не измерялись: для этого нужен staging/production-сценарий с авторизацией и реальными данными.
- Следующий наиболее заметный кандидат на оптимизацию — WebM loader размером 1,642 MiB; отдельно можно исключить source maps из runtime image и увеличить cache TTL для versioned assets.
