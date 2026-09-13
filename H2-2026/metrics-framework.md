# Metrics framework — H2 2026

**Цель:** регулярно доказывать не только объём delivery, но и влияние работы на пользователей, продукт, качество и бизнес.  
**Связанные документы:** [metrics.md](./metrics.md), [Asana-срез](./asana-tasks.md), [demos](./demos/README.md)

## Принцип

Метрики разделяются на четыре слоя:

1. **Delivery evidence** — что действительно сделано и выведено в production.
2. **Product outcome** — начали ли пользователи применять capability и завершают ли сценарий.
3. **Quality guardrails** — не выросли ли ошибки, инциденты или UX friction.
4. **Business / operational impact** — bookings, GMV, заявки, экономия времени или снижение ручной работы.

Story points и количество задач подтверждают объём, но сами по себе не являются импактом.

## Основные KPI

### KPI 1. New OBT adoption

**Определение**

Количество успешно завершённых eligible B2B-заказов в New OBT / все успешно завершённые eligible B2B-заказы.

**Разрезы**

- авиа / ЖД / отели;
- компания;
- неделя / месяц;
- обычный и multi-city маршрут;
- New OBT / legacy.

**Зачем**

Показывает, превращается ли delivery нового OBT в реальное использование.

**Источник**

Backend orders / BI warehouse. Amplitude может быть диагностическим источником, но не заменяет backend fact успешного заказа.

**Нужно получить**

- таблицу или dashboard заказов;
- признак канала New OBT / legacy;
- eligibility rules;
- order status и completion timestamp;
- GMV, если доступен.

**Guardrails**

- booking failure rate;
- cancel/refund rate;
- incident rate;
- возвраты пользователя в legacy.

### KPI 2. End-to-end completion rate

**Определение**

Количество успешных завершений выбранного flow / количество стартов этого flow.

**Flow-specific варианты**

| Flow | Start | Success |
|------|-------|---------|
| MICE | form_start | request_submit_success |
| Multi-city | search_submit с route_type=ML | booking/payment success |
| Employee drawer | drawer_open | employee_save_success и возврат в исходный flow |
| Rail refund | refund_init | refund_commit_success |
| Search with children | search с child/infant | booking success |

**Зачем**

Показывает, приносит ли новая функциональность пользователю законченную ценность, а не только существует в интерфейсе.

**Источник**

Product analytics events + backend success events.

**Guardrails**

- validation error rate;
- API error rate;
- abandon rate;
- duplicate request rate;
- p95 duration flow.

### KPI 3. Production quality rate

**Определение**

Доля production deliveries без blocker/critical regression в течение 14 дней после release.

Формула:

Production items without P0/P1 regression in 14 days / all production items.

**Зачем**

Связывает скорость delivery с устойчивостью rollout.

**Источник**

Asana bug links, incident tracker и release date.

**Guardrails**

- количество blocker/critical bugs;
- mean time to recovery;
- reopened task rate;
- escaped defects per release.

## Driver metrics

| Driver | Определение | Источник | Cadence |
|--------|-------------|----------|---------|
| Capability usage | Уникальные пользователи/компании, использовавшие новую функцию | Analytics / backend | еженедельно |
| Time to production | TR-DateProduction − TR-DateInProgress | Asana | по спринту |
| Review cycle time | first review − MR opened | GitLab | по спринту |
| Release lead time | production − MR opened | GitLab + Asana | по спринту |
| Ready-to-release queue | задачи со статусом ready и их возраст | Asana | еженедельно |
| Testing failure rate | tasks with testing error / tasks entering testing | Asana | по спринту |
| CI critical path | pipeline finished − pipeline started | GitLab | еженедельно |
| MR quality gates | доля MR с успешными lint/typecheck/unit/i18n checks | GitLab | еженедельно |

## Guardrail metrics

| Guardrail | Формула / определение | Источник |
|-----------|-----------------------|----------|
| Booking error rate | failed booking requests / booking attempts | Backend / monitoring |
| Client error rate | frontend errors / active sessions | Error monitoring |
| Legacy fallback | sessions returning from New OBT to old flow / New OBT sessions | Analytics |
| Incident count | P0/P1 incidents after release | Incident tracker |
| Refund failure rate | failed refund commits / refund commit attempts | Backend |
| Privacy readiness | Legal approval + privacy notice + runtime consent configuration | Legal / product / docs |

## Workstream measurement plan

### MICE

**Primary:** successful requests per week.  
**Conversion:** request_submit_success / form_start.  
**Drivers:** tab opens, service selection, venue-help selection.  
**Guardrails:** submit error rate, duplicate requests, p95 submit latency.  
**Business layer:** qualified leads, converted bookings, GMV.

### Employee drawer

**Primary:** employee_save_success / drawer_open.  
**Drivers:** opens by source flow, create/edit split, validation attempts.  
**Guardrails:** save errors, flow abandonment, repeated drawer opens.  
**Expected operational impact:** меньше переходов в кабинет и повторного ввода; измерять только после появления событий.

### Multi-city aviation

**Primary:** successful ML bookings per week.  
**Conversion:** booking success / ML search.  
**Drivers:** offers shown, details opened, payment started.  
**Guardrails:** search errors, pricing errors, booking failure, fallback to legacy.  
**Business layer:** ML GMV and incremental bookings.

### Rail post-sale

**Primary:** successful refund commits / refund starts.  
**Drivers:** init success, tickets selected, confirmation started.  
**Guardrails:** double commit, unclear status, support contacts, refund failure rate.

### Localization

**Primary:** successful completed flows by locale.  
**Drivers:** active users and sessions by ru/kk/en.  
**Guardrails:** missing translation keys, locale fallback rate, locale-related errors.  
**Technical measurement:** actual locale bundle before/after, not expected estimate.

### CI / platform

**Primary:** MR pipeline p50/p95 and develop-to-deploy p50/p95.  
**Drivers:** cache hit rate, queue time, test shard duration.  
**Guardrails:** flaky retry rate, CI minutes, bypassed quality gates, failed production build.

## Source map

| Source | Что можем получить | Read access | Состояние данных | Следующее действие |
|--------|--------------------|-------------|------------------|--------------------|
| Asana | задачи, SP, status, production dates, cycle fields, bugs | есть | данные доступны | обновлять weekly snapshot |
| Demo notes | qualitative feedback, decisions, follow-up | есть | структура готова | заполнять после каждого demo |
| GitLab | MRs, reviews, commits, pipelines, CI duration | нет | не проверено | дать API/connector access и GitLab username |
| Backend / BI | bookings, GMV, orders, refunds, New OBT adoption | нет | источник не определён | определить dashboard/table owner |
| Product analytics | starts, success, drop-off, feature usage | есть (Amplitude B2B prod `708958`, org Internet Tourism) | Core dashboard инвентаризирован 2026-08-28; baseline search→paid и SERP→next снят | повторить воронки через 7–14 дней после выката оверлея; добавить события disclosure / MICE / employee drawer / FC badge |
| Monitoring | frontend/backend errors, incidents, latency | нет | источник не определён | определить Sentry/logs/observability source |
| CRM / operations | ручное время, SLA, service fee corrections | нет | источник не определён | определить owner и метод выгрузки |
| Legal / privacy | разрешение Session Replay и privacy notice | не применимо | approval pending | получить formal approval before production rollout |

## Metric contract

Каждая метрика, попадающая в [metrics.md](./metrics.md), должна иметь:

| Поле | Что фиксировать |
|------|-----------------|
| Name | стабильное название |
| Decision | какое решение меняется при росте/падении |
| Definition | точная формула |
| Numerator | числитель |
| Denominator | знаменатель |
| Grain | user / session / order / task / MR |
| Dimensions | product, company, locale, channel |
| Source of truth | таблица, dashboard или API |
| Window | день / неделя / месяц / 14 days post-release |
| Owner | кто подтверждает определение |
| Baseline | значение до изменения |
| Current | последнее значение |
| Target | только после появления baseline |
| Evidence | query, dashboard или permalink |
| Caveats | исключения и ограничения |

## Cadence обновления

### После каждого демо

- заполнить feedback, решения и follow-up в завершённом demo-файле;
- обновить статус demo в [индексе](./demos/README.md);
- зафиксировать, что реально было показано;
- создать follow-up tasks;
- не переносить ожидаемый эффект в highlights как факт.

### Еженедельно

- обновить Asana status snapshot;
- закрытые production items и SP;
- live pipeline: in progress / testing / ready / blockers;
- stale parent/subtask statuses;
- при наличии GitLab — MR и CI metrics.

### Ежемесячно

- New OBT adoption;
- conversion по ключевым flows;
- bookings / GMV;
- quality guardrails;
- накопленный operational effect.

### Перед performance review

- зафиксировать immutable snapshot периода;
- проверить определения и источники;
- отделить measured impact от forecast;
- выбрать 5–10 достижений с лучшей доказательной базой.

## Порядок внедрения

### Этап 0 — уже работает

- Asana delivery и live pipeline.
- Demo notes.
- Manual impact curation.
- Дедупликация parent/subtask.

### Этап 1 — GitLab evidence

Нужно подключить GitLab и получить:

- созданные и merged MR пользователя;
- количество review;
- first review time;
- merge cycle time;
- pipeline p50/p95;
- quality gate pass rate.

### Этап 2 — product instrumentation

**Сделано 2026-08-28:** доступ к Amplitude B2B prod, audit существующих воронок Core dashboard, baseline last 30 days.

Уже есть в прод-телеметрии (имена точные):

- авиа: `b2b_flights_search_button_click` → `b2b_flights_serp_page_open` → `b2b_flights_offer_detail_view` → `b2b_flights_booking_button_click` → `b2b_flights_payment_page_open` → `b2b_travel_bill_paid`;
- ЖД: `b2b_rw_search_button_click` → `b2b_rw_serp_page_open` → `b2b_rw_seat_page_open` → `b2b_rw_booking_page_open` → `b2b_rw_payment_page_open` → `b2b_rw_pay_button_click` → `b2b_travel_bill_paid`;
- отели: `b2b_hotels_search_button_click` → `b2b_hotels_serp_page_open` → `b2b_hotels_room_page_open` → `b2b_hotels_booking_page_open` → `b2b_hotels_payment_page_open` → `b2b_hotels_pay_button_click` → `b2b_travel_bill_paid`.

Ещё нет — согласовать события:

- search_editor_open / search_editor_close (или эквивалент disclosure);
- mice_tab_open, mice_form_start, mice_submit_success, mice_submit_error;
- employee_drawer_open, employee_save_success, employee_save_error;
- search_submit с passenger mix и route type;
- booking_success / booking_error;
- rail_refund_init / rail_refund_commit_success;
- fc_offer_impression / fc_offer_click.

Не передавать персональные данные, ФИО, документы, телефон или email.

### Этап 3 — BI / business impact

Подключить authoritative source заказов и заявок:

- New OBT adoption;
- bookings и GMV;
- MICE leads и conversion to booking;
- multi-city bookings и GMV;
- refund success;
- экономия ручного времени.

## Ближайшие действия

1. После demo 0.0.11 заполнить feedback и реальные follow-up.
2. Определить владельца Backend/BI данных по orders и GMV.
3. Получить GitLab read access или согласовать безопасную выгрузку.
4. Amplitude access подтверждён. Снят baseline 2026-08-28: см. [metrics.md](./metrics.md#product-analytics-baseline--amplitude-b2b). Нет событий disclosure, MICE form, employee drawer, FC badge — согласовать instrumentation.
5. Согласовать с Legal production rollout Session Replay.
6. Через 7–14 дней после выката оверлея сравнить медиану SERP → detail (264 с) и Avia search → paid (75.3%) с этим снимком. Числовые targets не ставить до post-release окна.
