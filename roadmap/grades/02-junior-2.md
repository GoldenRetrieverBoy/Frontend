# Roadmap: Junior 2

[Все уровни](README.md) · [Прогресс](../progress.md) · [Источник и соответствие](../matrix-coverage.md)

**Глубина ответа:** Объяснить механизм, разобрать ошибку и граничный случай.

Этот маршрут показывает требования, которые добавляются на уровне. Предыдущие уровни остаются обязательными. Повторный ID означает углубление того же вопроса, а не новый разбор.

Условные SSR/BFF/Graphite-темы проходят при наличии такого стека; иначе укажи причину «не применимо» в журнале.

**Предыдущий уровень:** [Junior 1](01-junior-1.md). Быстро проверь базу; заново проходи только пробелы.

## Порядок занятия

Открой следующий вопрос → ответь без чтения → разбери пример → выполни практику → запиши результат в журнал. Ответы и примеры открываются по ссылке непосредственно на нужный раздел.

## Технические вопросы

1. [ARC-01 — Инкапсуляция, полиморфизм, наследование и композиция — зачем?](../../engineering/architecture.md#arc-01) — углубление; строки Excel: 6.
2. [TS-02 — Когда type, interface, union и intersection?](../../fundamentals/typescript.md#ts-02) — углубление; строки Excel: 6.
3. [TEST-04 — Как тестировать async и таймеры без flaky-тестов?](../../engineering/testing.md#test-04) — впервые в маршруте; строки Excel: 27.
4. [TEST-05 — Что проверять в компоненте?](../../engineering/testing.md#test-05) — впервые в маршруте; строки Excel: 28.
5. [OPS-01 — Что нужно понимать в Linux и терминале?](../../platform/delivery-node.md#ops-01) — углубление; строки Excel: 34.
6. [NET-04 — Как работают HTTP-кэш и CDN?](../../platform/networking.md#net-04) — впервые в маршруте; строки Excel: 53.
7. [NET-05 — Что такое CORS и preflight?](../../platform/networking.md#net-05) — углубление; строки Excel: 53.
8. [NET-06 — Content-Type, multipart, cookies и HTTPS — что важно?](../../platform/networking.md#net-06) — углубление; строки Excel: 53.
9. [NET-02 — Чем TCP отличается от UDP и где WebSocket?](../../platform/networking.md#net-02) — впервые в маршруте; строки Excel: 54.
10. [ALG-02 — Object, Map, Set, tuple и Record — что различается?](../../fundamentals/algorithms.md#alg-02) — углубление; строки Excel: 97.
11. [ALG-03 — Стек, очередь и связный список — где пригодятся?](../../fundamentals/algorithms.md#alg-03) — впервые в маршруте; строки Excel: 98.
12. [ALG-04 — DFS, BFS и рекурсия — как выбрать?](../../fundamentals/algorithms.md#alg-04) — впервые в маршруте; строки Excel: 99, 100.
13. [ALG-05 — Как найти кратчайший путь?](../../fundamentals/algorithms.md#alg-05) — впервые в маршруте; строки Excel: 100.
14. [UI-02 — Как сделать доступную форму и диалог?](../../frontend/html-css-ui.md#ui-02) — углубление; строки Excel: 107.
15. [UI-06 — BEM, utility first и состояния — как выбрать?](../../frontend/html-css-ui.md#ui-06) — углубление; строки Excel: 111.
16. [JS-01 — Что такое замыкание?](../../fundamentals/javascript.md#js-01) — впервые в маршруте; строки Excel: 117.
17. [JS-02 — От чего зависит this?](../../fundamentals/javascript.md#js-02) — углубление; строки Excel: 117.
18. [JS-09 — Как устроены прототипы, new и классы?](../../fundamentals/javascript.md#js-09) — углубление; строки Excel: 117.
19. [JS-04 — Блокирует ли await поток?](../../fundamentals/javascript.md#js-04) — углубление; строки Excel: 118.
20. [JS-05 — Как устранить гонку ответов поиска?](../../fundamentals/javascript.md#js-05) — впервые в маршруте; строки Excel: 118.
21. [JS-12 — Как распространяются ошибки в Promise?](../../fundamentals/javascript.md#js-12) — углубление; строки Excel: 118.
22. [VUE-05 — Когда slots, provide/inject и attrs?](../../frontend/vue.md#vue-05) — впервые в маршруте; строки Excel: 125.
23. [VUE-06 — Зачем key, v-if/v-show и async components?](../../frontend/vue.md#vue-06) — углубление; строки Excel: 125.
24. [VUE-08 — Что возвращает render-функция и когда нужен h()?](../../frontend/vue.md#vue-08) — впервые в маршруте; строки Excel: 125.
25. [TS-03 — Что дают generics и ограничения?](../../fundamentals/typescript.md#ts-03) — впервые в маршруте; строки Excel: 131.
26. [TS-05 — Как устроены mapped types и utility types?](../../fundamentals/typescript.md#ts-05) — впервые в маршруте; строки Excel: 131.
27. [TS-06 — Как работают conditional types, infer и рекурсивные типы?](../../fundamentals/typescript.md#ts-06) — впервые в маршруте; строки Excel: 131.
28. [TOOL-02 — Как работает bundler и чем dev отличается от build?](../../engineering/tooling-git.md#tool-02) — впервые в маршруте; строки Excel: 136.
29. [TOOL-04 — Зачем линтер и monorepo?](../../engineering/tooling-git.md#tool-04) — углубление; строки Excel: 137, 138.
30. [WEB-03 — Cookies, WebStorage и IndexedDB — что выбрать?](../../frontend/browser-web-api.md#web-03) — впервые в маршруте; строки Excel: 149.
31. [PERF-04 — Как ускорить ресурсы, список и рендер?](../../platform/performance-monitoring.md#perf-04) — углубление; строки Excel: 175.

## Поведенческие вопросы

- [SOFT-008 — Как объяснить нетехническому менеджеру причину задержки?](../../engineering/behavioural.md#soft-008)
- [SOFT-009 — Как провести обсуждение инцидента, когда коллеги обвиняют друг друга?](../../engineering/behavioural.md#soft-009)
- [SOFT-043 — Чем планирование итерации помогает при меняющихся требованиях?](../../engineering/behavioural.md#soft-043)
- [SOFT-044 — Процесс команды кажется лишним. Можно ли его пропустить?](../../engineering/behavioural.md#soft-044)
- [SOFT-045 — Срок релиза наступил, а согласованные проверки DoD не пройдены. Что делать?](../../engineering/behavioural.md#soft-045)
- [SOFT-049 — Как заметить срыв дедлайна до последнего дня?](../../engineering/behavioural.md#soft-049)
- [SOFT-054 — Бизнес просит срок до исследования интеграции. Как участвовать в оценке?](../../engineering/behavioural.md#soft-054)
- [SOFT-087 — Как предложить решение проблемы без готового указания от лида?](../../engineering/behavioural.md#soft-087)

## Ответственность уровня

- Правильно оценивает типовые задачи
- Пишет документацию
- Проводит код ревью

## Завершение уровня

Проведи мини-интервью: три технических вопроса без подготовки, одна новая практическая задача и один поведенческий сценарий. Проверь результат по разбору, зафиксируй пробелы и дату повторения в журнале.

Далее: [Junior 3](03-junior-3.md).
