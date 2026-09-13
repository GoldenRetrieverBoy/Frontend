# Соответствие требований вопросам

Источник: «Технические потребности для разработчиков (back&front&mobile).xlsx», листы `TechSkills Frontend`, `SoftSkills`, `Responsibilities`. Это внутренняя матрица компании, не универсальная шкала рынка. Исходные формулировки ниже сохранены; опечатки не переносятся в названия уроков.

Колонки C–E в Excel сохранены как даты; Junior 1–3 — предположение по порядку, а не подтверждённые подписи. Senior — последний столбец источника, отдельного Top/Lead в нём нет.

Грейд указывает первое появление требования. Уровни накопительные. Связь с уроком означает учебное покрытие, а не освоение. Строки 144–145 и 165 технического листа обязательны при наличии соответствующего SSR/BFF/Node.js-стека; при отсутствии отмечай «не применимо» с причиной в журнале. TODO исходника не включены.

Старые ID карточек сохранены только для поиска по истории; постоянные ID находятся в последней колонке. У одного урока может быть несколько требований и уровней глубины.

| Лист / строка | Первый грейд | Требование | Старый ID | Постоянные вопросы |
|---|---|---|---|---|
| TechSkills Frontend / A3 | Intern: база перед Junior | Знание базовых принципов(Инкапсуляция, Полиморфизм, Наследование) | IN-T001 | [ARC-01](../engineering/architecture.md#arc-01) |
| TechSkills Frontend / A32 | Intern: база перед Junior | Работа с терминалом. Установка пакетов. | IN-T002 | [OPS-01](../platform/delivery-node.md#ops-01) |
| TechSkills Frontend / A33 | Intern: база перед Junior | Редактирование файлов. Права на файлы. | IN-T003 | [OPS-01](../platform/delivery-node.md#ops-01) |
| TechSkills Frontend / A37 | Intern: база перед Junior | Git Basic (clone, add, commit, pull, push, checkout, reset, ssh) | IN-T004 | [TOOL-05](../engineering/tooling-git.md#tool-05) |
| TechSkills Frontend / A83 | Intern: база перед Junior | Клиент-серверная архитектура | IN-T005 | [ARC-07](../engineering/architecture.md#arc-07)<br>[NET-01](../platform/networking.md#net-01) |
| TechSkills Frontend / A96 | Intern: база перед Junior | Массивы, JSON Объекты | IN-T006 | [ALG-02](../fundamentals/algorithms.md#alg-02)<br>[JS-10](../fundamentals/javascript.md#js-10) |
| TechSkills Frontend / A105 | Intern: база перед Junior | Базовые HTML теги и аттрибуты | IN-T007 | [UI-01](../frontend/html-css-ui.md#ui-01) |
| TechSkills Frontend / A106 | Intern: база перед Junior | Семантическая верстка - Понимание влияния на SEO и использование семантически верных элементов с дефолтным поведением. | IN-T008 | [UI-01](../frontend/html-css-ui.md#ui-01) |
| TechSkills Frontend / A110 | Intern: база перед Junior | Знание специфичности, изоляция стилей, каскадность, media queries | IN-T009 | [UI-03](../frontend/html-css-ui.md#ui-03)<br>[UI-04](../frontend/html-css-ui.md#ui-04) |
| TechSkills Frontend / A114 | Intern: база перед Junior | Знать синтаксис (Переменные, Типы данных, Функции, Классы, Модули, Обработка ошибок) | IN-T010 | [JS-18](../fundamentals/javascript.md#js-18)<br>[JS-07](../fundamentals/javascript.md#js-07)<br>[JS-08](../fundamentals/javascript.md#js-08)<br>[JS-09](../fundamentals/javascript.md#js-09)<br>[JS-14](../fundamentals/javascript.md#js-14)<br>[JS-16](../fundamentals/javascript.md#js-16) |
| TechSkills Frontend / A134 | Intern: база перед Junior | Package Manager (npm, yarn) - Умение работать с пакетными менеджерами | IN-T011 | [TOOL-01](../engineering/tooling-git.md#tool-01) |
| TechSkills Frontend / A135 | Intern: база перед Junior | Linter - Придерживаться общепринятых правил для линтеров. | IN-T012 | [TOOL-04](../engineering/tooling-git.md#tool-04) |
| TechSkills Frontend / A148 | Intern: база перед Junior | Работа с DOM древом. | IN-T013 | [WEB-07](../frontend/browser-web-api.md#web-07)<br>[WEB-02](../frontend/browser-web-api.md#web-02) |
| TechSkills Frontend / A155 | Intern: база перед Junior | Обработка интерактивных состояний (hover/active/focus/disabled) | IN-T014 | [UI-06](../frontend/html-css-ui.md#ui-06) |
| SoftSkills / A3 | Intern: база перед Junior | Честность | IN-S001 | [SOFT-003](../engineering/behavioural.md#soft-003) |
| SoftSkills / A4 | Intern: база перед Junior | Вежливость | IN-S002 | [SOFT-004](../engineering/behavioural.md#soft-004) |
| SoftSkills / A5 | Intern: база перед Junior | Умеет задавать правильные вопросы | IN-S003 | [SOFT-005](../engineering/behavioural.md#soft-005) |
| SoftSkills / A6 | Intern: база перед Junior | Способность спокойно относиться к критике | IN-S004 | [SOFT-006](../engineering/behavioural.md#soft-006) |
| SoftSkills / A13 | Intern: база перед Junior | Соблюдать договорённости в команде | IN-S005 | [SOFT-013](../engineering/behavioural.md#soft-013) |
| SoftSkills / A14 | Intern: база перед Junior | Соблюдать приоритеты | IN-S006 | [SOFT-014](../engineering/behavioural.md#soft-014) |
| SoftSkills / A40 | Intern: база перед Junior | Быть вовремя на встречах | IN-S007 | [SOFT-040](../engineering/behavioural.md#soft-040) |
| SoftSkills / A61 | Intern: база перед Junior | Способность и желание обучаться | IN-S008 | [SOFT-061](../engineering/behavioural.md#soft-061) |
| SoftSkills / A66 | Intern: база перед Junior | Проактивен в поиске решения задач | IN-S009 | [SOFT-066](../engineering/behavioural.md#soft-066) |
| TechSkills Frontend / A4 | Junior 1 | Уметь применять базовые принципы | J1-T001 | [ARC-01](../engineering/architecture.md#arc-01) |
| TechSkills Frontend / A5 | Junior 1 | Статистические и классовые методы. Области видимости | J1-T002 | [ARC-01](../engineering/architecture.md#arc-01)<br>[JS-02](../fundamentals/javascript.md#js-02)<br>[JS-09](../fundamentals/javascript.md#js-09) |
| TechSkills Frontend / A23 | Junior 1 | Теория. Принципы и Виды тестирования. Умение писать юнит тесты. | J1-T003 | [TEST-01](../engineering/testing.md#test-01) |
| TechSkills Frontend / A24 | Junior 1 | Функции тестирования. Mocking and Fixtures. | J1-T004 | [TEST-02](../engineering/testing.md#test-02) |
| TechSkills Frontend / A25 | Junior 1 | Coverage | J1-T005 | [TEST-03](../engineering/testing.md#test-03) |
| TechSkills Frontend / A26 | Junior 1 | Параметризированные тесты. | J1-T006 | [TEST-03](../engineering/testing.md#test-03) |
| TechSkills Frontend / A38 | Junior 1 | Git Middle (resolve conflicts, remotes, revert, history, compare revisions and branches) | J1-T007 | [TOOL-05](../engineering/tooling-git.md#tool-05)<br>[TOOL-06](../engineering/tooling-git.md#tool-06) |
| TechSkills Frontend / A43 | Junior 1 | Merge Requests | J1-T008 | [TOOL-08](../engineering/tooling-git.md#tool-08) |
| TechSkills Frontend / A50 | Junior 1 | Базовое знание модели OSI | J1-T009 | [NET-01](../platform/networking.md#net-01) |
| TechSkills Frontend / A51 | Junior 1 | HTTP (Структура запросов/ответов, Cookies, Коды ответов, Multipart, Методы, HTTPS, Авторизация) | J1-T010 | [NET-03](../platform/networking.md#net-03)<br>[NET-06](../platform/networking.md#net-06)<br>[SEC-02](../platform/security.md#sec-02) |
| TechSkills Frontend / A52 | Junior 1 | Умение отправлять запросы. Знать протоколы передачи данных. | J1-T011 | [NET-03](../platform/networking.md#net-03)<br>[NET-06](../platform/networking.md#net-06) |
| TechSkills Frontend / A60 | Junior 1 | XSS (Cross Site Scripting) | J1-T012 | [SEC-01](../platform/security.md#sec-01) |
| TechSkills Frontend / A90 | Junior 1 | Базовые принципы программирования: DRY, KISS, YAGNI | J1-T013 | [ARC-02](../engineering/architecture.md#arc-02) |
| TechSkills Frontend / A115 | Junior 1 | Асинхронность (Callback, Promise, Async/Await, Таймауты и Интервалы) | J1-T014 | [JS-04](../fundamentals/javascript.md#js-04)<br>[JS-12](../fundamentals/javascript.md#js-12)<br>[JS-13](../fundamentals/javascript.md#js-13) |
| TechSkills Frontend / A116 | Junior 1 | FP (Чистые функции, Иммутабельность) Иммутабельность - Умение писать иммутабельный код. Понимать где мутация создают проблемы, где мутации это нормально Чистые функции - Ограниченное наличие сайд эффектов в функциях. Стремится преимущественно писать чистые функции | J1-T015 | [JS-11](../fundamentals/javascript.md#js-11) |
| TechSkills Frontend / A124 | Junior 1 | Basic (Components, Props, Events, Directives, Computed, Watch, Life Cycle Hooks, Templates, CompositionAPI) | J1-T016 | [VUE-02](../frontend/vue.md#vue-02)<br>[VUE-03](../frontend/vue.md#vue-03)<br>[VUE-04](../frontend/vue.md#vue-04)<br>[VUE-06](../frontend/vue.md#vue-06)<br>[VUE-07](../frontend/vue.md#vue-07) |
| TechSkills Frontend / A130 | Junior 1 | Basic - Type annotations - Type/Interface - Type Guards - Union - Intersection - Operators (keyof, typef, const) | J1-T017 | [TS-01](../fundamentals/typescript.md#ts-01)<br>[TS-02](../fundamentals/typescript.md#ts-02)<br>[TS-04](../fundamentals/typescript.md#ts-04) |
| TechSkills Frontend / A156 | Junior 1 | Поддержка клавиатуры - Навигация - Закрытие окон (Esc) - Нажатие через (Space, Enter etc) | J1-T018 | [UI-02](../frontend/html-css-ui.md#ui-02) |
| TechSkills Frontend / A163 | Junior 1 | Sentry. Логирование ошибок - Уровни логирования - Теги - Контекст - Хлебные крошки - Связывание ошибок (Error.prototype.cause) | J1-T019 | [PERF-05](../platform/performance-monitoring.md#perf-05)<br>[JS-16](../fundamentals/javascript.md#js-16) |
| TechSkills Frontend / A169 | Junior 1 | Debugging - Умение пользоваться встроенным дебаггером для отладки кода. | J1-T020 | [PERF-01](../platform/performance-monitoring.md#perf-01) |
| TechSkills Frontend / A170 | Junior 1 | Networking - Отладка запросов, Эмуляция медленного соединения | J1-T021 | [NET-01](../platform/networking.md#net-01)<br>[NET-05](../platform/networking.md#net-05) |
| TechSkills Frontend / A174 | Junior 1 | Базовые знания оптимизации: сжатие картинок, шрифты, js, css | J1-T022 | [PERF-04](../platform/performance-monitoring.md#perf-04) |
| SoftSkills / A7 | Junior 1 | Умение уточнять задачу | J1-S001 | [SOFT-007](../engineering/behavioural.md#soft-007) |
| SoftSkills / A15 | Junior 1 | Умение оповещать о проблемах (Держать команду/смежные команды в курсе, если что-то идёт не по плану) | J1-S002 | [SOFT-015](../engineering/behavioural.md#soft-015) |
| SoftSkills / A33 | Junior 1 | Умение оповещать о проблемах (Держать команду в курсе, если что-то идёт не по плану) | J1-S003 | [SOFT-033](../engineering/behavioural.md#soft-033) |
| SoftSkills / A41 | Junior 1 | Исполнительный | J1-S004 | [SOFT-041](../engineering/behavioural.md#soft-041) |
| SoftSkills / A42 | Junior 1 | Не болеет забывчивостью | J1-S005 | [SOFT-042](../engineering/behavioural.md#soft-042) |
| SoftSkills / A48 | Junior 1 | Умение распределять время | J1-S006 | [SOFT-048](../engineering/behavioural.md#soft-048) |
| SoftSkills / A78 | Junior 1 | Предоставляет конструктивную обратную связь о работе коллег | J1-S007 | [SOFT-078](../engineering/behavioural.md#soft-078) |
| SoftSkills / A85 | Junior 1 | Умение исследовать проблему | J1-S008 | [SOFT-085](../engineering/behavioural.md#soft-085) |
| SoftSkills / A86 | Junior 1 | Делать работу над ошибками | J1-S009 | [SOFT-086](../engineering/behavioural.md#soft-086) |
| TechSkills Frontend / A6 | Junior 2 | Отличие абстрактного класса от интерфейса | J2-T001 | [ARC-01](../engineering/architecture.md#arc-01)<br>[TS-02](../fundamentals/typescript.md#ts-02) |
| TechSkills Frontend / A27 | Junior 2 | Тестирование асинхронного кода. | J2-T002 | [TEST-04](../engineering/testing.md#test-04) |
| TechSkills Frontend / A28 | Junior 2 | Умение писать компонентные тесты (Юнит/Интеграционные) | J2-T003 | [TEST-05](../engineering/testing.md#test-05) |
| TechSkills Frontend / A34 | Junior 2 | Утилиты. Curl. Grep. SSH. | J2-T004 | [OPS-01](../platform/delivery-node.md#ops-01) |
| TechSkills Frontend / A53 | Junior 2 | HTTP детальная настройка запросов (Кэширование запросов, content-types, CORS) | J2-T005 | [NET-04](../platform/networking.md#net-04)<br>[NET-05](../platform/networking.md#net-05)<br>[NET-06](../platform/networking.md#net-06) |
| TechSkills Frontend / A54 | Junior 2 | TCP / UDP (Понимать принципы клиент серверной архитектуры) | J2-T006 | [NET-02](../platform/networking.md#net-02) |
| TechSkills Frontend / A97 | Junior 2 | Tuple, Record, Set, Map | J2-T007 | [ALG-02](../fundamentals/algorithms.md#alg-02) |
| TechSkills Frontend / A98 | Junior 2 | Списки. Стэк. Очередь. | J2-T008 | [ALG-03](../fundamentals/algorithms.md#alg-03) |
| TechSkills Frontend / A99 | Junior 2 | Деревья и рекурсия | J2-T009 | [ALG-04](../fundamentals/algorithms.md#alg-04) |
| TechSkills Frontend / A100 | Junior 2 | Графы. Обход и поиск кратчайшего пути | J2-T010 | [ALG-04](../fundamentals/algorithms.md#alg-04)<br>[ALG-05](../fundamentals/algorithms.md#alg-05) |
| TechSkills Frontend / A107 | Junior 2 | a11y - Базовое понимание | J2-T011 | [UI-02](../frontend/html-css-ui.md#ui-02) |
| TechSkills Frontend / A111 | Junior 2 | Понимание плюсов/минусов различных методологий (BEM, Utility first) | J2-T012 | [UI-06](../frontend/html-css-ui.md#ui-06) |
| TechSkills Frontend / A117 | Junior 2 | Концепции basic (Замыкания, Контекст вызова, Прототипы) | J2-T013 | [JS-01](../fundamentals/javascript.md#js-01)<br>[JS-02](../fundamentals/javascript.md#js-02)<br>[JS-09](../fundamentals/javascript.md#js-09) |
| TechSkills Frontend / A118 | Junior 2 | Нюансы async/await (Блокирующие и параллельные запросы, Обработка ошибок) | J2-T014 | [JS-04](../fundamentals/javascript.md#js-04)<br>[JS-05](../fundamentals/javascript.md#js-05)<br>[JS-12](../fundamentals/javascript.md#js-12) |
| TechSkills Frontend / A125 | Junior 2 | Intermediate (Slots, Async Components, Attrs inheritance, Render Function, Provide/Inject, Dynamic Components) | J2-T015 | [VUE-05](../frontend/vue.md#vue-05)<br>[VUE-06](../frontend/vue.md#vue-06)<br>[VUE-08](../frontend/vue.md#vue-08) |
| TechSkills Frontend / A131 | Junior 2 | Intermediate - Generics - Utility Types - Type Inference - Conditional Types - Recursive Types - Mapped Types | J2-T016 | [TS-03](../fundamentals/typescript.md#ts-03)<br>[TS-05](../fundamentals/typescript.md#ts-05)<br>[TS-06](../fundamentals/typescript.md#ts-06) |
| TechSkills Frontend / A136 | Junior 2 | Bundlers (Vite, Webpack, Rollup) - Умение настраивать сборку проекта | J2-T017 | [TOOL-02](../engineering/tooling-git.md#tool-02) |
| TechSkills Frontend / A137 | Junior 2 | Linter - Настройка линтера в проекте - При наличии проблем предлагать улучшения и контрибъютить | J2-T018 | [TOOL-04](../engineering/tooling-git.md#tool-04) |
| TechSkills Frontend / A138 | Junior 2 | Monorepo (lerna, turborepo) - Умение работать и понимать принципы работы с монорепо | J2-T019 | [TOOL-04](../engineering/tooling-git.md#tool-04) |
| TechSkills Frontend / A149 | Junior 2 | WebStorage - Умение работать с localStorage/sessionStorage - Понимание ограничений, в каких случаях подходит итд | J2-T020 | [WEB-03](../frontend/browser-web-api.md#web-03) |
| TechSkills Frontend / A175 | Junior 2 | Понимание оптимизации доставки контента (Алгоритмы сжатия данных) | J2-T021 | [PERF-04](../platform/performance-monitoring.md#perf-04) |
| SoftSkills / A8 | Junior 2 | Умеет ясно выражать свои мысли | J2-S001 | [SOFT-008](../engineering/behavioural.md#soft-008) |
| SoftSkills / A9 | Junior 2 | Контролирует эмоции | J2-S002 | [SOFT-009](../engineering/behavioural.md#soft-009) |
| SoftSkills / A43 | Junior 2 | Понимание методологий разработки и планирования (Agile) | J2-S003 | [SOFT-043](../engineering/behavioural.md#soft-043) |
| SoftSkills / A44 | Junior 2 | Следует правилам и процессам принятым в компании | J2-S004 | [SOFT-044](../engineering/behavioural.md#soft-044) |
| SoftSkills / A45 | Junior 2 | Стого соблюдает принципы DOR и DOD (релизить строго после тестирования на стейдже самим разработчиком и QA) | J2-S005 | [SOFT-045](../engineering/behavioural.md#soft-045) |
| SoftSkills / A49 | Junior 2 | Умение соблюдать дедлайны | J2-S006 | [SOFT-049](../engineering/behavioural.md#soft-049) |
| SoftSkills / A54 | Junior 2 | Участвует в формировании адекватных дедлайнов совместно с бизнесом | J2-S007 | [SOFT-054](../engineering/behavioural.md#soft-054) |
| SoftSkills / A87 | Junior 2 | Самостоятельно анализирует и предлагает решение проблемы | J2-S008 | [SOFT-087](../engineering/behavioural.md#soft-087) |
| TechSkills Frontend / A12 | Junior 3 | Теория - понимать отличие от виртуальных машин, чем отличается контейнер от образа. | J3-T001 | [OPS-02](../platform/delivery-node.md#ops-02) |
| TechSkills Frontend / A13 | Junior 3 | Basics. Практическое применения CLI. Docker-compose. (login, pull, up, down, kill, ps, exec) | J3-T002 | [OPS-03](../platform/delivery-node.md#ops-03) |
| TechSkills Frontend / A14 | Junior 3 | Dockerfile. Создаем простейшие образы. Модифицируем существующие | J3-T003 | [OPS-04](../platform/delivery-node.md#ops-04) |
| TechSkills Frontend / A55 | Junior 3 | Websockets | J3-T004 | [NET-02](../platform/networking.md#net-02) |
| TechSkills Frontend / A61 | Junior 3 | HTTP (HTTP сессии, Cookies) | J3-T005 | [SEC-02](../platform/security.md#sec-02)<br>[NET-06](../platform/networking.md#net-06) |
| TechSkills Frontend / A62 | Junior 3 | Модели Угроз в WEB | J3-T006 | [SEC-07](../platform/security.md#sec-07) |
| TechSkills Frontend / A63 | Junior 3 | Защита от Brute Force (captcha, отложенные запросы) | J3-T007 | [SEC-05](../platform/security.md#sec-05) |
| TechSkills Frontend / A74 | Junior 3 | Знать простые типы паттернов и уметь применять. (Factory. Builder. Singleton и др.) | J3-T008 | [ARC-03](../engineering/architecture.md#arc-03) |
| TechSkills Frontend / A84 | Junior 3 | FSD (feature sliced design) | J3-T009 | [ARC-05](../engineering/architecture.md#arc-05) |
| TechSkills Frontend / A91 | Junior 3 | Умение проводить рефакторинг кода | J3-T010 | [ARC-08](../engineering/architecture.md#arc-08) |
| TechSkills Frontend / A92 | Junior 3 | Понимание всех принципов SOLID | J3-T011 | [ARC-02](../engineering/architecture.md#arc-02) |
| TechSkills Frontend / A119 | Junior 3 | Eventloop (Макротаски и Микротаски) | J3-T012 | [JS-03](../fundamentals/javascript.md#js-03) |
| TechSkills Frontend / A120 | Junior 3 | Концепции intermediate (Proxy, Symbol, Generators) | J3-T013 | [JS-15](../fundamentals/javascript.md#js-15) |
| TechSkills Frontend / A139 | Junior 3 | Bundlers (Vite, Webpack, Rollup) - Расширять сборку проекта существующими плагинами, при необходимости уметь дописывать свои плагины - Оптимизация размера бандла | J3-T014 | [TOOL-03](../engineering/tooling-git.md#tool-03) |
| TechSkills Frontend / A143 | Junior 3 | - Умение работы с Node.js в контексте автоматизации, билдов. - Работа с файловой системой | J3-T015 | [OPS-08](../platform/delivery-node.md#ops-08) |
| TechSkills Frontend / A176 | Junior 3 | Понимание принципов загрузки ресурсов страницы современных веб браузеров | J3-T016 | [WEB-06](../frontend/browser-web-api.md#web-06)<br>[WEB-01](../frontend/browser-web-api.md#web-01) |
| TechSkills Frontend / A177 | Junior 3 | Оптимизация рендеринга (Виртуализация, Пагинация, Infinite scroll) | J3-T017 | [PERF-04](../platform/performance-monitoring.md#perf-04) |
| SoftSkills / A10 | Junior 3 | Умеет аргументировать свою точку зрения | J3-S001 | [SOFT-010](../engineering/behavioural.md#soft-010) |
| SoftSkills / A16 | Junior 3 | Умеет расположить к себе членов команды | J3-S002 | [SOFT-016](../engineering/behavioural.md#soft-016) |
| SoftSkills / A17 | Junior 3 | Помогает коллегам | J3-S003 | [SOFT-017](../engineering/behavioural.md#soft-017) |
| SoftSkills / A18 | Junior 3 | Умеет договариваться и находить компромиссы | J3-S004 | [SOFT-018](../engineering/behavioural.md#soft-018) |
| SoftSkills / A24 | Junior 3 | Несет ответственность за качество своей работы и работы всего продукта | J3-S005 | [SOFT-024](../engineering/behavioural.md#soft-024) |
| SoftSkills / A25 | Junior 3 | Непроходит мимо замеченной странности, уточняет что это: баг, фича или мелкая неточность | J3-S006 | [SOFT-025](../engineering/behavioural.md#soft-025) |
| SoftSkills / A34 | Junior 3 | Понимает для чего разрабатывается та или иная задача | J3-S007 | [SOFT-034](../engineering/behavioural.md#soft-034) |
| SoftSkills / A35 | Junior 3 | Умеет правильно расставлять приоритеты с учетом интересов бизнеса | J3-S008 | [SOFT-035](../engineering/behavioural.md#soft-035) |
| SoftSkills / A62 | Junior 3 | Непрерывно учиться | J3-S009 | [SOFT-062](../engineering/behavioural.md#soft-062) |
| SoftSkills / A63 | Junior 3 | Быстро адаптируется | J3-S010 | [SOFT-063](../engineering/behavioural.md#soft-063) |
| TechSkills Frontend / A7 | Middle 1 | Способы организации взаимодействия между классами. Наследование, композиция и агрегация | M1-T001 | [ARC-01](../engineering/architecture.md#arc-01) |
| TechSkills Frontend / A8 | Middle 1 | Знать парадигмы программирования (Императивная, функциональная, декларативная) | M1-T002 | [ARC-10](../engineering/architecture.md#arc-10)<br>[JS-11](../fundamentals/javascript.md#js-11) |
| TechSkills Frontend / A15 | Middle 1 | Volumes. Хранение данных. | M1-T003 | [OPS-03](../platform/delivery-node.md#ops-03) |
| TechSkills Frontend / A16 | Middle 1 | Registry. Хранение образов. | M1-T004 | [OPS-03](../platform/delivery-node.md#ops-03) |
| TechSkills Frontend / A17 | Middle 1 | Advanced. Взаимодействие между несколькими контейнерами (networks) | M1-T005 | [OPS-03](../platform/delivery-node.md#ops-03) |
| TechSkills Frontend / A39 | Middle 1 | Git Advanced (rebase, cherry pick) | M1-T006 | [TOOL-06](../engineering/tooling-git.md#tool-06) |
| TechSkills Frontend / A44 | Middle 1 | Repository Management | M1-T007 | [TOOL-10](../engineering/tooling-git.md#tool-10) |
| TechSkills Frontend / A45 | Middle 1 | CI/CD (Настройка Pipeline, деплой в разные окружения) | M1-T008 | [OPS-05](../platform/delivery-node.md#ops-05) |
| TechSkills Frontend / A64 | Middle 1 | Authentication JWT/SSO/OAuth | M1-T009 | [SEC-03](../platform/security.md#sec-03) |
| TechSkills Frontend / A75 | Middle 1 | Знать более сложные паттерны RefactoringGuru (Decorator, Composite, Facade, Observer, Strategy и др.) | M1-T010 | [ARC-03](../engineering/architecture.md#arc-03) |
| TechSkills Frontend / A76 | Middle 1 | Понимать какие паттерны помогают соблюдать SOLID | M1-T011 | [ARC-02](../engineering/architecture.md#arc-02)<br>[ARC-03](../engineering/architecture.md#arc-03) |
| TechSkills Frontend / A93 | Middle 1 | Умение применять все принципы SOLID | M1-T012 | [ARC-02](../engineering/architecture.md#arc-02) |
| TechSkills Frontend / A101 | Middle 1 | WeakSet, WeakMap | M1-T013 | [ALG-02](../fundamentals/algorithms.md#alg-02)<br>[JS-06](../fundamentals/javascript.md#js-06) |
| TechSkills Frontend / A102 | Middle 1 | Алгоритмы сортировки | M1-T014 | [ALG-01](../fundamentals/algorithms.md#alg-01)<br>[ALG-06](../fundamentals/algorithms.md#alg-06) |
| TechSkills Frontend / A121 | Middle 1 | Концепции advanced (Базовое понимание работы JS движков, JIT, Garbage Collector) | M1-T015 | [JS-17](../fundamentals/javascript.md#js-17)<br>[JS-06](../fundamentals/javascript.md#js-06) |
| TechSkills Frontend / A126 | Middle 1 | Реактивность (Getters & Setters, Proxy) | M1-T016 | [VUE-01](../frontend/vue.md#vue-01) |
| TechSkills Frontend / A127 | Middle 1 | Композиция компонентов с использованием слотов | M1-T017 | [VUE-05](../frontend/vue.md#vue-05) |
| TechSkills Frontend / A140 | Middle 1 | Monorepo (lerna, turborepo) - Плюсы/минусы (для чего подходит) - Настройка сборок итд в контексте монорепо с несколькими проектами. | M1-T018 | [TOOL-04](../engineering/tooling-git.md#tool-04) |
| TechSkills Frontend / A144 | Middle 1 | (Необходимо в контексте команд с SSR/BFF бэкендом) - Создание/Поддержка бэкендов - Кэширование - Сбор логов - Сбор метрик | M1-T019 | [OPS-09](../platform/delivery-node.md#ops-09)<br>[ARC-07](../engineering/architecture.md#arc-07) |
| TechSkills Frontend / A145 | Middle 1 | (Необходимо в контексте команд с SSR/BFF бэкендом) - Профилирование - Мониторинг использования памяти | M1-T020 | [OPS-09](../platform/delivery-node.md#ops-09)<br>[PERF-07](../platform/performance-monitoring.md#perf-07) |
| TechSkills Frontend / A150 | Middle 1 | WebWorker - Принцип работы и ограничения - Вынос тяжелых вычислений в другой поток | M1-T021 | [WEB-04](../frontend/browser-web-api.md#web-04) |
| TechSkills Frontend / A151 | Middle 1 | WebStorage - IndexDB - Понимание ограничений, в каких случаях подходит итд | M1-T022 | [WEB-03](../frontend/browser-web-api.md#web-03) |
| TechSkills Frontend / A159 | Middle 1 | NGINX - Базовое умение настраивать прокси сервер. | M1-T023 | [OPS-06](../platform/delivery-node.md#ops-06) |
| TechSkills Frontend / A178 | Middle 1 | Lazy Loading статики | M1-T024 | [WEB-06](../frontend/browser-web-api.md#web-06)<br>[PERF-04](../platform/performance-monitoring.md#perf-04) |
| SoftSkills / A19 | Middle 1 | Эффективно взаимодействует со всеми участниками своей и смежных команд | M1-S001 | [SOFT-019](../engineering/behavioural.md#soft-019) |
| SoftSkills / A20 | Middle 1 | Распространяет образ мышления - "максимальная взаимопомощь среди сотрудников" | M1-S002 | [SOFT-020](../engineering/behavioural.md#soft-020) |
| SoftSkills / A21 | Middle 1 | Влияет на решения принимаемые в команде, касательно вопросов постановки, прогресса, разработки | M1-S003 | [SOFT-021](../engineering/behavioural.md#soft-021) |
| SoftSkills / A26 | Middle 1 | Несет ответственность за соблюдение сроков и показатель Time To Market | M1-S004 | [SOFT-026](../engineering/behavioural.md#soft-026) |
| SoftSkills / A27 | Middle 1 | Задачи сопровождаются продуманной документацией | M1-S005 | [SOFT-027](../engineering/behavioural.md#soft-027) |
| SoftSkills / A36 | Middle 1 | Оперативно информирует в случаях срыва срока или возникновения форс мажора тим лида/руководителя/менеджера для своевременного решения ситуации. | M1-S006 | [SOFT-036](../engineering/behavioural.md#soft-036) |
| SoftSkills / A50 | Middle 1 | Все артефакты создает своевременно (тесты, документация, мониторинги) | M1-S007 | [SOFT-050](../engineering/behavioural.md#soft-050) |
| SoftSkills / A51 | Middle 1 | Все обращения от support обрабатывает оперативно и что немаловажно качественно | M1-S008 | [SOFT-051](../engineering/behavioural.md#soft-051) |
| SoftSkills / A58 | Middle 1 | Самостоятельно решает любые вопросы, задачи, проблемы (не нуждается в помощи и контроле из вне) | M1-S009 | [SOFT-058](../engineering/behavioural.md#soft-058) |
| SoftSkills / A67 | Middle 1 | Проявляет инициативу в любом вопросе (всегда сделает что-то чтобы исправить существующие недочеты; берет и разбирается сам, не ждет пока кто-то придет и сделает или назначат ответственного и т.п.) | M1-S010 | [SOFT-067](../engineering/behavioural.md#soft-067) |
| SoftSkills / A68 | Middle 1 | Предлагает и реализует изменения по улучшению (по обеспечению качества продуктов, по оптимизации рабочих процессов, продукту, по использованию фреймворков, инструметов, новых методик, подходов, паттернов, технологий и приемов для оптимизации тестирования и т.д.) | M1-S011 | [SOFT-068](../engineering/behavioural.md#soft-068) |
| SoftSkills / A69 | Middle 1 | Участие на собеседованиях в роли интервьюера | M1-S012 | [SOFT-069](../engineering/behavioural.md#soft-069) |
| SoftSkills / A72 | Middle 1 | Мониторит и анализирует ошибки в sentry, мониторинги сервисов команды в grafana, алерты в телеграмме | M1-S013 | [SOFT-072](../engineering/behavioural.md#soft-072) |
| SoftSkills / A77 | Middle 1 | Обучает и сопровождает новых сотрудников в соответствии с планом онбординга/развития | M1-S014 | [SOFT-077](../engineering/behavioural.md#soft-077) |
| SoftSkills / A79 | Middle 1 | Активно развивает базу знаний | M1-S015 | [SOFT-079](../engineering/behavioural.md#soft-079) |
| SoftSkills / A80 | Middle 1 | Выступление на внутренних конференциях с докладами | M1-S016 | [SOFT-080](../engineering/behavioural.md#soft-080) |
| SoftSkills / A88 | Middle 1 | Предлагает обдуманные варианты решений проблем, задач, изменений и понимает последствия | M1-S017 | [SOFT-088](../engineering/behavioural.md#soft-088) |
| SoftSkills / A97 | Middle 1 | Ведет статистику и анализ ошибок, багов продукта | M1-S018 | [SOFT-097](../engineering/behavioural.md#soft-097) |
| SoftSkills / A98 | Middle 1 | При делегировании задач на сотрудника, предоставляет требуемую для качественного выполнения задачи информацию, доходчиво объяснет суть задачи и контроллирует выполнение задачи. | M1-S019 | [SOFT-098](../engineering/behavioural.md#soft-098) |
| TechSkills Frontend / A18 | Middle 2 | Dockerfile. Multistage. | M2-T001 | [OPS-04](../platform/delivery-node.md#ops-04) |
| TechSkills Frontend / A19 | Middle 2 | Dockerfile. Для разных окружений Production & Staging. | M2-T002 | [OPS-05](../platform/delivery-node.md#ops-05) |
| TechSkills Frontend / A40 | Middle 2 | Понимать различия подходов GitFlow/Trunk Based | M2-T003 | [TOOL-07](../engineering/tooling-git.md#tool-07) |
| TechSkills Frontend / A46 | Middle 2 | Integrations(Webhooks, Integration with 3d party applications (jira, yandex tracker) | M2-T004 | [TOOL-09](../engineering/tooling-git.md#tool-09) |
| TechSkills Frontend / A47 | Middle 2 | Security | M2-T005 | [TOOL-10](../engineering/tooling-git.md#tool-10) |
| TechSkills Frontend / A56 | Middle 2 | CDN подходы к доставке содержимого | M2-T006 | [NET-04](../platform/networking.md#net-04) |
| TechSkills Frontend / A65 | Middle 2 | Content Security Policy | M2-T007 | [SEC-04](../platform/security.md#sec-04) |
| TechSkills Frontend / A66 | Middle 2 | Security Headers (X-Frame-Options, Referer-Policy, Strict-Transport-Security, X-Content-Type-Options, X-Xss-Protection, CORS) | M2-T008 | [SEC-04](../platform/security.md#sec-04)<br>[NET-05](../platform/networking.md#net-05) |
| TechSkills Frontend / A77 | Middle 2 | Знать основные антипаттерны разработки SourceMaking (применять при ревью) | M2-T009 | [ARC-04](../engineering/architecture.md#arc-04) |
| TechSkills Frontend / A85 | Middle 2 | Понимание видов рендеринга. В каких случаях подходят. Плюсы/Минусы каждого подхода Уметь настраивать/интегрировать тот или иной подход - SSR (Server Side Rendering) - CSR (Client Side Rendering) - SSG (Static Site Generation) | M2-T010 | [ARC-06](../engineering/architecture.md#arc-06) |
| TechSkills Frontend / A86 | Middle 2 | SPA (Single Page Application) vs MPA (Multie Page Application) В каких случаях подходят. Плюсы/Минусы каждого подхода Уметь настраивать/интегрировать тот или иной подход | M2-T011 | [ARC-06](../engineering/architecture.md#arc-06) |
| TechSkills Frontend / A87 | Middle 2 | Cloud, CDN и S3. Понимать принципы работы и уметь применять | M2-T012 | [ARC-07](../engineering/architecture.md#arc-07)<br>[NET-04](../platform/networking.md#net-04) |
| TechSkills Frontend / A152 | Middle 2 | ServiceWorker - Кэширование - Проксирование | M2-T013 | [WEB-05](../frontend/browser-web-api.md#web-05) |
| TechSkills Frontend / A164 | Middle 2 | ELK queries (Запросы, Access Logs, работа с интерфесом Kibana) | M2-T014 | [PERF-05](../platform/performance-monitoring.md#perf-05) |
| TechSkills Frontend / A171 | Middle 2 | Profiling - Умение профилировать код и выявлять медленные участки кода | M2-T015 | [PERF-01](../platform/performance-monitoring.md#perf-01) |
| TechSkills Frontend / A179 | Middle 2 | Настройка оптимизация доставки контента (пример: настройка gzip + nginx) | M2-T016 | [OPS-06](../platform/delivery-node.md#ops-06)<br>[PERF-04](../platform/performance-monitoring.md#perf-04) |
| TechSkills Frontend / A180 | Middle 2 | Оптимизация Web Vitals (LCP, FID, CLS) | M2-T017 | [PERF-02](../platform/performance-monitoring.md#perf-02) |
| SoftSkills / A28 | Middle 2 | Отвечает за правильность и целесобразность подходов и действий, а также применяемых технологий | M2-S001 | [SOFT-028](../engineering/behavioural.md#soft-028) |
| SoftSkills / A29 | Middle 2 | Берет на себя дополнительную ответственность, не избегает ее, даже если задачи/вопросы напрямую не касаются его области ответственности | M2-S002 | [SOFT-029](../engineering/behavioural.md#soft-029) |
| SoftSkills / A30 | Middle 2 | Все результаты его деятельности понятны и прозрачны (есть отчеты о результатах, чек-листы, планы, выводы) | M2-S003 | [SOFT-030](../engineering/behavioural.md#soft-030) |
| SoftSkills / A37 | Middle 2 | Всегда учитывает интересы бизнеса при решении задач, проверяет на соответствие ОКР | M2-S004 | [SOFT-037](../engineering/behavioural.md#soft-037) |
| SoftSkills / A55 | Middle 2 | Умеет хорошо планировать объем работ и предоставлять точную оценку сроков, с учетом рисков | M2-S005 | [SOFT-055](../engineering/behavioural.md#soft-055) |
| SoftSkills / A70 | Middle 2 | Участвует во всех активностях по оптимизации, ускорению и улучшению процессов команды/компании | M2-S006 | [SOFT-070](../engineering/behavioural.md#soft-070) |
| SoftSkills / A71 | Middle 2 | Помогает менеджерам/разработчикам в составлении задач | M2-S007 | [SOFT-071](../engineering/behavioural.md#soft-071) |
| SoftSkills / A89 | Middle 2 | Умеет работать в стрессовых ситуациях (жесткий дедлайн, большое количество разных задач, экстренные ситации или форс-мажоры) | M2-S008 | [SOFT-089](../engineering/behavioural.md#soft-089) |
| TechSkills Frontend / A20 | Middle 3 | Advanced. Минимизация объема и времени сборки образа. | M3-T001 | [OPS-04](../platform/delivery-node.md#ops-04) |
| TechSkills Frontend / A29 | Middle 3 | Умение проводить нагрузочное тестирование, сбор статистики и поиск узких мест | M3-T002 | [TEST-06](../engineering/testing.md#test-06) |
| TechSkills Frontend / A57 | Middle 3 | Понимать что такое DNS и его принцип работы | M3-T003 | [NET-07](../platform/networking.md#net-07) |
| TechSkills Frontend / A67 | Middle 3 | OWASP TOP 10 | M3-T004 | [SEC-06](../platform/security.md#sec-06) |
| TechSkills Frontend / A78 | Middle 3 | Знать паттерны за пределами RefactoringGuru | M3-T005 | [ARC-04](../engineering/architecture.md#arc-04) |
| TechSkills Frontend / A79 | Middle 3 | Знать анти-паттерны за пределами SourceMaking | M3-T006 | [ARC-04](../engineering/architecture.md#arc-04) |
| TechSkills Frontend / A160 | Middle 3 | Kubernetes - Основные знания, понимание как работает деплоймент приложений с нашими общими конфигами | M3-T007 | [OPS-07](../platform/delivery-node.md#ops-07) |
| TechSkills Frontend / A165 | Middle 3 | Graphite. Сбор метрик (При наличии бэкенда на ноде) | M3-T008 | [PERF-07](../platform/performance-monitoring.md#perf-07) |
| TechSkills Frontend / A166 | Middle 3 | Grafana. Уметь настраивать дэшборды и графики. Настройка алертов на разные источники. | M3-T009 | [PERF-06](../platform/performance-monitoring.md#perf-06) |
| SoftSkills / A73 | Middle 3 | Мониторит и анализирует эфективность разработки в команде | M3-S001 | [SOFT-073](../engineering/behavioural.md#soft-073) |
| SoftSkills / A93 | Middle 3 | Создает и стандартизирует документы, процессы, процедуры, схемы коммуникации отдела c остальными членами продуктовой команды и т.п. | M3-S002 | [SOFT-093](../engineering/behavioural.md#soft-093) |
| SoftSkills / A94 | Middle 3 | Составляет план работ для всей команды (для лучшей координации коллег, для оптимизированной и слаженной работы) | M3-S003 | [SOFT-094](../engineering/behavioural.md#soft-094) |
| SoftSkills / A95 | Middle 3 | Координирует работу отдельного направления | M3-S004 | [SOFT-095](../engineering/behavioural.md#soft-095) |
| SoftSkills / A96 | Middle 3 | Предпринимает меры по урегулированию/недопущению/сокращению стрессовых и сложных ситуаций | M3-S005 | [SOFT-096](../engineering/behavioural.md#soft-096) |
| SoftSkills / A99 | Middle 3 | Лидерство в команде/ в отделе/ в направлении, при необходимости может заменить лида | M3-S006 | [SOFT-099](../engineering/behavioural.md#soft-099) |
| TechSkills Frontend / A9 | Senior (top) | Понимание и умение применять GRASP паттерны | SR-T001 | [ARC-09](../engineering/architecture.md#arc-09) |
| TechSkills Frontend / A68 | Senior (top) | Анализ приложения на угрозы. Уметь их предупреждать и устранять | SR-T002 | [SEC-07](../platform/security.md#sec-07) |
| TechSkills Frontend / A69 | Senior (top) | Legal (GDPR, Закон о персональных данных и их защите РК) | SR-T003 | [SEC-08](../platform/security.md#sec-08) |
| TechSkills Frontend / A70 | Senior (top) | Принципы работы с секретами. Хранение. Шифрование | SR-T004 | [SEC-05](../platform/security.md#sec-05)<br>[TOOL-10](../engineering/tooling-git.md#tool-10) |
| TechSkills Frontend / A71 | Senior (top) | Pentest, понимать подходы и принципы | SR-T005 | [SEC-09](../platform/security.md#sec-09) |
| TechSkills Frontend / A80 | Senior (top) | Знать основные архитектурные антипаттерны (применять при ревью и проектировании архитектуры) | SR-T006 | [ARC-04](../engineering/architecture.md#arc-04)<br>[ARC-08](../engineering/architecture.md#arc-08) |
| TechSkills Frontend / A181 | Senior (top) | Оптимизация метрик - Time to First Byte (TTFB) - First Contentful Paint (FCP) - Time to Interactive (TTI) - Total Blocking Time (TBT) - Interaction to Next Paint (INP) | SR-T007 | [PERF-03](../platform/performance-monitoring.md#perf-03)<br>[PERF-01](../platform/performance-monitoring.md#perf-01) |
| TechSkills Frontend / A182 | Senior (top) | Отслеживание метрик (Lab metrics, Field metrics) | SR-T008 | [PERF-03](../platform/performance-monitoring.md#perf-03) |
| SoftSkills / A74 | Senior (top) | Мониторит и анализирует эфективность коммуникаций и взаимодействия с другими командами | SR-S001 | [SOFT-074](../engineering/behavioural.md#soft-074) |
| SoftSkills / A81 | Senior (top) | Выступление на внешних площадках (статьи, выступления на митапах и конференциях, проведение докладов/лекций/обучения/мастер классов) | SR-S002 | [SOFT-081](../engineering/behavioural.md#soft-081) |
| SoftSkills / A82 | Senior (top) | Внедряет успешные практики в компании (процессы, технологии) | SR-S003 | [SOFT-082](../engineering/behavioural.md#soft-082) |
| SoftSkills / A90 | Senior (top) | Может работать с параллельными проектами / деятельностями не связанными с проектами, такими, как презентации, исследования, обучения и т.д | SR-S004 | [SOFT-090](../engineering/behavioural.md#soft-090) |
| SoftSkills / A100 | Senior (top) | Лидерство в в компании (сфера влияния вся компания) | SR-S005 | [SOFT-100](../engineering/behavioural.md#soft-100) |
