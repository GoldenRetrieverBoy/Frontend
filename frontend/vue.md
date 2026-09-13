# Блок 03. Vue 3

[План](../README.md) · Предыдущий: [TypeScript](../fundamentals/typescript.md) · Следующий: [HTML/CSS](../frontend/html-css-ui.md)

Composition API, примеры для Vue 3.5+, если явно не сказано иначе. Небольшие SFC показывают одну идею и специально не разбиты на несколько файлов.

<a id="vue-01"></a>

## VUE-01. Как работает реактивность и чем ref отличается от reactive?

**Ответ.** При чтении реактивного значения внутри эффекта Vue регистрирует зависимость. При изменении уведомляет зависимые эффекты. reactive использует Proxy для объектов; ref предоставляет отслеживаемое свойство value и может содержать примитив или объект. Обычный ref с объектом поддерживает глубокую реактивность; shallowRef отслеживает замену value без глубокого преобразования объекта.

```ts
import { reactive, toRef, shallowRef } from 'vue';
const state = reactive({ count: 0 });
const snapshot = state.count;
const count = toRef(state, 'count');
state.count++;
console.log(snapshot, count.value); // 0, 1
const external = shallowRef({ count: 0 });
external.value.count++; // само по себе не уведомит зависимых потребителей
external.value = { count: 2 }; // уведомит
```

Чтение примитива в локальную переменную теряет связь с исходным свойством. Вложенный проксированный объект при деструктуризации может остаться реактивным — нельзя говорить «любая деструктуризация всё ломает». Для destructured defineProps в Vue 3.5 есть отдельное преобразование компилятора; это не общее правило JavaScript.

**Практика:** объясни `watch(() => state.count, fn)` против `watch(state.count, fn)`. Второй передаёт число, а не наблюдаемый источник.

<a id="vue-02"></a>

## VUE-02. computed, method, watch и watchEffect — как выбрать?

**Ответ.** computed — производное значение с кэшированием по реактивным зависимостям. Метод выполняется при вызове. watch нужен для эффекта с явно выбранными источниками; watchEffect автоматически отслеживает синхронно прочитанные зависимости. Чтения после первого await в async watchEffect автоматически в эту фазу отслеживания не попадают.

```ts
import { shallowRef, computed, watch } from 'vue';
const price = shallowRef(100);
const quantity = shallowRef(2);
const total = computed(() => price.value * quantity.value);
watch(total, value => console.log('Новый итог:', value));
```

Запись total в отдельный ref через watch дублирует состояние. Сеть и мутации внутри computed создают плохо управляемые эффекты. `computed(() => Date.now())` не обновляется от течения времени: реактивных зависимостей нет.

**Практика:** выбери механизм для фильтрации списка, сохранения черновика и фокуса после открытия окна. Объясни отдельный выбор для каждого.

<a id="vue-03"></a>

## VUE-03. Когда обновляется DOM и зачем nextTick?

**Ответ.** Изменение состояния не означает немедленное обновление DOM: Vue группирует обновления. nextTick ожидает завершения ожидаемого обновления DOM Vue, но не гарантирует фактическую отрисовку пикселей браузером или завершение сети. Watcher с flush:'post' выполняется после обновления DOM своего компонента.

```vue
<script setup lang="ts">
import { shallowRef, nextTick, useTemplateRef } from 'vue';
const visible = shallowRef(false);
const input = useTemplateRef<HTMLInputElement>('input');
async function open() {
  visible.value = true;
  await nextTick();
  input.value?.focus();
}
</script>
<template>
  <button @click="open">Открыть поле</button>
  <input v-if="visible" ref="input" aria-label="Поиск" />
</template>
```

onMounted подходит для работы с клиентским DOM, onUnmounted — для освобождения ресурсов. mounted не означает, что завершились все произвольные async-запросы потомков. Hooks регистрируем в допустимом контексте setup; синхронно созданные там watchers останавливаются при unmount, собственные таймеры и внешние подписки требуют очистки.

**Практика:** почему setTimeout(0) — слабая замена nextTick для ожидания DOM Vue?

<a id="vue-04"></a>

## VUE-04. Как организовать props, events и v-model?

**Ответ.** Родитель владеет состоянием и передаёт входы через props. Потомок сообщает о намерении событием. v-model компонента оформляет контракт значения и обновления; defineModel в Vue 3.4+ упрощает его запись. Component events не всплывают как DOM events.

```vue
<script setup lang="ts">
const query = defineModel<string>({ required: true });
const emit = defineEmits<{ submit: [query: string] }>();
</script>
<template>
  <form @submit.prevent="emit('submit', query)">
    <input v-model="query" aria-label="Поисковый запрос" />
    <button type="submit">Найти</button>
  </form>
</template>
```

Мутация вложенного объекта prop технически может менять объект родителя, но делает поток данных неявным. Для редактируемого черновика решаем, когда копировать входы, как отменять изменения и как реагировать на новый prop.

**Практика:** спроектируй форму с «Сохранить»/«Отмена», чтобы ввод не менял исходные данные до сохранения.

<a id="vue-05"></a>

## VUE-05. Когда slots, provide/inject и attrs?

**Ответ.** Slot передаёт содержимое от родителя, scoped slot позволяет ребёнку предоставить этому содержимому данные. provide/inject передаёт контекст по дереву без промежуточных props; зависимости должны иметь ясный контракт, лучше InjectionKey. attrs содержит не объявленные как props/emits входы; для нескольких корней нужно явно решить, куда их направить.

```vue
<!-- Учебный фрагмент шаблона списка: item задан циклом. -->
<slot name="item" :item="item">
  {{ item.name }}
</slot>
```

Slot компилируется в области родителя; данные ребёнка доступны через slot props. provide/inject подходит контексту формы, а не любому обмену данными. Мутации удобно оставить у provider через действия. Бездумное `$attrs` на внутренний div может направить aria-label и обработчики мимо настоящей кнопки.

**Практика:** опиши API переиспользуемой таблицы: props для данных, slot для ячейки, event для выбора, attrs для корректного DOM-элемента.

<a id="vue-06"></a>

## VUE-06. Зачем key, v-if/v-show и async components?

**Ответ.** key определяет идентичность элемента при сопоставлении деревьев. Индекс может связать локальное состояние с другой строкой после перестановки. v-if создаёт/уничтожает ветку, v-show оставляет её и меняет отображение. Dynamic component выбирает тип компонента; defineAsyncComponent позволяет загружать определение асинхронно.

```ts
import { defineAsyncComponent, h } from 'vue';
const Report = defineAsyncComponent(() => import('./Report.vue'));
const renderLabel = () => h('span', { class: 'label' }, 'Отчёт');
```

Это фрагмент: Report.vue должен существовать в приложении. Render function создаёт виртуальные узлы и полезна для программно формируемой структуры; обычный template чаще проще. Async-компоненту нужны состояния ожидания/ошибки. KeepAlive сохраняет экземпляры и требует учитывать activated/deactivated; лимиты важны для памяти.

**Практика:** список input с key=index после сортировки показывает чужие локальные значения. Объясни причину и выбери устойчивый key.

<a id="vue-07"></a>

## VUE-07. Как писать composable и очищать асинхронные эффекты?

**Ответ.** Composable инкапсулирует связанное реактивное поведение и его жизненный цикл. Вход должен сохранять реактивную связь, выход — давать явное состояние и действия. В каждом вызове можно иметь отдельное состояние; модульная переменная делает его общим, что особенно опасно для пользовательских данных в SSR.

```ts
import { shallowRef, watch, type Ref } from 'vue';
export function useText(url: Ref<string>) {
  const text = shallowRef('');
  const error = shallowRef<unknown>(null);
  watch(url, async (value, _old, onCleanup) => {
    const controller = new AbortController();
    let active = true;
    onCleanup(() => { active = false; controller.abort(); });
    error.value = null;
    try {
      const response = await fetch(value, { signal: controller.signal });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const result = await response.text();
      if (active) text.value = result;
    } catch (cause) {
      if (active) error.value = cause;
    }
  }, { immediate: true });
  return { text, error };
}
```

Вызывается синхронно в setup. Это пример клиентской загрузки текста; политика сохранения предыдущих данных и loading задаётся отдельно. active защищает состояние от устаревшего эффекта, abort сокращает лишнюю работу.

**Практика:** добавь loading с той же защитой и тест «старый запрос заканчивается после нового».

## Мини-собеседование

Разобрать реактивность; выбрать computed/watch; объяснить nextTick; исправить key; спроектировать composable. Критерий: понятны владельцы состояния, подписки и момент очистки.

## Источники

- [Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth.html).
- [Watchers](https://vuejs.org/guide/essentials/watchers.html).
- [Vue Guide](https://vuejs.org/guide/introduction.html) — компоненты, slots, composables и lifecycle.

<a id="vue-08"></a>

## VUE-08. Что возвращает render-функция и когда нужен h()?

**Короткий ответ.** Render-функция описывает результат отображения через виртуальные узлы. h() создаёт такой узел из типа, свойств и дочернего содержимого. Обычно шаблон проще; render-функция нужна, когда построение дерева удобнее выразить программно.

Это маленький учебный компонент, чтобы увидеть механизм; для такой кнопки в приложении достаточно обычного template.

```js
import { h, ref } from 'vue';

export default {
  setup() {
    const count = ref(0);
    return () => h('button', {
      type: 'button',
      onClick: () => count.value++,
    }, `Счёт: ${count.value}`);
  },
};
```

**По шагам:** setup создаёт состояние экземпляра. Возвращённая функция читает count и создаёт описание кнопки. Нажатие изменяет count, Vue обновляет отображение. h() не равен document.createElement().

**Практика:** что сломается, если из setup вернуть сразу h(...), а не функцию?

<details>
<summary>Разбор</summary>

setup должен вернуть render-функцию либо объект данных для шаблона. Готовый VNode не задаёт повторно вызываемую функцию отображения. Создавай узел внутри возвращённой функции. Для списка создавай отдельные VNode со стабильными key. Для слотов компонентов передавай функции слотов.

</details>

**Уточнение:** делает ли ручной render компонент автоматически быстрее? Нет: выбор требует причины, шаблонный компилятор уже выполняет оптимизации.

Источник: [Vue: Render Functions](https://vuejs.org/guide/extras/render-function.html).
