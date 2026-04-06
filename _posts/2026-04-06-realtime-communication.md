---
layout: post
title: "실시간 통신 — WebSocket vs SSE 선택 이유"
description: "양방향 제어가 필요한 Live 모드에서 SSE 대신 WebSocket을 선택한 이유와 구현"
date: 2026-04-06
category: Realtime
tags: [WebSocket, FastAPI, SSE, streaming]
---

## 기술 목록

| 기술 | 용도 |
|------|------|
| WebSocket (FastAPI native) | Live 모드 실시간 이벤트 스트리밍 |
| Server-Sent Events (SSE) | 검토됨, 미채택 |

---

## WebSocket을 선택한 이유

<div class="callout why">
<div class="callout-title">SSE가 아닌 WebSocket</div>

클라이언트가 서버로 `start_streaming` / `stop_streaming` / `ping` 메시지를 보내야 하는 **양방향 프로토콜**이 필요하다.

SSE는 단방향(서버 → 클라이언트)만 가능하므로:
- `stop_streaming` 신호를 별도 REST API로 구현해야 함
- 연결 상태 추적이 복잡해짐
- 클라이언트 재연결 로직이 분산됨

WebSocket 하나로 모든 메시지를 처리한다.
</div>

---

## 메시지 프로토콜

### 클라이언트 → 서버

```ts
type ClientMessage =
  | { type: "start_streaming"; project_id: string; interval_sec: number }
  | { type: "stop_streaming" }
  | { type: "ping" }
```

### 서버 → 클라이언트

```ts
type ServerMessage =
  | { type: "snapshot"; data: LiveSnapshot; timestamp: string }
  | { type: "error"; message: string }
  | { type: "pong" }
  | { type: "stopped" }
```

---

## FastAPI WebSocket 구현

```python
from fastapi import WebSocket, WebSocketDisconnect
import asyncio

@router.websocket("/ws/live")
async def live_stream(websocket: WebSocket):
    await websocket.accept()
    streaming_task: asyncio.Task | None = None

    try:
        while True:
            data = await websocket.receive_json()

            match data["type"]:
                case "start_streaming":
                    if streaming_task:
                        streaming_task.cancel()
                    streaming_task = asyncio.create_task(
                        stream_loop(websocket, data["project_id"], data["interval_sec"])
                    )

                case "stop_streaming":
                    if streaming_task:
                        streaming_task.cancel()
                        streaming_task = None
                    await websocket.send_json({"type": "stopped"})

                case "ping":
                    await websocket.send_json({"type": "pong"})

    except WebSocketDisconnect:
        if streaming_task:
            streaming_task.cancel()


async def stream_loop(ws: WebSocket, project_id: str, interval: int):
    while True:
        snapshot = await collect_all(project_id)
        await ws.send_json({"type": "snapshot", "data": snapshot.dict()})
        await asyncio.sleep(interval)
```

---

## 프론트엔드 연결

```ts
// Zustand live 스토어
const useLiveStore = create<LiveState>((set, get) => ({
  ws: null,
  status: "disconnected",

  connect: (projectId: string) => {
    const ws = new WebSocket(`ws://localhost:8000/ws/live`)
    ws.onopen = () => {
      set({ ws, status: "connected" })
      ws.send(JSON.stringify({ type: "start_streaming", project_id: projectId, interval_sec: 5 }))
    }
    ws.onmessage = (e) => {
      const msg = JSON.parse(e.data)
      if (msg.type === "snapshot") {
        set({ snapshot: msg.data, lastUpdated: msg.timestamp })
      }
    }
    ws.onclose = () => set({ ws: null, status: "disconnected" })
  },

  disconnect: () => {
    get().ws?.send(JSON.stringify({ type: "stop_streaming" }))
    get().ws?.close()
    set({ ws: null, status: "disconnected" })
  },
}))
```

---

## SSE와의 비교

| 항목 | WebSocket | SSE |
|------|-----------|-----|
| 방향 | 양방향 | 단방향 (서버→클라이언트) |
| 프로토콜 | ws:// / wss:// | HTTP/HTTPS |
| 자동 재연결 | 직접 구현 | 브라우저 내장 |
| HTTP/2 지원 | 별도 처리 | 기본 지원 |
| 이 프로젝트 적합성 | **필수** (제어 메시지 필요) | 부적합 |
