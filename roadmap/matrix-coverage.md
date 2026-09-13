# Соответствие исходной матрице

Источник: «Технические потребности для разработчиков (back&front&mobile).xlsx», лист `TechSkills Frontend`, столбец H (Mid3). Исходник не изменён.

Каждая строка ниже имеет `+` у Mid3. Ссылка означает наличие учебного разбора, а не подтверждённое владение темой. Крупные исходные пункты распределены между вопросами блока. Номера относятся к Excel, формулировки сохранены с нормализацией пробелов.

Условные пункты: A144, A145 — SSR/BFF; A165 — Node.js backend. Полный объём глубины определяем по стеку команды. Дополнения вроде подробных lab/field-метрик отмечены в учебных файлах.

| Строка | Требование | Материал |
|---|---|---|
| A3 / H3 | Знание базовых принципов(Инкапсуляция, Полиморфизм, Наследование) | [ARC-01–02](../engineering/architecture.md) |
| A4 / H4 | Уметь применять базовые принципы | [ARC-01–02](../engineering/architecture.md) |
| A5 / H5 | Статистические и классовые методы. Области видимости | [ARC-01–02](../engineering/architecture.md) |
| A6 / H6 | Отличие абстрактного класса от интерфейса | [ARC-01–02](../engineering/architecture.md) |
| A7 / H7 | Способы организации взаимодействия между классами. Наследование, композиция и агрегация | [ARC-01–02](../engineering/architecture.md) |
| A8 / H8 | Знать парадигмы программирования (Императивная, функциональная, декларативная) | [ARC-01–02](../engineering/architecture.md) |
| A12 / H12 | Теория - понимать отличие от виртуальных машин, чем отличается контейнер от образа. | [OPS-02–04](../platform/delivery-node.md) |
| A13 / H13 | Basics. Практическое применения CLI. Docker-compose. (login, pull, up, down, kill, ps, exec) | [OPS-02–04](../platform/delivery-node.md) |
| A14 / H14 | Dockerfile. Создаем простейшие образы. Модифицируем существующие | [OPS-02–04](../platform/delivery-node.md) |
| A15 / H15 | Volumes. Хранение данных. | [OPS-02–04](../platform/delivery-node.md) |
| A16 / H16 | Registry. Хранение образов. | [OPS-02–04](../platform/delivery-node.md) |
| A17 / H17 | Advanced. Взаимодействие между несколькими контейнерами (networks) | [OPS-02–04](../platform/delivery-node.md) |
| A18 / H18 | Dockerfile. Multistage. | [OPS-02–04](../platform/delivery-node.md) |
| A19 / H19 | Dockerfile. Для разных окружений Production & Staging. | [OPS-02–04](../platform/delivery-node.md) |
| A20 / H20 | Advanced. Минимизация объема и времени сборки образа. | [OPS-02–04](../platform/delivery-node.md) |
| A23 / H23 | Теория. Принципы и Виды тестирования. Умение писать юнит тесты. | [TEST-01–06](../engineering/testing.md) |
| A24 / H24 | Функции тестирования. Mocking and Fixtures. | [TEST-01–06](../engineering/testing.md) |
| A25 / H25 | Coverage | [TEST-01–06](../engineering/testing.md) |
| A26 / H26 | Параметризированные тесты. | [TEST-01–06](../engineering/testing.md) |
| A27 / H27 | Тестирование асинхронного кода. | [TEST-01–06](../engineering/testing.md) |
| A28 / H28 | Умение писать компонентные тесты (Юнит/Интеграционные) | [TEST-01–06](../engineering/testing.md) |
| A29 / H29 | Умение проводить нагрузочное тестирование, сбор статистики и поиск узких мест | [TEST-01–06](../engineering/testing.md) |
| A32 / H32 | Работа с терминалом. Установка пакетов. | [OPS-01](../platform/delivery-node.md) |
| A33 / H33 | Редактирование файлов. Права на файлы. | [OPS-01](../platform/delivery-node.md) |
| A34 / H34 | Утилиты. Curl. Grep. SSH. | [OPS-01](../platform/delivery-node.md) |
| A37 / H37 | Git Basic (clone, add, commit, pull, push, checkout, reset, ssh) | [TOOL-05–07](../engineering/tooling-git.md) |
| A38 / H38 | Git Middle (resolve conflicts, remotes, revert, history, compare revisions and branches) | [TOOL-05–07](../engineering/tooling-git.md) |
| A39 / H39 | Git Advanced (rebase, cherry pick) | [TOOL-05–07](../engineering/tooling-git.md) |
| A40 / H40 | Понимать различия подходов GitFlow/Trunk Based | [TOOL-05–07](../engineering/tooling-git.md) |
| A43 / H43 | Merge Requests | [TOOL-07; CI/CD также OPS-05](../engineering/tooling-git.md) |
| A44 / H44 | Repository Management | [TOOL-07; CI/CD также OPS-05](../engineering/tooling-git.md) |
| A45 / H45 | CI/CD (Настройка Pipeline, деплой в разные окружения) | [TOOL-07; CI/CD также OPS-05](../engineering/tooling-git.md) |
| A46 / H46 | Integrations(Webhooks, Integration with 3d party applications (jira, yandex tracker) | [TOOL-07; CI/CD также OPS-05](../engineering/tooling-git.md) |
| A47 / H47 | Security | [TOOL-07; CI/CD также OPS-05](../engineering/tooling-git.md) |
| A50 / H50 | Базовое знание модели OSI | [NET-01–06](../platform/networking.md) |
| A51 / H51 | HTTP (Структура запросов/ответов, Cookies, Коды ответов, Multipart, Методы, HTTPS, Авторизация) | [NET-01–06](../platform/networking.md) |
| A52 / H52 | Умение отправлять запросы. Знать протоколы передачи данных. | [NET-01–06](../platform/networking.md) |
| A53 / H53 | HTTP детальная настройка запросов (Кэширование запросов, content-types, CORS) | [NET-01–06](../platform/networking.md) |
| A54 / H54 | TCP / UDP (Понимать принципы клиент серверной архитектуры) | [NET-01–06](../platform/networking.md) |
| A55 / H55 | Websockets | [NET-01–06](../platform/networking.md) |
| A56 / H56 | CDN подходы к доставке содержимого | [NET-01–06](../platform/networking.md) |
| A57 / H57 | Понимать что такое DNS и его принцип работы | [NET-01–06](../platform/networking.md) |
| A60 / H60 | XSS (Cross Site Scripting) | [SEC-01–06](../platform/security.md) |
| A61 / H61 | HTTP (HTTP сессии, Cookies) | [SEC-01–06](../platform/security.md) |
| A62 / H62 | Модели Угроз в WEB | [SEC-01–06](../platform/security.md) |
| A63 / H63 | Защита от Brute Force (captcha, отложенные запросы) | [SEC-01–06](../platform/security.md) |
| A64 / H64 | Authentication JWT/SSO/OAuth | [SEC-01–06](../platform/security.md) |
| A65 / H65 | Content Security Policy | [SEC-01–06](../platform/security.md) |
| A66 / H66 | Security Headers (X-Frame-Options, Referer-Policy, Strict-Transport-Security, X-Content-Type-Options, X-Xss-Protection, CORS) | [SEC-01–06](../platform/security.md) |
| A67 / H67 | OWASP TOP 10 | [SEC-01–06](../platform/security.md) |
| A74 / H74 | Знать простые типы паттернов и уметь применять. (Factory. Builder. Singleton и др.) | [ARC-02–04](../engineering/architecture.md) |
| A75 / H75 | Знать более сложные паттерны RefactoringGuru (Decorator, Composite, Facade, Observer, Strategy и др.) | [ARC-02–04](../engineering/architecture.md) |
| A76 / H76 | Понимать какие паттерны помогают соблюдать SOLID | [ARC-02–04](../engineering/architecture.md) |
| A77 / H77 | Знать основные антипаттерны разработки SourceMaking (применять при ревью) | [ARC-02–04](../engineering/architecture.md) |
| A78 / H78 | Знать паттерны за пределами RefactoringGuru | [ARC-02–04](../engineering/architecture.md) |
| A79 / H79 | Знать анти-паттерны за пределами SourceMaking | [ARC-02–04](../engineering/architecture.md) |
| A83 / H83 | Клиент-серверная архитектура | [ARC-05–07](../engineering/architecture.md) |
| A84 / H84 | FSD (feature sliced design) | [ARC-05–07](../engineering/architecture.md) |
| A85 / H85 | Понимание видов рендеринга. В каких случаях подходят. Плюсы/Минусы каждого подхода Уметь настраивать/интегрировать тот или иной подход - SSR (Server Side Rendering) - CSR (Client Side Rendering) - SSG (Static Site Generation) | [ARC-05–07](../engineering/architecture.md) |
| A86 / H86 | SPA (Single Page Application) vs MPA (Multie Page Application) В каких случаях подходят. Плюсы/Минусы каждого подхода Уметь настраивать/интегрировать тот или иной подход | [ARC-05–07](../engineering/architecture.md) |
| A87 / H87 | Cloud, CDN и S3. Понимать принципы работы и уметь применять | [ARC-05–07](../engineering/architecture.md) |
| A90 / H90 | Базовые принципы программирования: DRY, KISS, YAGNI | [ARC-02, ARC-08](../engineering/architecture.md) |
| A91 / H91 | Умение проводить рефакторинг кода | [ARC-02, ARC-08](../engineering/architecture.md) |
| A92 / H92 | Понимание всех принципов SOLID | [ARC-02, ARC-08](../engineering/architecture.md) |
| A93 / H93 | Умение применять все принципы SOLID | [ARC-02, ARC-08](../engineering/architecture.md) |
| A96 / H96 | Массивы, JSON Объекты | [ALG-01–06](../fundamentals/algorithms.md) |
| A97 / H97 | Tuple, Record, Set, Map | [ALG-01–06](../fundamentals/algorithms.md) |
| A98 / H98 | Списки. Стэк. Очередь. | [ALG-01–06](../fundamentals/algorithms.md) |
| A99 / H99 | Деревья и рекурсия | [ALG-01–06](../fundamentals/algorithms.md) |
| A100 / H100 | Графы. Обход и поиск кратчайшего пути | [ALG-01–06](../fundamentals/algorithms.md) |
| A101 / H101 | WeakSet, WeakMap | [ALG-01–06](../fundamentals/algorithms.md) |
| A102 / H102 | Алгоритмы сортировки | [ALG-01–06](../fundamentals/algorithms.md) |
| A105 / H105 | Базовые HTML теги и аттрибуты | [UI-01–02](../frontend/html-css-ui.md) |
| A106 / H106 | Семантическая верстка - Понимание влияния на SEO и использование семантически верных элементов с дефолтным поведением. | [UI-01–02](../frontend/html-css-ui.md) |
| A107 / H107 | a11y - Базовое понимание | [UI-01–02](../frontend/html-css-ui.md) |
| A110 / H110 | Знание специфичности, изоляция стилей, каскадность, media queries | [UI-03–06](../frontend/html-css-ui.md) |
| A111 / H111 | Понимание плюсов/минусов различных методологий (BEM, Utility first) | [UI-03–06](../frontend/html-css-ui.md) |
| A114 / H114 | Знать синтаксис (Переменные, Типы данных, Функции, Классы, Модули, Обработка ошибок) | [JS-01–17](../fundamentals/javascript.md) |
| A115 / H115 | Асинхронность (Callback, Promise, Async/Await, Таймауты и Интервалы) | [JS-01–17](../fundamentals/javascript.md) |
| A116 / H116 | FP (Чистые функции, Иммутабельность) Иммутабельность - Умение писать иммутабельный код. Понимать где мутация создают проблемы, где мутации это нормально Чистые функции - Ограниченное наличие сайд эффектов в функциях. Стремится преимущественно писать чистые функции | [JS-01–17](../fundamentals/javascript.md) |
| A117 / H117 | Концепции basic (Замыкания, Контекст вызова, Прототипы) | [JS-01–17](../fundamentals/javascript.md) |
| A118 / H118 | Нюансы async/await (Блокирующие и параллельные запросы, Обработка ошибок) | [JS-01–17](../fundamentals/javascript.md) |
| A119 / H119 | Eventloop (Макротаски и Микротаски) | [JS-01–17](../fundamentals/javascript.md) |
| A120 / H120 | Концепции intermediate (Proxy, Symbol, Generators) | [JS-01–17](../fundamentals/javascript.md) |
| A121 / H121 | Концепции advanced (Базовое понимание работы JS движков, JIT, Garbage Collector) | [JS-01–17](../fundamentals/javascript.md) |
| A124 / H124 | Basic (Components, Props, Events, Directives, Computed, Watch, Life Cycle Hooks, Templates, CompositionAPI) | [VUE-01–07](../frontend/vue.md) |
| A125 / H125 | Intermediate (Slots, Async Components, Attrs inheritance, Render Function, Provide/Inject, Dynamic Components) | [VUE-01–07](../frontend/vue.md) |
| A126 / H126 | Реактивность (Getters & Setters, Proxy) | [VUE-01–07](../frontend/vue.md) |
| A127 / H127 | Композиция компонентов с использованием слотов | [VUE-01–07](../frontend/vue.md) |
| A130 / H130 | Basic - Type annotations - Type/Interface - Type Guards - Union - Intersection - Operators (keyof, typef, const) | [TS-01–06](../fundamentals/typescript.md) |
| A131 / H131 | Intermediate - Generics - Utility Types - Type Inference - Conditional Types - Recursive Types - Mapped Types | [TS-01–06](../fundamentals/typescript.md) |
| A134 / H134 | Package Manager (npm, yarn) - Умение работать с пакетными менеджерами | [TOOL-01–04](../engineering/tooling-git.md) |
| A135 / H135 | Linter - Придерживаться общепринятых правил для линтеров. | [TOOL-01–04](../engineering/tooling-git.md) |
| A136 / H136 | Bundlers (Vite, Webpack, Rollup) - Умение настраивать сборку проекта | [TOOL-01–04](../engineering/tooling-git.md) |
| A137 / H137 | Linter - Настройка линтера в проекте - При наличии проблем предлагать улучшения и контрибъютить | [TOOL-01–04](../engineering/tooling-git.md) |
| A138 / H138 | Monorepo (lerna, turborepo) - Умение работать и понимать принципы работы с монорепо | [TOOL-01–04](../engineering/tooling-git.md) |
| A139 / H139 | Bundlers (Vite, Webpack, Rollup) - Расширять сборку проекта существующими плагинами, при необходимости уметь дописывать свои плагины - Оптимизация размера бандла | [TOOL-01–04](../engineering/tooling-git.md) |
| A140 / H140 | Monorepo (lerna, turborepo) - Плюсы/минусы (для чего подходит) - Настройка сборок итд в контексте монорепо с несколькими проектами. | [TOOL-01–04](../engineering/tooling-git.md) |
| A143 / H143 | - Умение работы с Node.js в контексте автоматизации, билдов. - Работа с файловой системой | [OPS-08–09](../platform/delivery-node.md) |
| A144 / H144 | (Необходимо в контексте команд с SSR/BFF бэкендом) - Создание/Поддержка бэкендов - Кэширование - Сбор логов - Сбор метрик | [OPS-08–09](../platform/delivery-node.md) |
| A145 / H145 | (Необходимо в контексте команд с SSR/BFF бэкендом) - Профилирование - Мониторинг использования памяти | [OPS-08–09](../platform/delivery-node.md) |
| A148 / H148 | Работа с DOM древом. | [WEB-02–05](../frontend/browser-web-api.md) |
| A149 / H149 | WebStorage - Умение работать с localStorage/sessionStorage - Понимание ограничений, в каких случаях подходит итд | [WEB-02–05](../frontend/browser-web-api.md) |
| A150 / H150 | WebWorker - Принцип работы и ограничения - Вынос тяжелых вычислений в другой поток | [WEB-02–05](../frontend/browser-web-api.md) |
| A151 / H151 | WebStorage - IndexDB - Понимание ограничений, в каких случаях подходит итд | [WEB-02–05](../frontend/browser-web-api.md) |
| A152 / H152 | ServiceWorker - Кэширование - Проксирование | [WEB-02–05](../frontend/browser-web-api.md) |
| A155 / H155 | Обработка интерактивных состояний (hover/active/focus/disabled) | [UI-02, UI-06](../frontend/html-css-ui.md) |
| A156 / H156 | Поддержка клавиатуры - Навигация - Закрытие окон (Esc) - Нажатие через (Space, Enter etc) | [UI-02, UI-06](../frontend/html-css-ui.md) |
| A159 / H159 | NGINX - Базовое умение настраивать прокси сервер. | [OPS-06–07](../platform/delivery-node.md) |
| A160 / H160 | Kubernetes - Основные знания, понимание как работает деплоймент приложений с нашими общими конфигами | [OPS-06–07](../platform/delivery-node.md) |
| A163 / H163 | Sentry. Логирование ошибок - Уровни логирования - Теги - Контекст - Хлебные крошки - Связывание ошибок (Error.prototype.cause) | [PERF-05–07](../platform/performance-monitoring.md) |
| A164 / H164 | ELK queries (Запросы, Access Logs, работа с интерфесом Kibana) | [PERF-05–07](../platform/performance-monitoring.md) |
| A165 / H165 | Graphite. Сбор метрик (При наличии бэкенда на ноде) | [PERF-05–07](../platform/performance-monitoring.md) |
| A166 / H166 | Grafana. Уметь настраивать дэшборды и графики. Настройка алертов на разные источники. | [PERF-05–07](../platform/performance-monitoring.md) |
| A169 / H169 | Debugging - Умение пользоваться встроенным дебаггером для отладки кода. | [PERF-01](../platform/performance-monitoring.md) |
| A170 / H170 | Networking - Отладка запросов, Эмуляция медленного соединения | [PERF-01](../platform/performance-monitoring.md) |
| A171 / H171 | Profiling - Умение профилировать код и выявлять медленные участки кода | [PERF-01](../platform/performance-monitoring.md) |
| A174 / H174 | Базовые знания оптимизации: сжатие картинок, шрифты, js, css | [PERF-02, PERF-04; загрузка также WEB-06](../platform/performance-monitoring.md) |
| A175 / H175 | Понимание оптимизации доставки контента (Алгоритмы сжатия данных) | [PERF-02, PERF-04; загрузка также WEB-06](../platform/performance-monitoring.md) |
| A176 / H176 | Понимание принципов загрузки ресурсов страницы современных веб браузеров | [PERF-02, PERF-04; загрузка также WEB-06](../platform/performance-monitoring.md) |
| A177 / H177 | Оптимизация рендеринга (Виртуализация, Пагинация, Infinite scroll) | [PERF-02, PERF-04; загрузка также WEB-06](../platform/performance-monitoring.md) |
| A178 / H178 | Lazy Loading статики | [PERF-02, PERF-04; загрузка также WEB-06](../platform/performance-monitoring.md) |
| A179 / H179 | Настройка оптимизация доставки контента (пример: настройка gzip + nginx) | [PERF-02, PERF-04; загрузка также WEB-06](../platform/performance-monitoring.md) |
| A180 / H180 | Оптимизация Web Vitals (LCP, FID, CLS) | [PERF-02, PERF-04; загрузка также WEB-06](../platform/performance-monitoring.md) |

## Дополнительные ожидания

- `Responsibilities!B8`: аварии/профилактика — MID-01–02; контроль долга — MID-03; документация — MID-04.
- `SoftSkills!H73,H93:H96,H99`: эффективность, процессы, планирование, координация, снижение стрессовых ситуаций, лидерство — MID-01–06.
- GRASP и ряд security/architecture-пунктов имеют минус у Mid3: не считаем их обязательными по этому столбцу.
- `A199:A202`: TODO исходника, не утверждённый перечень Mid3.

[Вернуться к плану](../README.md)
