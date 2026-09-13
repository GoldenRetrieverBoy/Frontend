# Топ достижения — H2 2026

**Период:** 2026-07-01 — 2026-08-28  
**Статус:** промежуточная выжимка; demo 0.0.11 — 2026-08-28  
**Доказательная база:** [Asana-срез](./asana-tasks.md), [Demo 0.0.11](./demos/2026-08/0.0.11-new-obt-demo.md), [метрики Amplitude](./metrics.md#product-analytics-baseline--amplitude-b2b)

1. **Приблизил New OBT к полноценному production rollout** → 30 дедуплицированных задач / 70 SP по кабинету, поездкам, документам, сотрудникам, auth, ЖД и общим UI-состояниям.

2. **Унифицировал layout ключевых travel-вoронок** → единая ширина 1440px и стабильная навигация без layout shift для авиа, ЖД, отелей, трансферов и shell; [34 SP](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1215496524558181).

3. **Добавил полную поддержку сложного авиа-маршрута** → multi-city сценарий проходит через выдачу, детали, бронирование и оплату; [13 SP](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1215581144897702).

4. **Расширил ЖД post-sale capability** → возврат доступен из деталей заказа с новым UX; [8 SP](https://app.asana.com/1/1208507351529750/project/1210670407720856/task/1216843138867579).

5. **Сделал единый employee flow** → guest поддержан в list/create/details, а один drawer переиспользуется в кабинете, авиа, ЖД и отелях без ухода со страницы.

6. **Подготовил MICE MVP к release 0.0.11** → реализованы вкладка «Мероприятия» и собственная форма через Events API вместо старого лендинга с Google Form.

7. **Закрыл критичные детали семейного и паспортного бронирования** → дети и младенцы снова доступны в поиске; в авиа используются ФИО из документа; длинные имена корректно отображаются.

8. **Локализовал ключевые пользовательские сценарии на ru/kk/en** → словари синхронизированы, добавлены parity/quality tests; полноту покрытия подтверждает task report, а не продуктовая аналитика.

9. **Усилил frontend security и platform foundation** → Node.js 24.15.0, hardened image, актуальные зависимости, npm audit = 0, единые UI/architecture contracts.

10. **Перенёс статику Corporate Travel Portal на C3 CDN** → объём media в production `dist` сократился с 7,377 до 0,289 MiB (−96,08%), а `dist` без source maps — с 15,314 до 8,215 MiB (−46,36%). Все 132 CDN-ресурса доступны, имеют корректный MIME и cache headers; повторный контрольный прогон дал 132/132 cache HIT. [Подробные метрики](./metrics.md#corp-4825--перенос-статики-corporate-travel-portal-на-c3-cdn).

11. **Реализовал privacy-safe интеграцию Session Replay и Clarity** → техническая часть готова, но production rollout организационно заблокирован до Legal approval и обновления privacy notice.

12. **Сократил правку поиска на выдаче с двух действий до одного** → клик по сегменту компакт-бара (маршрут / даты / гости) сразу открывает нужное поле; форма — оверлей, список не прыгает. Влит `30b7b0139` 28 августа. Продуктовый эффект ещё не измерен: событий disclosure в Amplitude нет.

13. **Снял Amplitude baseline критичных воронок до выката оверлея** → Core dashboard, last 30 days: Avia search → paid 75.3% (1 823 → 1 372 unique), медиана SERP → offer detail 264 с; rail 52.9%; hotels 36.6%. Это база для сравнения, не импакт релиза.

Точки 1–12 подтверждают capability delivery. Точка 13 — измеренный baseline, не post-release эффект. Утверждения о снижении ошибок, росте conversion, revenue или экономии по-прежнему требуют измерений после выката.

## Требует дополнительной метрики

- Compact search / overlay: медиана SERP → detail/room/seat через 7–14 дней после выката vs baseline 264 / 91 / 55 с; нужны события open/close disclosure.
- MICE: количество отправленных заявок и conversion формы — событий в Amplitude нет.
- Multi-city: поиски, бронирования, GMV и error rate.
- New OBT rollout: активные компании, completed bookings и возвраты в legacy — Amplitude не заменяет backend orders.
- Smart / FC: показы бейджа и клики; capability на ветке, в проде нет.
- i18n: фактический bundle before/after.
- CI: реальные p50/p95 после rollout.
- CDN migration: route-level transferred bytes, LCP и cache-hit ratio на production traffic.
