# 모듈 import / export — default vs named

ES Module의 내보내기/가져오기 방식은 두 가지이며, 이름을 다루는 규칙이 다르다.

## default export — 가져올 때 이름 자유

파일당 **하나**만 가능하고, **이름이 없다**. 가져오는 쪽에서 마음대로 이름을 붙인다.

```tsx
// Profile.tsx
export default function Profile() { ... }
```

```tsx
import JuJinProfile from './Profile'   // 이름 자유
import Anything from './Profile'       // 이것도 됨
```

`{}` 없이 쓰고, 이름은 가져오는 쪽이 정한다.

## named export — `as`로 별명

파일당 **여러 개** 가능하고, **이름 자체가 식별자**다. 가져올 때 그 이름을 정확히 써야 하며, 바꾸려면 `as`를 쓴다.

```tsx
// utils.ts
export function formatDate() { ... }
export const MAX = 100
```

```tsx
import { formatDate, MAX } from './utils'              // 이름 일치
import { formatDate as fmt, MAX as LIMIT } from './utils'  // as로 변경
```

## 왜 다른가

| | default | named |
|---|---|---|
| 개수 | 파일당 1개 | 파일당 여러 개 |
| 이름 | 없음 (가져올 때 정함) | 있음 (정해진 이름) |
| 이름 변경 | `{}` 없이 자유 | `{ 이름 as 새이름 }` |

default는 애초에 이름이 없으니 가져오는 쪽이 정하는 것이고, named는 이름이 정해져 있으니 `as`로 별명을 붙이는 개념이다.

## 둘을 함께 쓰기

한 파일에 default와 named가 같이 있을 수 있다.

```tsx
// Profile.tsx
export default function Profile() { ... }
export function Avatar() { ... }
```

```tsx
import JuJinProfile, { Avatar as UserAvatar } from './Profile'
//     └ default(자유)    └ named(as로 변경)
```

콤마 기준으로 앞은 default(자유 이름), `{}` 안은 named(`as` 사용)다.
