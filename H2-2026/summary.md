# Performance Review — H2 2026

**Период:** 2026-07-01 — 2026-08-28  
**Статус:** interim review  
**Ближайшее демо:** 2026-08-28, релиз 0.0.11  
**Источники:** [Asana-срез](./asana-tasks.md), [метрики](./metrics.md), [highlights](./highlights.md), [Demo 0.0.11](./demos/2026-08/0.0.11-new-obt-demo.md), Amplitude B2B `708958`

## Общий обзор

В июле–августе основной вклад был направлен на production readiness нового OBT: стабилизацию пользовательских воронок, расширение продуктовых сценариев и укрепление frontend foundation. В production вышло 111 task records; после исключения очевидного двойного учёта parent/subtask — 96 delivery items и 302 SP.

Главный подтверждённый результат — capability delivery: единый layout, multi-city авиа, ЖД post-sale, employee/guest flow, ru/kk/en, MICE MVP, компакт-поиск на выдаче (2 действия → 1), перенос статики Corporate Travel Portal на C3 CDN и техническая интеграция observability. 28 августа снят Amplitude baseline критичных воронок; бизнес-эффект оверлея и Smart-бейджа ещё нельзя считать измеренным.

## Технический импакт

### Production readiness нового OBT

Закрыто 30 дедуплицированных задач / 70 SP из фронтового bug epic. Исправления покрывают кабинет, документы, настройки компании, поездки, auth, сотрудников, ЖД и общие UI-состояния.

**Ожидаемый импакт:** меньше блокирующих и визуальных дефектов перед rollout, более согласованный UX и меньше возвратов в legacy-сценарии. Фактический эффект нужно подтвердить error rate и navigation analytics.

### Сквозные travel flows

- [CORP-3783](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1215496524558181), 34 SP: единый layout без прыжков между авиа, ЖД, отелями, трансферами и shell.
- [CORP-3841](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1215581144897702), 13 SP: multi-city авиа от выдачи до оплаты.
- [CORP-4471](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1216843138867579), 8 SP: ЖД post-sale и возврат из деталей заказа.

### Employee / guest

Guest-поддержка доведена в list/create/details и закреплена в доменном контракте. В релизе 0.0.11 один employee drawer используется в кабинете, авиа, ЖД и отелях; повторный авиапоиск с другим составом больше не конфликтует с предыдущим запросом.

**Подтверждённый capability:** единая форма работает без перехода в кабинет. Ожидаемый эффект — меньше прерываний booking flow; его нужно подтвердить funnel/error analytics.

### Platform engineering

- Node.js 24.15.0 и обновлённые зависимости.
- Hardened CI image, npm audit = 0, production build.
- 165 файлов / 688 unit-тестов в migration task.
- Единые ESLint, shared UI, Storybook и architecture contracts.
- Подготовлено разделение 981 frontend-теста и обязательные quality gates.
- Статика Corporate Travel Portal вынесена в отдельный C3 CDN namespace: media в production `dist` уменьшились на 96,08%, а `dist` без source maps — на 46,36%; live-проверка подтвердила доступность и cache headers для всех 132 ресурсов.

**Ожидаемый импакт:** ниже security/compatibility risk и архитектурный drift. CI-ускорение нужно подтвердить после rollout; точные technical numbers взяты из task reports.

## Продуктовый импакт

### Demo 0.0.11

- **Мероприятия:** self-service форма MICE на главной реализована вместо старого Google Form и подготовлена к release 0.0.11.
- **Единый drawer:** одинаковое управление сотрудником во всех ключевых flows.
- **Дети в поиске:** корректная поддержка детей и младенцев по возрасту документа.
- **ФИО из документа:** авиа показывает паспортное имя, снижая риск расхождения профиля и документа.
- **Длинные имена:** устранён дефект выбора сотрудника.
- **Повторный поиск:** устранён race condition при смене состава пассажиров.

### Другие H2 capabilities

- Трёхъязычный ru/kk/en интерфейс.
- Session Replay и Clarity технически интегрированы; production rollout ожидает Legal approval и обновления privacy notice.
- Более точные сервисные сборы, статьи расходов, суммы без СС и фильтры CRM.
- Компактный поиск на выдаче: клик по сегменту сразу открывает нужное поле (2 → 1), форма оверлеем, без прыжка списка. Влит 28 августа; в Amplitude нет событий disclosure.
- Отдельная вкладка заказов и меньше legacy-переходов.

28 августа подтверждён доступ к Amplitude B2B prod и снят baseline: Avia search → paid **75.3%** (1 823 → 1 372 unique / 30 дней), медиана SERP → offer detail **264 с**. Rail search → paid 52.9%, hotels 36.6%. Это текущий прод до выката оверлея, не A/B. Revenue/GMV и New OBT adoption по-прежнему требуют backend/BI; Amplitude их не заменяет.

## Что сейчас в работе

- Пять задач находятся на тестировании, одна не прошла тестирование.
- Шесть live-задач готовы к релизу. CORP-4076 находится в archive и в live count не включён.

CORP-4825 реализована; её технические результаты зафиксированы в [метриках](./metrics.md#corp-4825--перенос-статики-corporate-travel-portal-на-c3-cdn). Остальной live status взят из предыдущего [Asana-среза](./asana-tasks.md) и требует обновления перед финальной оценкой периода.

## Что запланировано

1. Актуализировать [CORP-4838](https://app.asana.com/1/1208507351529750/project/1210670407720851/task/1217857878635406): переключение media уже реализовано и измерено в рамках CORP-4825.
2. Закрыть blockers и открытые баги New OBT, включая password reset link и service fee.
3. Через 7–14 дней после выката оверлея сравнить медиану SERP → detail (база 264 с) и Avia search → paid (база 75.3%) с этим снимком.
4. Зафиксировать post-release метрики по MICE, multi-city и New OBT rollout — для MICE событий в Amplitude ещё нет.
5. Собрать route-level transferred bytes, LCP и cache-hit ratio для CDN-assets на production traffic.

CORP-3007 (ЖД-возврат init/commit, 4 SP) находится в archive S41 со статусом backlog. Он не считается текущим планом, пока актуальность не подтверждена.

## Метрики

| Метрика                            |             Значение |
| ---------------------------------- | -------------------: |
| Production task records            |                  111 |
| Delivery items после дедупликации  |                   96 |
| Story points после дедупликации    |                  302 |
| New OBT bug epic                   |     30 задач / 70 SP |
| Сокращение media в production dist | −7,088 MiB / −96,08% |
| Сокращение dist без source maps    | −7,099 MiB / −46,36% |
| Проверенные CDN-assets             |            132 / 132 |
| Avia search → paid (Amplitude, 30d) |                75.3% |
| Медиана Avia SERP → detail         |               264 с |
| Unique avia SERP users (30d)       |                1 838 |
| В работе                           |                    1 |
| На тестировании                    |                    6 |
| Готово к релизу                    |                    6 |
| Открыто / blocker                  |                    3 |
| Запланировано                      |                    1 |
| Без workflow status                |                    1 |

## Зоны роста

- Связывать technical delivery с post-release продуктовой метрикой.
- Синхронизировать parent/subtask statuses после релиза.
- Фиксировать фактический before/after для performance и CI.
- Добавлять dashboard/MR links и metric owner сразу при завершении задачи.

## Цели до следующего обновления

1. Обновить demo 0.0.11 после показа 28 августа и записать feedback.
2. Закрыть текущие testing/ready задачи и blockers.
3. Сравнить Amplitude воронки с baseline от 28 августа; не ставить targets, пока нет post-release окна.
