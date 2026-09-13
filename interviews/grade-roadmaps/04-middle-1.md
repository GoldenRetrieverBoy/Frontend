# Roadmap: Middle 1

[Все уровни](README.md) · [Прогресс](../progress.md) · [Источник и соответствие](../matrix-coverage.md)

**Глубина ответа:** Самостоятельно выбрать решение с учётом зависимостей, тестов и сопровождения.

Этот маршрут показывает требования, которые добавляются на уровне. Предыдущие уровни остаются обязательными. Повторный ID означает углубление того же вопроса, а не новый разбор.

Условные SSR/BFF/Graphite-темы проходят при наличии такого стека; иначе укажи причину «не применимо» в журнале.

**Предыдущий уровень:** [Junior 3](03-junior-3.md). Быстро проверь базу; заново проходи только пробелы.

## Порядок занятия

Открой следующий вопрос → ответь без чтения → разбери пример → выполни практику → запиши результат в журнал. Ответы и примеры открываются по ссылке непосредственно на нужный раздел.

## Технические вопросы

1. [ARC-01 — Инкапсуляция, полиморфизм, наследование и композиция — зачем?](../../engineering/architecture.md#arc-01) — углубление; строки Excel: 7.
2. [ARC-10 — Чем императивный, декларативный и функциональный подходы отличаются на одном примере?](../../engineering/architecture.md#arc-10) — впервые в маршруте; строки Excel: 8.
3. [JS-11 — Что такое чистая функция и когда допустима мутация?](../../fundamentals/javascript.md#js-11) — углубление; строки Excel: 8.
4. [OPS-03 — Volumes, networks, registry и Compose — зачем?](../../platform/delivery-node.md#ops-03) — углубление; строки Excel: 15, 16, 17.
5. [TOOL-06 — Merge, rebase и cherry-pick — как выбрать?](../../engineering/tooling-git.md#tool-06) — углубление; строки Excel: 39.
6. [TOOL-10 — Как защитить репозиторий, секреты и pipeline?](../../engineering/tooling-git.md#tool-10) — впервые в маршруте; строки Excel: 44.
7. [OPS-05 — Как строить CI/CD и разделять окружения?](../../platform/delivery-node.md#ops-05) — впервые в маршруте; строки Excel: 45.
8. [SEC-03 — JWT, OAuth, OIDC и SSO — одно и то же?](../../platform/security.md#sec-03) — впервые в маршруте; строки Excel: 64.
9. [ARC-03 — Какие паттерны реально применяются на Frontend?](../../engineering/architecture.md#arc-03) — углубление; строки Excel: 75, 76.
10. [ARC-02 — Как применять SOLID без лишних абстракций?](../../engineering/architecture.md#arc-02) — углубление; строки Excel: 76, 93.
11. [ALG-02 — Object, Map, Set, tuple и Record — что различается?](../../fundamentals/algorithms.md#alg-02) — углубление; строки Excel: 101.
12. [JS-06 — Почему возникают утечки памяти?](../../fundamentals/javascript.md#js-06) — впервые в маршруте; строки Excel: 101, 121.
13. [ALG-01 — Как оценивать сложность?](../../fundamentals/algorithms.md#alg-01) — впервые в маршруте; строки Excel: 102.
14. [ALG-06 — Что знать о сортировках и бинарном поиске?](../../fundamentals/algorithms.md#alg-06) — впервые в маршруте; строки Excel: 102.
15. [JS-17 — Что нужно знать о JIT и движке?](../../fundamentals/javascript.md#js-17) — впервые в маршруте; строки Excel: 121.
16. [VUE-01 — Как работает реактивность и чем ref отличается от reactive?](../../frontend/vue.md#vue-01) — впервые в маршруте; строки Excel: 126.
17. [VUE-05 — Когда slots, provide/inject и attrs?](../../frontend/vue.md#vue-05) — углубление; строки Excel: 127.
18. [TOOL-04 — Зачем линтер и monorepo?](../../engineering/tooling-git.md#tool-04) — углубление; строки Excel: 140.
19. [OPS-09 — Условный блок: SSR/BFF, кэш, профилирование памяти](../../platform/delivery-node.md#ops-09) — впервые в маршруте; строки Excel: 144, 145.
20. [ARC-07 — Cloud, S3, CDN, BFF и API — как связаны?](../../engineering/architecture.md#arc-07) — углубление; строки Excel: 144.
21. [PERF-07 — Условный блок: Graphite и серверные метрики](../../platform/performance-monitoring.md#perf-07) — впервые в маршруте; строки Excel: 145.
22. [WEB-04 — Когда нужен Web Worker?](../../frontend/browser-web-api.md#web-04) — впервые в маршруте; строки Excel: 150.
23. [WEB-03 — Cookies, WebStorage и IndexedDB — что выбрать?](../../frontend/browser-web-api.md#web-03) — углубление; строки Excel: 151.
24. [OPS-06 — Как NGINX отдаёт SPA и проксирует API?](../../platform/delivery-node.md#ops-06) — впервые в маршруте; строки Excel: 159.
25. [WEB-06 — Как загружаются script, async, defer и ресурсы?](../../frontend/browser-web-api.md#web-06) — углубление; строки Excel: 178.
26. [PERF-04 — Как ускорить ресурсы, список и рендер?](../../platform/performance-monitoring.md#perf-04) — углубление; строки Excel: 178.

## Поведенческие вопросы

- [SOFT-019 — Как согласовать работу Frontend, Backend и QA по новой функции?](../../engineering/behavioural.md#soft-019)
- [SOFT-020 — Как сделать взаимопомощь регулярной, не превращая её в отвлечения?](../../engineering/behavioural.md#soft-020)
- [SOFT-021 — Как повлиять на план команды без формальной роли лида?](../../engineering/behavioural.md#soft-021)
- [SOFT-026 — Как сократить Time to Market без пропуска проверок?](../../engineering/behavioural.md#soft-026)
- [SOFT-027 — Какая документация нужна вместе с задачей?](../../engineering/behavioural.md#soft-027)
- [SOFT-036 — Как сообщить менеджеру о внезапной недоступности зависимости?](../../engineering/behavioural.md#soft-036)
- [SOFT-050 — Как не откладывать тесты и мониторинг до конца релиза?](../../engineering/behavioural.md#soft-050)
- [SOFT-051 — Support принёс жалобу без воспроизведения. Как обработать обращение?](../../engineering/behavioural.md#soft-051)
- [SOFT-058 — Как самостоятельно вести задачу с неизвестными частями?](../../engineering/behavioural.md#soft-058)
- [SOFT-067 — Ты видишь повторяющуюся проблему без назначенного владельца. Что делать?](../../engineering/behavioural.md#soft-067)
- [SOFT-068 — Как внедрить улучшение процесса, а не только предложить его?](../../engineering/behavioural.md#soft-068)
- [SOFT-069 — Как провести техническое интервью объективно?](../../engineering/behavioural.md#soft-069)
- [SOFT-072 — Алерты приходят ежедневно, но команда их игнорирует. Как действовать?](../../engineering/behavioural.md#soft-072)
- [SOFT-077 — Как понять, что онбординг нового разработчика работает?](../../engineering/behavioural.md#soft-077)
- [SOFT-079 — Как поддерживать базу знаний полезной?](../../engineering/behavioural.md#soft-079)
- [SOFT-080 — Как подготовить внутренний доклад, после которого команда сможет применить знание?](../../engineering/behavioural.md#soft-080)
- [SOFT-088 — Как сравнить несколько решений до реализации?](../../engineering/behavioural.md#soft-088)
- [SOFT-097 — Как использовать статистику багов для улучшения качества?](../../engineering/behavioural.md#soft-097)
- [SOFT-098 — Как делегировать задачу, чтобы не переделывать её в конце?](../../engineering/behavioural.md#soft-098)

## Ответственность уровня

- Поиск в code review слабых мест в коде
- Решение сложных багов
- Закрытие технического долга

## Завершение уровня

Проведи мини-интервью: три технических вопроса без подготовки, одна новая практическая задача и один поведенческий сценарий. Проверь результат по разбору, зафиксируй пробелы и дату повторения в журнале.

Далее: [Middle 2](05-middle-2.md).
