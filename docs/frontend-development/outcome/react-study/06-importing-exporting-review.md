# 리뷰 — import/export와 Java 비유

> [Importing and Exporting Components](https://ko.react.dev/learn/importing-and-exporting-components) 페이지를 읽고 정리한 감상과, 그에 대한 평가. 메커니즘 정리는 [02](02-module-import-export.md) 참고.

## 나의 감상

- `default export`는 자바에서 기본적으로 클래스를 사용하는 방식과 유사하다.
- `named exports`는 static 메서드 사용법과 비슷하다.
- import 시 `default export function`을 다른 이름으로 가져올 수 있다는 건 처음엔 자유가 아니라 **방임**처럼 느껴졌다. 그러나 함께 스터디하며 홍수석님과의 대화로, 같은 컴포넌트 이름의 파일이 다른 패키지에 존재할 때의 **대응책**임을 확인했다. 즉 import 시 `as`나 다른 이름을 쓰는 것은 단순히 컴포넌트를 가져왔다는 것을 넘어, **변수명 선언 역할도 겸한다**고 느꼈다.

## 평가

**세 관찰 모두 방향이 맞고, 두 곳은 더 날카롭게 다듬을 수 있다.**

**① default export ≈ Java의 클래스 사용 — 적절하다.**
Java는 보통 파일 하나에 public 클래스 하나(파일명 = 클래스명)를 두고, 그 클래스를 가져와 쓴다. default export도 "이 파일의 대표 하나"라는 점에서 같은 직관이다. 파일당 하나라는 제약도 닮았다.

**② named exports ≈ static 메서드 — 비유를 더 좁히면 Java의 `import static`이다.**
단순히 static 메서드라기보다, **여러 멤버 중 이름을 콕 집어 가져오는** 구조가 핵심이다.

```java
// Java
import static com.example.Utils.formatDate;   // 이름을 지정해 가져옴
```
```tsx
// React/JS — 거의 1:1로 대응
import { formatDate } from './utils'
```

`utils.ts`에서 여러 named export를 두고 필요한 것만 골라 import하는 건, Java에서 한 유틸 클래스의 여러 static 멤버를 `import static`으로 골라 쓰는 것과 같은 모양이다.

**③ "방임이 아니라 변수명 선언" — 가장 좋은 통찰이고, 정확하다.**
ES Module의 import는 단순한 "파일 가져오기"가 아니라, **이 모듈 안에서 쓸 로컬 식별자(변수)를 묶는(binding) 선언**이다. 그래서 default는 이름이 없으니 가져오는 쪽이 변수명을 정하고, named는 `as`로 다른 변수명을 붙인다.

여기서 Java와의 차이가 통찰을 오히려 강화한다 — **Java는 import 이름을 바꿀 수 없다.** 이름이 충돌하면 별칭 대신 패키지 전체 경로(fully qualified name)를 그대로 써야 한다.

```java
// Java — 별칭 불가, 충돌 시 풀 경로
com.a.Profile p1 = new com.a.Profile();
com.b.Profile p2 = new com.b.Profile();
```
```tsx
// JS — import에서 변수명을 새로 선언해 충돌 해소
import Profile from './a/Profile'
import { Profile as AdminProfile } from './b/Profile'
```

즉 "import = 변수 선언"이라는 감상은, 별칭이 없는 Java보다 JS의 import가 **더 변수 선언에 가깝다**는 점에서 정확히 맞다. 홍수석님과의 대화로 도달한 "다른 패키지의 동명 대응"이라는 결론은 실제 이 기능의 대표 용도다.

**정리:** default↔클래스, named↔`import static`, import↔변수 선언 — 세 비유 모두 본질을 잡았다. named는 "static 메서드"보다 "`import static`"으로, import의 자유는 "방임"이 아니라 "Java에는 없는 별칭(변수 선언) 능력"으로 자리매김하면 직관이 완성된다.
