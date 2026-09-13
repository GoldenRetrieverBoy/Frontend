# Блок 02. TypeScript

[План](../README.md) · Предыдущий: [JavaScript](../fundamentals/javascript.md) · Следующий: [Vue](../frontend/vue.md)

Предполагаем strict mode. Фрагменты независимы. Цель — моделировать допустимые состояния и понимать границу между проверкой типов и выполнением JavaScript.

<a id="ts-01"></a>

## TS-01. Чем TypeScript отличается от runtime-валидации?

**Ответ.** TypeScript проверяет совместимость типов до запуска. Аннотации и большинство конструкций типов удаляются при преобразовании в JS. Запись `as User` не проверяет JSON и не преобразует его в пользователя. Внешние данные проверяем во время выполнения.

```ts
type User = { id: string };
function isUser(value: unknown): value is User {
  return typeof value === 'object' && value !== null
    && 'id' in value && typeof value.id === 'string';
}
const raw: unknown = JSON.parse('{"id":42}');
if (isUser(raw)) console.log(raw.id.toUpperCase());
```

unknown требует сужения перед использованием; any отключает значительную часть проверок и распространяет небезопасность. Самописный type predicate компилятор принимает на доверии: если проверка ошибочна, типовая гарантия ложная.

**Практика.** Расширь проверку на массив пользователей и ошибку с указанием некорректного элемента. **Ошибка:** считать ответ сервера безопасным из-за generic у HTTP-клиента.

<a id="ts-02"></a>

## TS-02. Когда type, interface, union и intersection?

**Ответ.** interface удобно описывает объектные контракты и поддерживает слияние объявлений. type может называть union, tuple и другие типовые выражения. `A | B` означает один из вариантов, `A & B` — необходимость удовлетворить обоим одновременно. Intersection не выполняет runtime-слияние объектов.

```ts
type Result<T> =
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };
function label(result: Result<string>) {
  if (result.status === 'success') return result.data;
  return result.status;
}
```

Discriminated union исключает состояние «success, но data отсутствует». Набор независимых optional-полей этого не гарантирует. При пересечении несовместимых свойств, например string и number для одного ключа, можно получить never.

**Уточнение.** Для исчерпывающего switch передай необработанный вариант функции `(value: never) => never`: новый вариант выявит неполную обработку. **Практика:** добавь cancelled и обнови обработчик.

<a id="ts-03"></a>

## TS-03. Что дают generics и ограничения?

**Ответ.** Generic сохраняет связь между входными и выходными типами, а не просто заменяет any красивой буквой. Ограничение задаёт операции, которые разрешены над неизвестным конкретным типом.

```ts
function getProperty<T, K extends keyof T>(object: T, key: K): T[K] {
  return object[key];
}
const name = getProperty({ name: 'Игнат', age: 30 }, 'name'); // string
// getProperty({ name: 'Игнат' }, 'missing'); // ошибка типов
```

K связан с ключами T, T[K] — тип выбранного свойства. Возврат просто `T[keyof T]` дал бы объединение всех значений и потерял точность выбранного ключа.

**Практика.** Напиши `groupBy<T>(items, keyFn)` с результатом Map<string, T[]> и объясни, почему keyFn делает функцию применимой к разным моделям.

<a id="ts-04"></a>

## TS-04. keyof, typeof, as const и satisfies — в чём разница?

**Ответ.** keyof получает ключи типа; typeof в позиции типа получает тип значения; as const сохраняет литералы и делает свойства литеральной структуры readonly на уровне типов. satisfies проверяет соответствие контракту, сохраняя полезную точность выражения. Это не Object.freeze и не runtime-защита.

```ts
const routes = { home: '/', orders: '/orders' } as const;
type RouteName = keyof typeof routes; // 'home' | 'orders'
type Path = typeof routes[RouteName]; // '/' | '/orders'
const palette = {
  success: '#00aa00', error: '#aa0000',
} satisfies Record<'success' | 'error', string>;
```

**Ошибка.** `as SomeType` может скрыть проблему, тогда как satisfies её обнаруживает. **Практика:** добавь неверный ключ и неверный тип значения и объясни сообщения компилятора.

<a id="ts-05"></a>

## TS-05. Как устроены mapped types и utility types?

**Ответ.** Mapped type проходит по набору ключей и строит новый тип свойств. Partial делает свойства необязательными, Required — обязательными, Readonly запрещает запись через этот тип, Pick/Omit выбирают ключи. Обычные версии этих преобразований поверхностные.

```ts
type Flags<T> = { [K in keyof T]: boolean };
type User = { id: string; profile: { name: string } };
type UserFlags = Flags<User>; // { id: boolean; profile: boolean }
type EditUser = Partial<Pick<User, 'profile'>>;
```

Partial<User> не означает частичный вложенный profile: если он передан, его name всё ещё обязателен. Runtime-объект преобразование типов не меняет.

**Практика.** Определи payload редактирования, в котором id обязателен, а name и email необязательны. Реши отдельно, означает ли undefined «не менять» или «удалить».

<a id="ts-06"></a>

## TS-06. Как работают conditional types, infer и рекурсивные типы?

**Ответ.** Conditional type выбирает ветку по совместимости типов. infer извлекает часть структуры. Для параметра типа union условие часто распределяется по участникам; оборачивание в tuple меняет это поведение.

```ts
type ElementOf<T> = T extends readonly (infer U)[] ? U : T;
type A = ElementOf<string[]>; // string
type B = ElementOf<string[] | number[]>; // string | number
type IsString<T> = [T] extends [string] ? true : false;
type C = IsString<string | number>; // false
type Tree<T> = { value: T; children: Tree<T>[] };
```

Рекурсивный тип описывает рекурсивную структуру; это не исполнение рекурсивной функции. Чрезмерно сложные преобразования ухудшают диагностику и время проверки. Для вложенных Promise обычно достаточно встроенного Awaited.

**Практика.** Получи тип результата async-функции через `Awaited<ReturnType<typeof fn>>`. Объясни, почему generic HTTP-клиента всё равно не заменяет TS-01.

## Мини-собеседование

Смоделируй загрузку заказа, проверь unknown JSON, напиши generic-доступ к свойству, объясни shallow readonly и составь частичный update-контракт. Критерий: обходишься без необоснованных any/as и объясняешь ограничения.

## Источники

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html).
- [Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html).
- [Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html).
