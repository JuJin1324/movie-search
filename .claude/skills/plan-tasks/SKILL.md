---
name: plan-tasks
description: "선택된 코딩 Story 하나를 PR 단위 Task 목록으로 분해한다. plan-stories에서 코딩 Story 하나를 골라 진입할 때 사용 — 비코딩 Story에는 호출하지 않음. 다음 단계는 execute-task."
---

# Plan Tasks

## 목적

선택된 *코딩 Story* 하나를 *PR 단위 Task 목록*으로 분해한다. 비코딩(문서) Story에는 호출하지 않는다 — 그 경우 Story 자체가 실행 단위.

코딩 Story를 그대로 실행하면 여러 흩어진 파일에 한꺼번에 변경이 가해져 *한 번에 검토할 수 있는 단위*가 비대해진다. plan-tasks는 그 변경 묶음을 *PR 단위*로 잘라 검토 가능성을 유지하는 자리. 비코딩 Story는 보통 한 문서·한 자리에 변경이 모이므로 분해 없이도 검토 가능 — plan-tasks가 필요 없다.

## 입력

plan-stories 산출물에서 선택된 *코딩 Story* 하나.

## 출력

`epics/<epic-slug>/3-plan/storyN/tasks.md` *초안*. 해당 Story의 Task 목록 문서. 전체 흐름과 Task별 상세가 한 자리에 정리됨. 한 Story = 한 디렉터리. 실행 산출물(`taskN-executed.md`)은 같은 디렉터리에 들어가지만 *그건 execute-task의 자리*.

### 템플릿

```markdown
# Story N — Task 목록

선행: [../stories.md](../stories.md) §Story N

## 전체 흐름

`mermaid 다이어그램 — Task 간 순서·의존관계`

(Task 간 흐름 한 줄 설명)

---

## Task 1 — {제목}

### 목표
### 핵심 작업
### 이 Task에서 하지 않을 것
### 완료 기준

---

## Task 2 — {제목}
...

## 다음 사이클

(이 Story 이후 무엇으로 이어지는지 — 보통 *다음 Story의 plan-tasks는 진입 직전*)
```

산출물 자체가 완성본이 아니다 — 사용자가 AI 에이전트와 대화하며 Task 단위·완료 기준을 채워간다. 스킬은 *진입점*과 *초안*을 제공할 뿐.

## 작동 방식

핑퐁. 전체 흐름을 먼저 합의한 뒤 Task 단위로 사용자와 주고받으며 보충한다.

1. **전체 흐름 다이어그램** — Story를 Task 후보로 쪼개 mermaid로 순서·의존관계를 그린다. *왜 이 입자로 쪼갰는지*, *왜 이 순서인지*를 설명하고 확인받는다. Task 수가 *Story 입자에 맞는가*도 같이 — Story가 1일이면 Task 2~3개 정도. 4개 이상으로 잘게 자르면 안티패턴(*실행 방법을 과도하게 규정*)에 가까워짐.

2. **Task별 상세** — Task 1부터 순서대로 *한 Task씩* 작성. 각 Task마다: AI가 *목표 / 핵심 작업 / 하지 않을 것 / 완료 기준*을 먼저 적고, 사용자가 보충하고 싶은 자리를 짚으면 그 자리에서 갱신. 다음 Task로 넘어가기 전에 합의.

3. **다음 사이클 메모** — Task 목록이 끝나면 *execute-task로 넘어간다*는 점만 짧게. 다음 Story의 plan-tasks는 *그 Story 진입 직전*에 별도 사이클로 — 모든 Story의 Task를 미리 다 짜지 않는다.

### Task 작성 시 주의

- **하나의 의도, 하나의 변경 이유, 하나의 검토 이야기** — 한 Task에 서로 다른 목적이 섞이지 않게.
- **완료 기준은 *상태*로** — *~한다*가 아니라 *~인 상태다*. 비코딩이면 *사용자가 무엇을 확인하면 끝났다고 볼 수 있는가*.
- **작은 ADR은 Task 안의 결정으로 흡수** — 별도 Task로 떼지 않음. 결정이 *Task 자체를 갈라놓을 만큼 크면* 그때 분리.
- **1:1이면 1:1** — Story가 작으면 Task 1개도 맞다. 억지로 쪼개지 않음.

## 경계

- **비코딩 Story에는 호출하지 않는다.** 문서 작업 같은 비코딩 Story는 Story 자체가 실행 단위 — plan-tasks를 건너뛰고 바로 execute-task로 간다.
- **plan-stories의 자리는 여기서 안 한다.** Story 자체를 다시 쪼개거나 Story 목록을 새로 짜야 한다고 느끼면 plan-stories로 돌아간다.
- **실행은 여기서 안 한다.** Task 실행과 산출물(`taskN-executed.md`)은 execute-task의 자리. 여기서는 *Task 목록*까지.
- **실행 방법을 과도하게 규정하지 않는다.** Task는 *무엇을 달성할지*와 *어디서 멈출지*를 정한다. *어떻게 할지*는 실행자에게 위임.
- **모든 Story의 Task를 한 번에 짜지 않는다.** 각 Story 진입 직전에 별도 사이클로. 미리 다 짜면 *다음 Story의 입력*(앞 Story의 마찰 메모)을 못 쓴다.
